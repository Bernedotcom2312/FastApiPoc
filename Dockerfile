FROM python:3.14.3-alpine3.23 AS builder

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv && \
    uv sync --frozen --no-dev

FROM python:3.14.3-alpine3.23

COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN adduser -D -h /home/app -s /bin/sh app

USER app
WORKDIR /home/app

COPY --chown=app:app ./app ./app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
