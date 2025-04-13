#!/bin/bash


echo "Ожидаем, пока база будет доступна"
while ! nc -z db 5432; do sleep 0.1; done
echo "БД доступна"

alembic upgrade head

exec "$@"
