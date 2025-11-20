PY?=python
PELICAN?=pelican
SETTINGS?=pelicanconf.py
PUBLISH_SETTINGS?=publishconf.py
CONTENT?=content
OUTPUT?=output

help:
	@echo "make html        -> build the site"
	@echo "make clean       -> remove generated files"
	@echo "make serve       -> serve output/ over HTTP"
	@echo "make devserver   -> auto-regenerating server"
	@echo "make publish     -> build using publishconf.py"

html:
	$(PELICAN) $(CONTENT) -o $(OUTPUT) -s $(SETTINGS)

clean:
	@if exist $(OUTPUT) rd /s /q $(OUTPUT)

serve:
	$(PELICAN) --listen -o $(OUTPUT) -s $(SETTINGS)

regenerate:
	$(PELICAN) --autoreload $(CONTENT) -o $(OUTPUT) -s $(SETTINGS)

devserver:
	$(PELICAN) --autoreload --listen $(CONTENT) -o $(OUTPUT) -s $(SETTINGS)

publish:
	$(PELICAN) $(CONTENT) -o $(OUTPUT) -s $(PUBLISH_SETTINGS)
