# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN python -m pip install --upgrade pip

# Copy the application code to the container
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
