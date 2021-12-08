migrate: bash python manage.py migrate
collectstatic: heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn ngerti_in.wsgi