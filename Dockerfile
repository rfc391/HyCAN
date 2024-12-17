FROM python:3.13-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y python3-distutils gcc

# Copy requirements and install them
COPY requirements.txt .
pip install -r requirements.txt

# Copy application code
COPY . .

# Set the command to run the application
CMD ["python", "src/app.py"]
