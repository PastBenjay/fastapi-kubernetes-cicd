# FastAPI Kubernetes CI/CD Project

A cloud-native DevOps project demonstrating CI/CD workflows using FastAPI, Docker, Kubernetes, and Jenkins.

This project showcases how modern applications can be containerized, deployed, and managed through automated deployment pipelines and Kubernetes orchestration.

---

## Project Architecture

```text
GitHub → Jenkins → Docker → Kubernetes
```

---

## Technologies Used

- FastAPI
- Docker
- Kubernetes
- Minikube
- Jenkins
- Python
- kubectl

---

## Features

- FastAPI backend service
- Simple frontend dashboard
- Docker containerization
- Kubernetes deployment and scaling
- Kubernetes NodePort service exposure
- Jenkins CI/CD pipeline configuration
- Health check endpoint

---

## Application Endpoints

### Home Dashboard

```text
/
```

Displays the frontend dashboard.

### Health Check

```text
/health
```

Returns application health status.

---

## Project Structure

```bash
.
├── main.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── Jenkinsfile
└── README.md
```

---

## Run Application Locally

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t fastapi-cicd-app .
```

### Run Docker Container

```bash
docker run -p 8000:8000 fastapi-cicd-app
```

---

## Kubernetes Deployment

### Start Minikube

```bash
minikube start
```

### Deploy Application

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Verify Resources

```bash
kubectl get pods
kubectl get services
```

### Access Application

```bash
minikube service fastapi-service
```

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates:

- Docker image build
- Kubernetes deployment

Pipeline stages are defined inside:

```text
Jenkinsfile
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Containerization using Docker
- Kubernetes deployments and services
- CI/CD pipeline concepts
- Infrastructure automation
- Cloud-native application deployment
- Troubleshooting Kubernetes image issues

---

## Future Improvements

- Deploy to AWS EKS
- Add monitoring with Prometheus and Grafana
- Configure ingress controller
- Integrate GitHub Actions
- Add automated testing stages

---

## Author

Benjamin Chukwudi
