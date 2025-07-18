# Full Stack App Setup

## Overview

This project is a simple full-stack web application built and deployed as part of the Maincode Software Development Engineer take-home assignment.  
It demonstrates end-to-end setup, code clarity, and developer experience using modern tooling and cloud deployment.

**Tech Stack:**

- **Frontend:** React (Vite)
- **Backend:** Python Flask
- **Database:** SQLite
- **Containerization:** Docker, Docker Compose
- **Cloud Deployment:** Azure Container Instances
- **CI/CD:** GitHub Actions

---

## Features

- **Frontend:** Displays a "Hello, Maincode!" message and checks API health.
- **Backend:** Provides `/api/hello` and `/api/healthcheck` endpoints.
- **Database:** SQLite with basic initialization and usage.
- **Health Check:** `/api/healthcheck` endpoint for monitoring.
- **CI/CD:** Automated build and deployment via GitHub Actions.

---

## Local Development

### Prerequisites

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) (recommended for DevContainer support)

### Steps

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd maincode-app
   ```

2. **Open in DevContainer (VS Code):**

   - Open the folder in VS Code.
   - If prompted, "Reopen in Container".

3. **Run the stack with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend: [http://localhost:8000](http://localhost:8000)

---

## Cloud Deployment (Azure Container Instances)

### Automated Deployment

Deployment is handled via GitHub Actions.  
On push to `main`, the workflow:

- Builds and pushes Docker images for frontend and backend to Azure Container Registry.
- Deploys containers to Azure Container Instances with public DNS endpoints.

### Manual Deployment

1. **Set up Azure resources:**

   - Azure Container Registry
   - Resource Group

2. **Configure GitHub Secrets:**

   - `AZURE_CREDENTIALS`
   - `ACR_LOGIN_SERVER`
   - `ACR_USERNAME`
   - `ACR_PASSWORD`
   - `RESOURCE_GROUP`
   - `ACI_BACKEND_NAME`
   - `ACI_BACKEND_DNS`
   - `ACI_FRONTEND_NAME`
   - `ACI_FRONTEND_DNS`

3. **Push to `main` branch:**  
   The workflow will build, push, and deploy automatically.

---

## Trade-offs & Limitations

- **Database:** Uses SQLite for simplicity; not suitable for production scale.
- **CORS:** Backend must be configured to allow requests from the deployed frontend URL.
- **Secrets:** All cloud credentials must be set in GitHub Actions.
- **No migrations:** Database migrations are not automated.
- **Monitoring:** Basic health check endpoint only.

---

## Areas for Improvement

- Add automated database migrations.
- Enhance error handling and logging.
- Add more robust health checks and monitoring.
- Use environment variables for more flexible configuration.
- Add integration tests to CI workflow.

---

## Optional Bonus Features

- Health check endpoint (`/api/healthcheck`)
- GitHub Actions workflow for CI/CD
- Containerized database initialization
- Basic error handling in API

---

## How to Contact

For questions or feedback, please reach out via GitHub Issues.
