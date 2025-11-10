FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    tini ca-certificates && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser
WORKDIR /app

# Copy dependency files first (for build caching)
COPY --chown=appuser:appuser pyproject.toml /app/
# If you use requirements.txt instead, change the line above accordingly

RUN python -m pip install --upgrade pip build && \
    python -m pip install --no-cache-dir .

# Copy application code
COPY --chown=appuser:appuser . /app

# Disable .pyc and buffer
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/bin/tini", "--"]

# Default command – adjust to your entry point
CMD ["python", "main.py"]
