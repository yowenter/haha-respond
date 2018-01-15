FROM python:2.7-alpine


MAINTAINER TAOG

RUN apk add --update \
  ca-certificates gcc musl-dev nginx supervisor \
  && rm -rf /var/cache/apk/* \
  && pip install gunicorn newrelic


ENV LANG en_US.utf8

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/haha.conf /etc/nginx/conf.d/haha.conf

COPY webui/dist/        /usr/share/nginx/html/

RUN mkdir -p /usr/src/app

COPY api/requirements.txt  /usr/src/app/
COPY api/requirements-doc.txt /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements-doc.txt


ADD . /usr/src/app

RUN chmod +x /usr/src/app/supervisord.sh

CMD ["sh", "/usr/src/app/supervisord.sh"]






