FROM ubuntu:20.04 


ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt ./


RUN set -ex \
    && apt update \
    && apt upgrade -y \
    && apt-get install -y --no-install-recommends python3-pip\
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove --allow-remove-essential \
    && rm -rf /var/lib/apt/lists/* /var/log/* /usr/share/man /usr/share/doc

COPY . /app
RUN mkdir /data

CMD ["python3","main.py"]
