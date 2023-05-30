release: export DJANGO_SETTINGS_MODULE=config.settings.production
release: python manage.py collectstatic --noinput
web: python manage.py migrate && gunicorn config.wsgi --log-file -