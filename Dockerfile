FROM nginx

RUN apt update -y; \
    apt install -y python3-pip; \
    pip3 install uwsgi pyjwt;

COPY content /content
COPY nginx.conf /etc/nginx/nginx.conf
COPY auth.py /src/auth.py
COPY uwsgi.conf /etc/init/uwsgi.conf
COPY go.sh /src/go.sh

ENTRYPOINT ["sh", "/src/go.sh"]