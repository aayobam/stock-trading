#!/bin/bash

set -o errexit  # exit on error

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsu
python manage.py createdummyusers
celery -A config worker -l info -B