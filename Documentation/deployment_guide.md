
# Deployment Guide

## Deployment Options

### Docker

1. Build the Docker image:
   ```bash
   docker build -t hycan .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 hycan
   ```

### Kubernetes

1. Use the provided `deployment.yaml` file to deploy on a Kubernetes cluster:
   ```bash
   kubectl apply -f deployment.yaml
   ```

2. Verify the service is running:
   ```bash
   kubectl get services
   ```

### Cloud Hosting

- Recommended platforms: AWS, Google Cloud, Azure.
- Use the `docker-compose.yml` file for scalable deployment.

