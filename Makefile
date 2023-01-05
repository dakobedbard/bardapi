DOCKER_COMPOSE_FILE?=docker-compose.yaml

COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE)
APPDOCKER=$(COMPOSE) run --rm app
DAKOBED_TAG=latest


all: build web

build:
	$(COMPOSE) build

shell: services
	$(APPDOCKER) /bin/bash

web: services
	$(COMPOSE) up api

migrate:
	$(APPDOCKER) bard db upgrade
	$(APPDOCKER) bard db  migrate

services:
	$(COMPOSE) up -d --remove-orphans \
		$(SERVICES_CONTAINERS)

test:
	$(APPDOCKER) contrib/test.sh

prune:
	docker-compose down --remove-orphans
	docker system prune -f
	docker volume prune -f