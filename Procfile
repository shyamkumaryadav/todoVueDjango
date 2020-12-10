release: python manage.py collectstatic --noinput && python manage.py makemigrations todos && python manage.py migrate
web: gunicorn django_proj.wsgi
