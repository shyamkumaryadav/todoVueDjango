npm ci
npm run postpublish
python manage.py makemigrations todos
python manage.py migrate