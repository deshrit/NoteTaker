# gunicorn configuration

accesslog = '-'
errorlog = '-'
loglevel = 'info'
workers = 4
threads = 6
bind = '0.0.0.0:8000'