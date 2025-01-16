
# HyCAN User Documentation

## Overview
HyCAN is a modular framework designed for optimizing hydrogen production and nanomaterial synthesis. This document provides a comprehensive guide to deploying, configuring, and using HyCAN.

## Setup
### Prerequisites
- Docker and Docker Compose installed.
- Python 3.9 or higher.
- Access to IPFS and PostgreSQL instances.

### Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/rfc391/HyCAN.git
   cd HyCAN
   ```
2. Build and deploy the Catalyst Service:
   ```bash
   cd services
   docker build -t catalyst_service .
   docker run -p 50051:50051 catalyst_service
   ```

## Configuration
### PostgreSQL
- Update `config/postgres_config.ini` with your database credentials.
- Ensure the database is running and accessible.

### Cloudflare D1
- Update `config/cloudflare_d1_config.ini` with your Cloudflare account details.

### IPFS
- Ensure the IPFS node is running locally or remotely.
- Update `config/ipfs_config.ini` with the IPFS API URL.

## Usage
1. Access the Catalyst Service via gRPC on port `50051`.
2. Use provided gRPC clients or tools like `grpcurl` to interact with the service.

## AI Integration
- Place a pre-trained model file (`model.pkl`) in the `services` directory for AI-based predictions.
- The model should accept input as a list of parameters and return efficiency as output.

## ISO 9001 Compliance
HyCAN adheres to ISO 9001 standards by documenting workflows, ensuring traceability, and following quality management principles.

## Troubleshooting
- Verify all services are running using `docker ps`.
- Check logs for errors: `docker logs <container_id>`.

