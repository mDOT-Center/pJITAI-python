#!/bin/sh

if [ "$BOILERPLATE_ENV" = "prod" ]; then
  echo "Waiting for mysql..."

  while ! nc -z "$MYSQL_HOST" 3306; do
    sleep 0.1
  done

  echo "MySQL started"
fi
