FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="devopsapp.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./headers.conf /etc/nginx/headers.conf
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=django
ENV APP_PORT=8001

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]