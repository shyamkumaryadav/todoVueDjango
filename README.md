# todovuedjango

## Project setup
```bash
npm install
pipenv install
```

### IMP
```bash
pipenv run ./manage.py makemigrations todos # App Name required
pipenv run ./manage.py migrate  
# Create Super User for /admin/
# pipenv run ./manage.py createsuperuser 
# --username admin --email testvue@django.org 
pipenv run ./manage.py collectstatic 
```

### Compiles and minifies for production
```bash
npm run build
```

### hot-reloads for development
```bash
pipenv run ./manage.py runserver 0.0.0.0:8000
```

### auto build on heroku
[Heroku vuetododjango](https://todovuedjango.herokuapp.com/)