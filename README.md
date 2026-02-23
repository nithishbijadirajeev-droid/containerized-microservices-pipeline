# CI/CD and Containerized Deployment Pattern

Production-grade multi-container microservices deployment using Docker, Docker Compose, GitHub Actions, and AWS.

## Overview

This project implements a real-world containerized microservices deployment pattern with automated CI/CD pipeline. Three independent services communicate over a Docker network, each containerized separately and orchestrated using Docker Compose.

## Architecture
```
GitHub Push
      |
GitHub Actions CI/CD Pipeline
      |
Build and Test All Services
      |
Docker Compose Orchestration
      |
--------------------------------
|            |                 |
Frontend   API Gateway    Database
(Nginx)   (Python Flask) (PostgreSQL)
Port 80    Port 5000      Port 5432
--------------------------------
      |
All services communicate over
microservices-network
```

## Services

| Service | Technology | Port | Description |
|---------|-----------|------|-------------|
| Frontend | Nginx | 80 | Dashboard UI |
| API Gateway | Python Flask | 5000 | REST API |
| Database | PostgreSQL | 5432 | Data persistence |

## Tech Stack

- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Frontend:** Nginx
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Cloud:** AWS EC2
- **OS:** Linux Ubuntu

## Setup and Usage

### Run Locally
```bash
git clone https://github.com/nithishbijadirajeev-droid/containerized-microservices-pipeline.git
cd containerized-microservices-pipeline
docker-compose up --build
```

Visit:
- Frontend: http://localhost:80
- API Gateway: http://localhost:5000
- Services API: http://localhost:5000/api/services

### Monitor Container Logs
```bash
docker-compose logs -f
docker-compose ps
docker stats
```

### Stop Services
```bash
docker-compose down
```
