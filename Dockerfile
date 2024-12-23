
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Dash app
EXPOSE 8050

# Run the interactive dashboard script
CMD ["python", "src/visualizations/interactive_dashboard.py"]
