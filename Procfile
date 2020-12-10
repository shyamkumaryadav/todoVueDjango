release: npm ci && npm run build && python manage.py makemigrations todos && python manage.py migrate
web: gunicorn django_proj.wsgi
