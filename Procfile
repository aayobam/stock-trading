release: export DJANGO_SETTINGS_MODULE=config.settings.production
release: python manage.py migrate
release: python manage.py collectstatic --noinput
release: python manage.py createdummyusers
#release: celery -A config worker -l info -B
web: gunicorn config.wsgi --log-file -