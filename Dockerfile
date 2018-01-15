FROM python:2.7-alpine


MAINTAINER TAOG

RUN apk add --update alpine-sdk
RUN apk add --update \
  ca-certificates gcc musl-dev nginx supervisor \
  && rm -rf /var/cache/apk/* \
  && pip install gunicorn

RUN apk --update add py-mysqldb mariadb-dev linux-headers libc-dev python-dev


ENV LANG en_US.utf8

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/haha.conf /etc/nginx/conf.d/haha.conf



RUN mkdir -p /usr/src/app

COPY api/requirements.txt  /usr/src/app/
COPY api/requirements-doc.txt /usr/src/app/
COPY stream/requirements-stream.txt /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements-doc.txt
RUN pip install -r /usr/src/app/requirements-stream.txt




ADD . /usr/src/app




# make html doc
WORKDIR /usr/src/app/api-doc
#
RUN make html
#
COPY build/html /usr/share/nginx/html/api-doc

WORKDIR /usr/src/app

RUN chmod +x /usr/src/app/supervisord.sh

CMD ["sh", "/usr/src/app/supervisord.sh"]






