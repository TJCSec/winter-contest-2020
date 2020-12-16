FROM python:3.8-slim-buster

RUN pip3 install Flask gunicorn

WORKDIR /home/app
ADD ./web/ /home/app/
RUN chmod -R ugo-w /home/app

RUN python3 /home/app/database.py

CMD /usr/local/bin/gunicorn -b 0.0.0.0:5000 -w 4 application:app

