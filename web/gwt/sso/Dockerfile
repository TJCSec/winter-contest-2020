FROM python:3.8-slim-buster

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    apt-get purge -y libpq-dev build-essential

COPY . .

CMD [ "gunicorn", "--worker-tmp-dir=/dev/shm", "--bind=0.0.0.0:3000", "--log-file=-", "--workers=2", "--threads=4", "--worker-class=gthread", "wsgi:app"]
