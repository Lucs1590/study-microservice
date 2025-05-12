#!/bin/bash

echo "Esperando o PostgreSQL estar disponível em $POSTGRES_HOST:$POSTGRES_PORT..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT"; do
  sleep 2
done

echo "PostgreSQL disponível. Iniciando o serviço..."

exec "$@"
