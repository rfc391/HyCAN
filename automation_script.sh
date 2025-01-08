
#!/bin/bash

echo "Starting AI-Driven Build, Test, and Deployment..."

# Step 1: Install Dependencies
echo "Installing dependencies..."
pip install -r requirements_updated.txt

# Step 2: Lint the Code
echo "Running code linting..."
flake8 .

# Step 3: Format the Code
echo "Formatting code..."
black .

# Step 4: Run Tests
echo "Running tests..."
pytest --maxfail=5 --disable-warnings

# Step 5: Deployment Simulation
echo "Packaging project for deployment..."
zip -r project_deployment.zip *

echo "Build, test, and deployment process completed successfully."
