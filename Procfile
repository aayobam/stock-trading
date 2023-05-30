#release: python manage.py createdummyusers
#release: celery -A config worker -l info -B

export DJANGO_SETTINGS_MODULE=config.settings.production
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 config.wsgi --log-file -