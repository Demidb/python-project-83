[tool.poetry]
name = "hexlet-code"
version = "0.1.0"
description = "Study project No. 3 'Page Analyzer'"
authors = ["Demid <LLiker1337@gmail.com>"]
readme = "README.md"
repository = "https://github.com/Demidb/python-project-83"

packages = [{include = "page_analyzer"}]

[tool.poetry.dependencies]
python = "^3.10"
flask = "^2.2.3"
gunicorn = "^20.1.0"
python-dotenv = "^1.0.0"
psycopg2-binary = "^2.9.6"
validators = "^0.20.0"
requests = "^2.29.0"
beautifulsoup4 = "^4.12.2"
responses = "^0.23.1"

[tool.poetry.group.dev.dependencies]
flake8 = "^6.0.0"
pytest = "^7.3.1"
pytest-cov = "^4.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"