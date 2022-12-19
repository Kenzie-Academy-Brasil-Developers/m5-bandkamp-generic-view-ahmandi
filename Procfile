web: python manage.py collectstatic --noinput \
    && python manage.py migrate \
    && gunicorn bandkamp.wsgi --log-level debug