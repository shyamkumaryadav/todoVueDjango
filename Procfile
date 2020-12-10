release: echo '***********release************' && python manage.py collectstatic --noinput && python manage.py makemigrations todos && python manage.py migrate && echo '***********release************'
web: gunicorn django_proj.wsgi
