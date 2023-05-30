release: export DJANGO_SETTINGS_MODULE=config.settings.production
web: python manage.py migrate && gunicorn config.wsgi --log-file -