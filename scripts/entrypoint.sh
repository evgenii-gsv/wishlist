#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python -m wishlist.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run gunicorn wishlist.project.wsgi:application -p 8000 -b 0.0.0.0 -w 3
