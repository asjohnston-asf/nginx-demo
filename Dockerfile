FROM nginx

RUN apt update -y; \
    apt install -y python3-pip; \
    pip3 install uwsgi pyjwt;

COPY content /content
COPY nginx /etc/nginx
COPY src /src

ENTRYPOINT ["sh", "/src/go.sh"]