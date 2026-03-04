#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started"
fi

python3 -c "
from app.main import app, db
with app.app_context():
    db.create_all()
"

exec "$@"
