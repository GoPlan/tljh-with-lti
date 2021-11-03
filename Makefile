setup:
	git submodule update --init --recursive 

build: setup
	docker-compose build

down:
	docker-compose down

up:
	docker-compose up --detach

rm-container:
	docker-compose stop
	docker-compose rm

rm-image:
	docker image rm tljh-with-lti

shell:
	docker exec -it tljh-dev /bin/bash

firstrun:
	docker exec -it tljh-dev python3 /srv/src/bootstrap/bootstrap.py --admin admin:password


