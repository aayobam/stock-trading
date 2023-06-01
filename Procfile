release: python manage.py migrate && python manage.py createdummyusers && celery -A config worker -l info -B
web: python manage.py collectstatic --noinput && gunicorn config.wsgi --log-file -