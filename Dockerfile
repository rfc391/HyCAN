FROM python:3.9-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y python3-distutils gcc

WORKDIR /app

# Copy requirements and install them
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Set the command to run the application
CMD ["python", "src/app.py"]
