#!/bin/bash

docker-compose up

docker-compose exec kafka \
   kafka-topics  \
     --create \
     --topic events \
     --partitions 1 \
     --replication-factor 1 \
     --if-not-exists --zookeeper zookeeper:32181

docker-compose exec mids \
    env FLASK_APP=/w205/w205-project3/game_api_v2.py \
    flask run --host 0.0.0.0
