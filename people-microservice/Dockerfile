FROM python:alpine@sha256:452682e4648deafe431ad2f2391d726d7c52f0ff291be8bd4074b10379bb89ff AS builder

ENV \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev postgresql-dev

COPY requirements.txt .
RUN mkdir -p /wheels && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:alpine@sha256:452682e4648deafe431ad2f2391d726d7c52f0ff291be8bd4074b10379bb89ff

ENV \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apk add --no-cache libffi openssl postgresql-libs postgresql-client

RUN addgroup -S appgroup \
    && adduser -S -G appgroup -h /app appuser

WORKDIR /app

# Copy wheels and requirements
COPY --from=builder /wheels /wheels
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt \
    && rm -rf /wheels

COPY . /app

RUN chmod +x /app/wait-for-postgres.sh && chown -R appuser:appgroup /app

USER appuser

CMD ["sh", "wait-for-postgres.sh", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
