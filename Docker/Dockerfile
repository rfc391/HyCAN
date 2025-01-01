
# Multi-stage build for production
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Copy only necessary files for dependency installation
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Final lightweight image
FROM python:3.9-slim
WORKDIR /app

# Copy installed dependencies and source files
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app/

# Expose the port for the Dash app
EXPOSE 8050

# Run the interactive dashboard
CMD ["python", "src/visualizations/interactive_dashboard.py"]
