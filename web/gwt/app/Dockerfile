FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "--worker-tmp-dir=/dev/shm", "--bind=0.0.0.0:3000", "--log-file=-", "--workers=2", "--threads=4", "--worker-class=gthread", "app:app"]
