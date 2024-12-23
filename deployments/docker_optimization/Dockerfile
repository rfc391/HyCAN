
"""
Optimized Dockerfile
"""
# Stage 1: Build
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Image
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app /app
COPY . .
CMD ["python", "main.py"]
