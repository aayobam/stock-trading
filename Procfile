release: export DJANGO_SETTINGS_MODULE=config.settings.production
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi --log-file -