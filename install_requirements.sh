#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker could not be found. Please install Docker first."
    exit
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "All dependencies installed successfully!"

