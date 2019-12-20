nohup uwsgi --wsgi-file /src/auth.py --socket :3031 --buffer-size 32768 &
nginx -g "daemon off;"