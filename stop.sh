#!/bin/bash

# Stop the running containers
docker stop mysql-container python-app

# Remove the containers
docker rm mysql-container python-app

# Remove the Docker image for the Python application
docker rmi python-app

# Optional: Remove dangling images to free up space
docker image prune -f

echo "Containers and images have been removed."

