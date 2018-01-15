#!/bin/bash

cat <<EOT > /etc/supervisord.conf
[supervisord]
nodaemon=true


[program:app]
directory=/usr/src/app/api/haha_respond
command=gunicorn -k gevent --max-requests 3000 --access-logfile - --error-logfile - -b 0.0.0.0:8000 haha_respond.haha_respond.wsgi:application --threads 4
autorestart=true
startsecs=0
startretries=25
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

[program:stream]
directory=/usr/src/app/stream
command=python haha_stream.py
autorestart=true
startsecs=0
startretries=25
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

[program:nginx]
directory=/usr/src/app
command=nginx -g 'daemon off;'
autorestart=true
startsecs=0
startretries=15
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
EOT

exec /usr/bin/supervisord
