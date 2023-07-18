# DevOps Course Pipeline Project - Deployment of DjangoApp
This project aims to create a pipeline for deploying the DjangoApp (Communication System) using two different approaches: Docker Compose for the master branch and Kubernetes (minikube) for the kubernetes_pipeline branch. The pipeline will be set up using Jenkins to automate the deployment process. Please note that this pipeline is designed to work on Ubuntu OS only.

## Prerequisites
Ensure that the following applications are installed on your Ubuntu machine before proceeding:
- Docker
- Docker Compose (For master branch)
- Minikube and Kubernetes CLI (For kubernetes_pipeline branch)
- Jenkins

## Setup
### Pipeline Setup for Docker Compose (master branch)
1. Create a new Jenkins pipeline job.
2. Configure the pipeline to use Jenkinsfile from SCM (GitHub repository) and connect it to your DjangoApp project.
3. Set the pipeline to build the master branch.

### Pipeline Setup for Kubernetes (kubernetes_pipeline branch)
1. Create another Jenkins pipeline job.
2. Configure the pipeline to use Jenkinsfile from SCM (GitHub repository) and connect it to your DjangoApp project.
3. Set the pipeline to build the kubernetes_pipeline branch.

## Pipelines Flow

### Docker Compose (master branch)
1. **Verify tooling**: This stage checks the presence and versions of Docker, Docker Compose, and Kubernetes CLI.
2. **Prune Docker data**: This stage removes unused Docker data to free up space.
3. **Create .env file**: This stage creates the .env file with the required environment variables for the DjangoApp.
4. **Build images** and push to docker-hub: This stage builds the Docker images for the DjangoApp and pushes them to Docker Hub.

### Kubernetes (kubernetes_pipeline branch)
1. **Verify tooling**:  This stage checks the presence and versions of Docker, Minikube, and Kubernetes CLI.
2. **Prune Docker data**: This stage removes unused Docker data to free up space.
3. **Build images on docker-hub**: This stage builds the Docker images for the DjangoApp and tags them accordingly.
4. **Push images to minikube container**: This stage loads the Docker images into the Minikube container.
5. **Deploy k8s pods**: This stage applies the Kubernetes deployment files to deploy the DjangoApp using Minikube.


## Project members
This repository was created by the following programmers:
- [Raziel Shushan](https://github.com/RazielShushan).
- [Matan Alter](https://github.com/matan_alter).
- [Alice Motzlov](https://github.com/alice_motzlov).
- [Ori Ronen](https://github.com/orironen555).
  
## DjangoApp Repository
For this project, we used the following GitHub repository for the DjangoApp:
- [DjangoApp Repository](https://github.com/orironen555).

