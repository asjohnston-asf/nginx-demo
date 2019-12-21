FROM nginx

RUN apt update -y; \
    apt install -y python3-pip; \
    pip3 install uwsgi pyjwt supervisor;

COPY content /content
COPY etc /etc

ENTRYPOINT ["/usr/local/bin/supervisord"]