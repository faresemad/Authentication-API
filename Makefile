COMPOSE_FILE = docker-compose.yml


upbuild:
	docker-compose -f $(COMPOSE_FILE) up --build

up:
	docker-compose -f $(COMPOSE_FILE) up

up-detached:
	docker-compose -f $(COMPOSE_FILE) up -d

build:
	docker-compose -f $(COMPOSE_FILE) build

rebuild:
	docker-compose -f $(COMPOSE_FILE) up --build --force-recreate

restart:
	docker-compose -f $(COMPOSE_FILE) restart

down:
	docker-compose -f $(COMPOSE_FILE) down

stop:
	docker-compose -f $(COMPOSE_FILE) stop

logs:
	docker-compose -f $(COMPOSE_FILE) logs $(filter-out $@,$(MAKECMDGOALS))

makemigrations:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py makemigrations

migrate:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

flush:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py flush

createsuperuser:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py createsuperuser

startapp:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

collectstatic:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py collectstatic

command:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py $(filter-out $@,$(MAKECMDGOALS))

swagger:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py spectacular --file schema.yaml --validate --fail-on-warn

get-backup:
	docker-compose -f $(COMPOSE_FILE) exec db pg_dump -U postgres -d postgres > backup.sql

set-backup:
	docker-compose -f $(COMPOSE_FILE) exec db psql -U postgres -d postgres < backup.sql

get-media-files:
	docker cp $(shell docker-compose -f $(COMPOSE_FILE) ps -q django):/app/media/ .
