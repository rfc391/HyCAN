import subprocess
import requests
import time

def run_docker_compose():
    try:
        # Step 1: Build Docker images
        print("Building Docker images...")
        subprocess.run(["docker-compose", "build"], check=True)

        # Step 2: Start Docker containers
        print("Starting Docker containers...")
        subprocess.run(["docker-compose", "up", "-d"], check=True)

        # Step 3: Wait for the app to be ready
        print("Waiting for the application to start...")
        time.sleep(10)  # Adjust based on app startup time

        # Step 4: Test the app endpoint
        print("Testing the application endpoint...")
        response = requests.get("http://localhost:8050")
        if response.status_code == 200:
            print("Application is running successfully!")
        else:
            print(f"Application returned an unexpected status: {response.status_code}")

    except subprocess.CalledProcessError as e:
        print(f"Docker Compose command failed: {e}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request to the application failed: {e}")
    finally:
        # Step 5: Tear down Docker containers
        print("Stopping Docker containers...")
        subprocess.run(["docker-compose", "down"], check=False)

if __name__ == "__main__":
    run_docker_compose()
