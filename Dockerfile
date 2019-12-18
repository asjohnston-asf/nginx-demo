FROM nginx

COPY content /content
COPY nginx.conf /etc/nginx/nginx.conf
