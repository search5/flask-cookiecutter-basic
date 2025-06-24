from pathlib import Path

project_name = '{{ cookiecutter.project_name }}'

static_dir = "src" / Path(project_name) / "static"
templates_dir = "src" / Path(project_name) / "templates"

for item in (static_dir, templates_dir):
    item.mkdir()
