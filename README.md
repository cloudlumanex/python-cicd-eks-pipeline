# Python CI/CD Pipeline to AWS EKS

A complete DevOps demonstration project showcasing automated CI/CD pipeline using GitHub Actions, Docker, Kubernetes (EKS), and security scanning.

## 🚀 Features

- **Containerization**: Docker with multi-stage builds
- **Security Scanning**: Trivy vulnerability scanning
- **Container Registry**: GitHub Container Registry (GHCR)
- **Orchestration**: Kubernetes (AWS EKS)
- **CI/CD**: GitHub Actions automated pipeline
- **Infrastructure**: AWS EKS cluster provisioned with eksctl
- **Monitoring**: Health checks and readiness probes

## 🏗️ Architecture
```
GitHub → GitHub Actions → Docker Build → Trivy Scan → GHCR → Deploy to EKS → LoadBalancer
```

## 📋 Prerequisites

- AWS Account with appropriate permissions
- GitHub Account
- AWS CLI configured
- kubectl installed
- eksctl installed

## 🛠️ Technologies Used

- **Application**: Python Flask
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AWS EKS)
- **CI/CD**: GitHub Actions
- **Security**: Trivy vulnerability scanner
- **Cloud Provider**: AWS
- **Container Registry**: GitHub Container Registry

## 🚦 Pipeline Stages

1. **Build**: Docker image built with Python Flask application
2. **Scan**: Trivy scans for vulnerabilities
3. **Push**: Image pushed to GitHub Container Registry
4. **Deploy**: Automated deployment to EKS cluster
5. **Verify**: Health checks and service exposure

## 📦 Project Structure
```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
├── k8s/
│   ├── deployment.yaml         # Kubernetes deployment
│   └── service.yaml            # LoadBalancer service
├── static/
│   └── style.css               # Application styles
├── templates/
│   └── index.html              # Web interface
├── app.py                      # Flask application
├── Dockerfile                  # Container definition
└── requirements.txt            # Python dependencies
```

## 🔧 Setup Instructions

### 1. Create EKS Cluster
```bash
eksctl create cluster \
  --name devops-project-cluster \
  --region eu-west-1 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 2 \
  --managed
```

### 2. Configure GitHub Secrets

Add these secrets to your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### 3. Push to GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

The pipeline will automatically trigger and deploy your application!

## 🌐 Access the Application

After deployment, get the LoadBalancer URL:
```bash
kubectl get service python-app-service
```

Open the provided URL in your browser to see the dashboard.

## 📊 Monitoring

Check deployment status:
```bash
kubectl get pods
kubectl get services
kubectl logs -f deployment/python-app
```

## 🧹 Cleanup
```bash
# Delete Kubernetes resources
kubectl delete -f k8s/

# Delete EKS cluster
eksctl delete cluster --name devops-project-cluster --region eu-west-1
```

## 👨‍💻 Author

**Emmanuel Ulu**

## 📝 License

This project is for educational and demonstration purposes.
# Retrying with fixed AWS credentials
