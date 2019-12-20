nohup uwsgi --wsgi-file /src/auth.py --socket :3031 &
nginx -g "daemon off;"