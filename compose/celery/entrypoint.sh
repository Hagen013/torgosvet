#!/bin/bash
set -e
cmd="$@"

function postgres_ready(){
python3 << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname='$POSTGRES_DATABASE', user='$POSTGRES_USER', password='$POSTGRES_PASSWORD', host='$POSTGRES_HOST')
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
>&2 cd web/backend

>&2 celery -A config worker -l info -E -B

exec $cmd
