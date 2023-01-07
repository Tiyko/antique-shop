web: gunicorn shop_main.wsgi:application --log-file - --log-level debug
python manage.py collectstatic
manage.py migrate