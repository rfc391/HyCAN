
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

# Expose port for gRPC server
EXPOSE 50051

# Command to run the gRPC server
CMD ["python", "catalyst_service.py"]
