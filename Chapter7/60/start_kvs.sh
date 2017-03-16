#!/bin/sh

ids=$(docker ps -q --filter name=redis)

if [[ "$ids" ]]; then
    echo Already exists
    exit
fi

docker run -p 6379:6379 -v data:/data --name redis -d redis redis-server --appendonly yes
