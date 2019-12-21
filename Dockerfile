FROM nginx

RUN apt update -y; \
    apt install -y python3-pip; \
    pip3 install uwsgi pyjwt supervisor;

COPY content /content
COPY nginx /etc/nginx
COPY src /src
COPY supervisord.conf /etc

ENTRYPOINT ["/usr/local/bin/supervisord"]