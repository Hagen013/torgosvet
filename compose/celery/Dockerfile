FROM alpine:latest
RUN apk update

COPY  web/requirements/base.txt base.txt
COPY  web/requirements/production.txt requirements.txt
COPY  compose/celery/entrypoint.sh entrypoint.sh
ENV LD_LIBRARY_PATH=/lib:/usr/lib

# INSTALL PYTHON3, psycopg2, and libs for pip requirements
RUN apk add --no-cache \
    python3 \
    py3-psycopg2 \
    libpq \
    zlib-dev \
    jpeg-dev \
    musl-dev \
    python3-dev \
    ca-certificates


# INSTALL requirements
RUN apk add --no-cache gcc && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del gcc

RUN apk add --no-cache uwsgi uwsgi-python3 uwsgi-python uwsgi-http uwsgi-corerouter uwsgi-stats_pusher_socket


# Install bash
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY  web /web
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8001

ENTRYPOINT ["/entrypoint.sh"]