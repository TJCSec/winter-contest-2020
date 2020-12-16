FROM python:3.8-alpine

ADD https://github.com/DarinMao/xinetd-musl/releases/download/xinetd-2-3-15/xinetd-musl /usr/local/sbin/xinetd
RUN chmod +x /usr/local/sbin/xinetd

FROM python:3.8-alpine

COPY --from=0 /usr/local/sbin/xinetd /usr/local/sbin/xinetd 

COPY xinetd.conf /etc/xinetd.conf

COPY server.py flag.txt mazemaker.py /

CMD ["xinetd", "-dontfork"]

EXPOSE 9999
