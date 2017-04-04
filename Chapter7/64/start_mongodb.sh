#!/bin/sh

is_running=$(docker ps -aq --filter status=running --filter name=mongo)

if [[ "$is_running" ]]; then
    echo "Already running"
    exit
fi

is_exist=$(docker ps -aq --filter name=mongo)

if [[ "$is_exist" ]]; then
  docker start $is_exist
else
  docker run -d -p 27017:27017 --name mongo mongo
fi

