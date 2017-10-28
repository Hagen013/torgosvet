#!/bin/bash
set -e
cmd="$@"


function redis_ready(){
python3 << END
import redis
import sys
rs = redis.Redis('redis')
try:
    response = rs.client_list()
    print('redis connection')
except redis.ConnectionError:
    print('redis connection refused')
    sys.exit(-1)
sys.exit(0)
END
}

function rabbit_ready(){
python3 << END
from kombu import Connection
import sys
rabbit_url = 'amqp://8800:8800pass@rabbit/8800vh'
conn = Connection(rabbit_url)
try:
    conn.connect()
    print('rabbit connection')
except:
    print('rabbit connection refused')
    sys.exit(-1)
sys.exit(0)
END
}

until redis_ready; do
  >&2 echo "Redis is unavailable - sleeping"
  sleep 1
done

>&2 echo "Redis is up - continuing..."

until rabbit_ready; do
  >&2 echo "Rabbit is unavailable - sleeping"
  sleep 1
done

>&2 echo "Rabbit is up - continuing..."

>&2 cd web/backend
>&2 celery -A config flower --url_prefix=$FLOWER_URL_PREFIX --basic_auth=$FLOWER_ADMIN:$FLOWER_PASSWORD


exec $cmd