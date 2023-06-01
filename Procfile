release: python manage.py migrate && python manage.py createdummyusers
web: python manage.py collectstatic --noinput && gunicorn config.wsgi --log-file -
worker: celery -A config worker -l info -B