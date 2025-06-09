#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."

until mysql -h"$DB_HOST" -P"$DB_PORT" -u"$DB_USER" -p"$DB_PASS" -e "SELECT 1;" >/dev/null 2>&1; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 2
done

echo "MySQL is up - starting the app"
exec node app.js
