SHELL=/bin/bash
DOCKER_COMPOSE=docker-compose.yml
SUDO=sudo
CONTAINER_NAME=partner_delivery

install: build start
	make exec COMMAND="python initial_data.py"

build:
	docker-compose -f $(DOCKER_COMPOSE) build --force-rm --no-cache ${CONTAINER_NAME}

start: 
	docker-compose -f $(DOCKER_COMPOSE) up -d

stop:
	docker-compose -f $(DOCKER_COMPOSE) down; true

exec:
	docker-compose -f $(DOCKER_COMPOSE) exec -T ${CONTAINER_NAME} $(COMMAND)

install-requirements:
	pip install -r requirements.txt

pep8:
	make exec COMMAND="flake8 . --exit-zero"

test: setup_test
	make exec COMMAND="pytest --cov=. --cov-config .coveragerc --cov-report xml"

formatter:
	make exec COMMAND="black . -S -v -t py38 --exclude '\alembic/ .venv/' -l 100 "
	make pep8

migrate:
	make exec COMMAND="alembic upgrade heads"

setup_test: start
	make exec CONTAINER_NAME="service.postgres" COMMAND='psql -U tom -d postgres -c "DROP DATABASE IF EXISTS cashback_postgres_test;"'
	make exec CONTAINER_NAME="service.postgres" COMMAND="psql -U tom -d postgres -c 'CREATE DATABASE  cashback_postgres_test;'"
	make exec  COMMAND="alembic --name tests upgrade heads"

coverage: test
	make exec COMMAND="apt install curl -y"
	bash <(curl -Ls https://coverage.codacy.com/get.sh) report -r coverage.xml