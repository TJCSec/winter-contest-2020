FROM ubuntu:19.04

RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list && \
    apt-get update -y && apt-get install -y --no-install-recommends \
    xinetd && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /home/ctf

RUN mkdir -p /home/ctf/lib && \
    cp -R /usr/lib/x86_64-linux-gnu /home/ctf/lib/x86_64-linux-gnu && \
    cp -R /usr/lib64 /home/ctf/lib64

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /bin/ls /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./bin/ /home/ctf/
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag.txt

CMD ["/start.sh"]

EXPOSE 9999
