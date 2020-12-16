FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y xinetd && \
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY server.py ginkoid.png flag.txt ./

CMD ["xinetd", "-dontfork"]
