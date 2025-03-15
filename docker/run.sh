#!/bin/bash

# To be ran from docker directory NOT inside container

# Copy server
rm -rf docker_server
cp ../build_server ./docker_server -r

# Generate dockerfile
docker build -t rubbyducky:latest .


# Copy payloads

# Run docker
docker compose up -d

cp ../build_server/payloads . -r