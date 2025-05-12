#!/bin/bash

# Espera o PostgreSQL estar aceitando conexões
echo "Aguardando o PostgreSQL iniciar em $POSTGRES_HOST:$POSTGRES_PORT..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT"; do
  sleep 2
done

echo "PostgreSQL está pronto. Iniciando o serviço..."
exec "$@"
