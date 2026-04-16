# ---------- Stage 1: Build ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

# Create non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

WORKDIR /app

# Copy only installed dependencies
COPY --from=builder /install /usr/local

# Copy app code
COPY app ./app

# Copy test code
COPY tests ./tests

# Add python path
ENV PYTHONPATH=/app

# Set ownership
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]