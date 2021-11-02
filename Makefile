.PHONY: run
run:
	@poetry run python artisanbackend/manage.py runserver

.PHONY: lint_backend
lint_backend:
	@poetry run pylint artisanbackend/*

.PHONY: test_backend
test_backend:
	@echo "Testing backoffice"
	@poetry run python artisanbackend/manage.py test backoffice
	@echo "Testing store"
	@poetry run python artisanbackend/manage.py test store

.PHONY: test
test: test_backend

.PHONY: lint
lint: lint_backend
