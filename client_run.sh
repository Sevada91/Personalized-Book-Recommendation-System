#!/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Build the Python application Docker image if not already built
docker build -t python-app .

# Run the Python application container to execute the client script
docker run --name python-client --link mysql-container:mysql \
    --env-file .env \
    python-app python test_client.py

# Remove the container after running the client script
docker rm python-client

