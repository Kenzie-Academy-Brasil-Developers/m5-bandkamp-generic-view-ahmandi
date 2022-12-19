web: python manage.py collectstatic --noinput \
    && python manage.py migrate \
    && gunicorn _core.wsgi --log-level debug