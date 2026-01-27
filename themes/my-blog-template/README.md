# Microsoft Security inspired Pelican theme

This custom theme recreates the clean grid-first design language from the [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/). It provides a responsive experience with an Azure Blue palette, flexible card grid, and focused article layout.

## Highlights

- 1200px centered content column with responsive grid (3/2/1 columns)
- Sticky, minimalist header with opinionated primary links
- Hero section optimized for short taglines and CTAs
- Category spotlight rows with hover-elevated cards
- Article template featuring wide hero, readable body width, pill tags, and share links
- Accessible typography defaults using `Segoe UI` fallback stack
- Syntax-friendly code block treatment for technical content

## Structure

```
themes/my-blog-template/
├── README.md
├── theme.conf
├── static/
│   └── css/
│       └── security.css
└── templates/
    ├── article.html
    ├── archives.html
    ├── author.html
    ├── authors.html
    ├── base.html
    ├── categories.html
    ├── category.html
    ├── index.html
    ├── page.html
    ├── tag.html
    ├── tags.html
    └── partials/
        └── post-card.html
```

## Usage

1. Install Pelican dependencies (`pip install -r requirements.txt`).
2. Point `pelicanconf.py` (and `publishconf.py`) at the theme:
   ```python
   THEME = 'themes/my-blog-template'
   ```
3. (Optional) Customize hero copy or footer text in `pelicanconf.py`:
   ```python
   HERO_INTRO = 'Your custom intro sentence.'
   FOOTER_TEXT = 'Add a legal notice or mission statement here.'
   COPYRIGHT_YEAR = '2025'
   ```
4. Run `pelican content` and view with `pelican --listen` or your preferred workflow.

## Customization tips

- **Navigation**: `MENUITEMS` entries are appended after the default Home/Categories/Archives/About links.
- **Hero tagline**: Set `SITESUBTITLE`, `SITEDESCRIPTION`, or `HERO_INTRO` for the landing hero text.
- **Category spotlight**: The index page automatically surfaces up to three categories and their three most recent posts.
- **Syntax highlighting**: Update `pygments_style` in Pelican settings if you need a different palette; code blocks use the neutral container styles provided in `security.css`.

Feel free to adapt the CSS variables in `static/css/security.css` to match additional brand requirements.
