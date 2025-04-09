#!/bin/bash

#!/bin/bash

echo "Starting AI-Driven Build, Test, and Deployment..."

# Step 1: Install Dependencies
echo "Installing dependencies..."
pip install -r requirements_optimized.txt

# Step 2: Verify OpenCV Installation
echo "Verifying OpenCV installation..."
python -c "import cv2; print(f'OpenCV version: {cv2.__version__}')"

# Step 3: Lint the Code
echo "Running code linting..."
flake8 .

# Step 4: Format the Code
echo "Formatting code..."
black .

# Step 5: Run Security Checks
echo "Running security checks..."
bandit -r .

# Step 6: Run Tests
echo "Running tests..."
pytest --maxfail=5 --disable-warnings

# Step 7: Deployment Simulation
echo "Packaging project for deployment..."
zip -r project_deployment.zip *

echo "Build, Test, and Deployment completed successfully."
