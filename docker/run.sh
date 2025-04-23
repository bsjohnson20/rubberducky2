#!/bin/bash

# To be ran from docker directory NOT inside container

# Copy server
rm -rf docker_server
cp ../build_server ./docker_server -r
cp ../build_server/payloads . -r
mkdir files

# Generate dockerfile
docker build -t rubbyducky:latest . #--no-cache


# Copy payloads

# Run docker
docker compose up -d
docker compose down
docker compose up -d
