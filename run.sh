#!/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Stop and remove existing containers if they exist
docker rm -f mysql-container python-app 2>/dev/null

# Run the MySQL container and mount the initialization SQL script
docker run --name mysql-container \
    -e MYSQL_ROOT_PASSWORD=$MYSQL_PASSWORD \
    -e MYSQL_DATABASE=$MYSQL_DATABASE \
    -p 3307:3306 \
    -v "$(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql" \
    -v mysql_data:/var/lib/mysql \
    -d mysql:latest

# Wait for a few seconds to ensure MySQL is ready
sleep 10

# Build the Python application Docker image
docker build -t python-app .

# Run the Python application container
docker run --name python-app --link mysql-container:mysql \
    --env-file .env \
    python-app
