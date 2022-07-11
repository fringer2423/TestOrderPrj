#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

chmod 644 scripts/creds.json

python scripts/first_script.py
python scripts/get_current_curs.py &
python scripts/get_data_from_table.py &


exec "$@"
