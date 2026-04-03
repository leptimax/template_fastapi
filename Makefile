COMPOSE=docker compose -f

PRODUCTION=prod.docker-compose.yml
DEVELOPMENT=deployment/docker-compose.yml

build:
	bash ./scripts/build.sh
	$(COMPOSE) $(DEVELOPMENT) build --build-arg "ARTIFACT_PATH=./_build"

up:
	$(COMPOSE) $(DEVELOPMENT) up -d

down:
	$(COMPOSE) $(DEVELOPMENT) down --remove-orphans

logs:
	$(COMPOSE) $(DEVELOPMENT) logs -f

.PHONY: build, up, down, logs, migration
