FROM python:3-slim

WORKDIR /
ENV SUCCESS_RATE=80 \
    FLASK_APP=app.py
STOPSIGNAL SIGINT
CMD ["python", "/app.py"]
RUN pip install flask prometheus_client flask_prometheus
COPY app.py /app.py
