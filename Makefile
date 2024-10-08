PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app --debug run

build:
	./build.sh

