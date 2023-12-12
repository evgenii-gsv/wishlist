.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m wishlist.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m wishlist.manage makemigrations

.PHONY: run-dependencies
run-dependencies:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: runserver
runserver:
	poetry run python -m wishlist.manage runserver

.PHONY: shell
shell:
	poetry run python -m wishlist.manage shell

.PHONY: superuser
superuser:
	poetry run python -m wishlist.manage createsuperuser

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: test-detailed
test-detailed:
	poetry run pytest -vv -rs -s

.PHONY: update
update: install migrate install-pre-commit ;
