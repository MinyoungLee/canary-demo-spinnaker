#!/usr/bin/env python

from random import randrange
from flask import Flask
from prometheus_client import start_http_server, Gauge, Counter
import os

app = Flask('kayenta-tester')
c = Counter('requests', 'Number of requests served, by http code', ['http_code'])
g = Gauge('rate_requests', 'Rate of success requests')
responce_500 = 0
responce_200 = 0
rate_responce = 0
@app.route('/')
def hello():
    global responce_500
    global responce_200
    global rate_responce
    if randrange(1, 100) > int(os.environ['SUCCESS_RATE']):
        c.labels(http_code='500').inc()
        responce_500 = responce_500 + 1
        rate_responce = responce_500 / (responce_500+responce_200) * 100
        g.set(rate_responce)
        return "Internal Server Error\n", 500
    else:
        c.labels(http_code = '200').inc()
        responce_200 = responce_200 + 1
        rate_responce = responce_500 / (responce_500+responce_200) * 100
        g.set(rate_responce)
        return "Hello World!\n"

#cc = rate_counter('requests_rate', 'Number of requests rate served, by http code', ['rate_counter'])

start_http_server(8000)
app.run(host = '0.0.0.0', port = 8080)
