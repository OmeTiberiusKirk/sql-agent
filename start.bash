#!/bin/bash

volumes=$(docker volume ls)
if [[ "$volumes" != *"sql-agent"* ]]; then
    docker volume create sql-agent;
fi

docker run -d \
--name sql-agent \
-e POSTGRES_DB=ai_agent \
-e POSTGRES_PASSWORD=password \
-e PGDATA=/var/lib/postgresql/data/pgdata \
-v sql-agent:/var/lib/postgresql/data \
-v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
-p 5432:5432 \
postgres:17
