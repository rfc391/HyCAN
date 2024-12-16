# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
