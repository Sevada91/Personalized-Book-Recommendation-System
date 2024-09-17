#!/bin/bash

# Check if the MySQL container is running
if [ $(docker ps -q -f name=mysql-container) ]; then
  # Run the MySQL client within the container
  docker exec -it mysql-container mysql -u root -p$MYSQL_PASSWORD -D $MYSQL_DATABASE -e "$1"
else
  echo "MySQL container is not running."
fi

