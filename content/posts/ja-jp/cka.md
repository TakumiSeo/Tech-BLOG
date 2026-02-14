Title: CKA学習メモ: Kubernetes 基礎（Pod / Namespace / Controller / Service）
Date: 2026-02-14
Slug: cka
Lang: ja-jp
Category: notebook
Tags: kubernetes,cka
Summary: CKAに向けてKubernetesの基本概念（Pod、Namespace、コントローラ、Service、ラベル等）を図解して整理します。

CKA の勉強用に、いただいた文章を **図解（Mermaid + ASCII）** と **やさしい説明** で整理します。

---

## 1. Kubernetes は「コンテナを直接」ではなく「オブジェクト」を管理する

Kubernetes は「コンテナをデプロイして管理する」ためのオーケストレーション基盤ですが、実際には **コンテナ単体を直接管理する** というより、
**Pod / Deployment / Service などの Kubernetes オブジェクト** を通して状態（あるべき姿）を管理します。

ポイント:

- Kubernetes は「宣言した理想状態（Desired）」に「実状態（Current）」を近づけ続ける仕組み
- コンテナは多くの場合 **Pod の一部** として扱われる

---

## 2. Pod とは: 1つ以上のコンテナをまとめる最小の実行単位

**Pod** は Kubernetes における最小のデプロイ単位です。
1つの Pod は、1つ以上のコンテナで構成され、次のようなものを **共有** します。

- **IP アドレス（= Pod IP）**
- **ストレージ（Volume）**
-（文脈上）同じ “実行環境” としてのまとまり（例: 同じノード上で一緒に動く）

よくある構成:

- メインのアプリコンテナが処理を実行
- サイドカーなどの補助コンテナがログ転送・プロキシ・設定配布などで支援

### 図: Pod の中身（イメージ）

```mermaid
flowchart TB
  subgraph Pod [Pod]
    direction TB
    Net[Pod IP / Network]
    Vol[Shared Volume]
    subgraph C1 [Container: main app]
      A[Application]
    end
    subgraph C2 [Container: sidecar]
      S[Support: log/agent/proxy]
    end
    Net --- C1
    Net --- C2
    Vol --- C1
    Vol --- C2
  end
```

ASCII での見え方（Mermaidが表示されない場合）:

```
+------------------------------+
| Pod (1つのIPを持つ)          |
|  - Shared Volume             |
|                              |
|  +-----------+  +----------+ |
|  | main app  |  | sidecar  | |
|  | container |  | container| |
|  +-----------+  +----------+ |
+------------------------------+
```

---

## 3. Namespace とは: マルチテナント/リソース分割のための「境界」

Kubernetes はリソース管理やマルチテナント（チーム/環境の分離）を考慮して、
**Namespace** でオブジェクトを区別できるようにしています。

### スコープの違い

- **クラスタスコープ（cluster-scoped）**: クラスタ全体に属する
- **Namespaced**: どれか1つの Namespace に所属する

例（ざっくり）:

- cluster-scoped: Node, Namespace, PersistentVolume, CustomResourceDefinition
- namespaced: Pod, Service, Deployment, ReplicaSet, Job, CronJob, ConfigMap, Secret

### 「Namespace で分割される」ので Service が重要になる

Namespace によってリソースは分割されるため、Pod 間連携（安定した到達先）には
**Service** のような仕組みが必要になります。

---

## 3.5 クラスター全体イメージ（Control Plane / Worker / Namespace）

「クラスタの中で何がどこにいるか」を、まずは1枚で把握する用の図です。

ポイント:

- **Control Plane** は「状態を保存し、調整して、割り当てる」側
- **Worker Node** は「Pod（コンテナ）を実際に動かす」側
- 多くの操作は `kube-apiserver` を経由して行われる
- Namespace は論理的な区切り（ノードの物理的分割ではない）

```mermaid
flowchart TB
  subgraph Cluster [Kubernetes Cluster]
    direction TB

    subgraph CP [Control Plane]
      direction TB
      API[kube-apiserver]
      ETCD[etcd]
      CM[kube-controller-manager]
      SCH[kube-scheduler]
      API --- ETCD
      CM --> API
      SCH --> API
    end

    subgraph W1 [Worker Node]
      direction TB
      K1[kubelet]
      R1[container runtime]
      K1 --> R1

      subgraph NS1 [Namespace: team-a]
        direction TB
        SVC1[Service]
        P1[Pod]
        P2[Pod]
        SVC1 --> P1
        SVC1 --> P2
      end
    end

    subgraph W2 [Worker Node]
      direction TB
      K2[kubelet]
      R2[container runtime]
      K2 --> R2

      subgraph NS2 [Namespace: team-b]
        direction TB
        P3[Pod]
      end
    end

    K1 --> API
    K2 --> API
  end
```

---

## 3.6 Python runtime のWebマイクロサービスをクラスタでホストするイメージ

「Python の runtime を持つコンテナ（例: FastAPI/Flask/Django）で Web サイト/API をマイクロサービスとして動かす」時の典型パターンです。

ざっくり流れ:

- 外部アクセス（ブラウザ/クライアント） → **Ingress（入口）**
- Ingress は **Ingress Controller（例: nginx ingress）** が実際にルーティング
- ルーティング先は **Service（安定した宛先）**
- Service が **ラベルで Pod を選択**（Pod は Deployment/ReplicaSet が管理）

```mermaid
flowchart TB
  Client["Client<br/>(Browser / App)"] --> DNS["DNS<br/>example.com"]
  DNS --> LB["Load Balancer<br/>(Public IP)"]
  LB --> IC["Ingress Controller<br/>(runs as Pods)"]
  IC --> ING["Ingress Resource<br/>host/path rules"]

  subgraph Cluster [Kubernetes Cluster]
    direction TB

    subgraph NS [Namespace: prod]
      direction TB
      SVC["Service<br/>web-python-svc"]
      DEP["Deployment<br/>web-python"]
      RS[ReplicaSet]
      P1["Pod<br/>Python runtime + app"]
      P2["Pod<br/>Python runtime + app"]

      ING --> SVC
      SVC --> P1
      SVC --> P2
      DEP --> RS
      RS --> P1
      RS --> P2

      CMAP[ConfigMap] -.-> P1
      SECRET[Secret] -.-> P1
      CMAP -.-> P2
      SECRET -.-> P2
    end
  end
```

覚えどころ（CKA向け）:

- **Ingress は「入口のルール」**、実処理は Ingress Controller
- **Service は Pod の IP が変わっても安定**（selector で追従する）
- **Deployment はローリングアップデート**やスケールの中心（Pod を直接ではなく ReplicaSet 経由で管理）

---

## 4. オーケストレーションの本質: コントローラの監視ループ

オーケストレーションは、**コントローラ（controller / operator）** と呼ばれる監視ループで実現します。

基本動作:

1. コントローラが `kube-apiserver` から対象オブジェクトの状態を観測
2. 「望ましい状態」と一致していなければ変更を加える
3. 一致するまで繰り返す

多くの標準コントローラは `kube-controller-manager` に集約されています。
また CRD（Custom Resource Definition）により、独自のオペレータ/コントローラを追加できます。

### 図: Desired → Current を近づけるループ

```mermaid
sequenceDiagram
  participant U as User (kubectl)
  participant A as kube-apiserver
  participant C as Controller/Operator
  participant S as Scheduler
  participant K as kubelet
  participant R as Container Runtime

  U->>A: オブジェクトを作成/更新（Desired state）
  loop reconcile
    C->>A: 現在の状態をwatch/list
    C->>A: 足りない分を作る/直す（例: ReplicaSet更新）
  end
  S->>A: Podにノード割り当て
  K->>A: PodSpecを取得
  K->>R: イメージ取得/コンテナ作成・停止
```

---

## 5. Deployment → ReplicaSet → Pod: デフォルトの（超重要）流れ

コンテナのための代表的コントローラは **Deployment** です。
ただし Deployment は Pod を直接いじるのではなく、基本的に次の関係になります。

- **Deployment** が **ReplicaSet** を管理
- **ReplicaSet** が **Pod** の数を PodSpec に従って増減

### 図: Deployment から Pod が動くまで

```mermaid
flowchart LR
  D[Deployment] --> RS[ReplicaSet]
  RS -->|create/delete| P1[Pod]
  RS -->|create/delete| P2[Pod]
  P1 -->|PodSpec| K1[kubelet]
  P2 -->|PodSpec| K2[kubelet]
  K1 --> CR1[container runtime]
  K2 --> CR2[container runtime]
```

補足:

- **PodSpec** は「どのイメージを」「何個」「どんな設定で」などを記述
- `kubelet` がノード上で PodSpec を実行に落とし込み、コンテナの作成/終了を行う

---

## 6. Service / Endpoint: ラベルを使って通信先を束ねる

Service（および関連するオペレータ）は、ラベルに基づいてネットワーク接続（到達先の集合）を管理します。

ざっくり言うと:

- Service は **selector（ラベル条件）** で「どの Pod を束ねるか」を決める
- 実際の到達先（Pod IP の集合）が Endpoint / EndpointSlice として管理される
- Service は **Pod間 / Namespace間 / クラスタ外部との通信** に使われる

### 図: Service が Pod を選ぶ

```mermaid
flowchart TB
  SVC["Service<br/>selector: app=web"] --> EP[Endpoints / EndpointSlice]
  EP --> P1["Pod app=web"]
  EP --> P2["Pod app=web"]
  EP -.-> P3["Pod app=batch<br/>(選ばれない)"]
```

---

## 7. Job / CronJob: バッチ（1回 or 定期）

- **Job**: 1回きり、あるいは完了まで再試行するタスク向け
- **CronJob**: cron 形式で定期実行する Job を作る

図（イメージ）:

```mermaid
flowchart LR
  CJ[CronJob] -->|schedule| J1[Job]
  J1 --> P["Pod (run-to-completion)"]
```

---

## 8. 大量リソース管理の鍵: Label / Selector

千単位の Pod を百単位のノードで運用する時、名前や UID を1つ1つ扱うのは現実的ではありません。
そこで **label（任意の文字列のキー/値）** を使って、まとまりで操作します。

代表例:

- `app=web`
- `env=prod`
- `tier=frontend`

Label が効く場面:

- Service が Pod を選ぶ（selector）
- Deployment/ReplicaSet が管理対象を紐づける
- `kubectl get pods -l app=web` のような絞り込み

---

## 9. Node の割り当て制御: Taint / Toleration

ノードには **Taint** を付けられます。
Taint があるノードは、Pod 側に対応する **Toleration** がない限り、
基本的に「そのノードに Pod を載せない（回避する）」挙動になります。

イメージ:

```
Node A: taint=dedicated=team-a:NoSchedule
	- tolerationを持つPodだけが乗れる

Node B: taintなし
	- 通常のPodが乗れる
```

---

## 10. Annotation: 付加情報（ただし selector には使わない）

**Annotation** はオブジェクトに付随するメタデータですが、
**ラベルのように selector としては使いません**。

用途:

- サードパーティのエージェント/ツールが参照する情報
- 運用メモ（オーナー、チケットURL、設計情報など）

---

## まとめ（試験向けの覚え方）

- **Pod**: コンテナの実行単位。IP/Volumeなどを共有するまとまり
- **Namespace**: 分離の境界（マルチテナント/整理）。スコープに注意
- **Controller**: Desired と Current を一致させ続ける監視ループ
- **Deployment → ReplicaSet → Pod**: 重要な管理チェーン
- **Service**: ラベルで Pod を束ね、安定した到達先を提供
- **Job/CronJob**: バッチ用
- **Label**: selector に使える。大量管理の主役
- **Annotation**: 付加情報。selector には使わない

