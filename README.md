# Kostkater ML Model API Tutorial

This tutorial provides step-by-step instructions on how to replicate and deploy the Kostkater ML Model API using Docker and Cloud Run. The Kostkater API is a machine learning model API that offers services related to Kostkater, an meal recommendation and planning.

## Access the Current API 

You can access the Kostkater ML Model API at the following URL: https://kostkater-api-bs2yfqpjra-et.a.run.app/

## Prerequisites

Before getting started, make sure you have the following:

- Docker installed on your machine
- Basic knowledge of Docker and containerization concepts

## Replicate this Projects

To replicate the Kostkater ML Model API, follow the steps below:

1. **Install Docker**: If you haven't installed Docker yet, you can download it from the official Docker website for your operating system.

2. **Run Docker**: Launch Docker on your machine.

3. **Clone the Repository**: Clone the Kostkater ML Model API repository to your local machine.

   ```bash
   git clone <repository_url>
   
4. **Build and Run**: Open a terminal and navigate to the project directory. Run the following command to build and run the Docker containers using the provided Docker Compose file.

   ```bash
   docker-compose -f docker-compose.development.yaml up --build
   
    ```
    This command will create and start the necessary Docker containers for the Kostkater ML Model API.
    
5. **Update the Files**: Once the Docker containers are running, you can make changes to the project files. The application will automatically reload whenever a file is updated.

## Deployment Steps using Docker and Cloud Run

1. **Build the Docker Image**: Open a terminal and navigate to the project directory. Run the following command to build the Docker image. Replace `<docker_username>` with your Docker username and `<project_name>` with the name of your project.

   ```bash
   docker build -t <docker_username>/<project_name>:1.1.0 .

2. **Login to Container Registry**: Run the following command to log in to your container registry. This step is necessary to push the Docker image.

   ```bash
   docker login

3. **Push the Docker Image**: Once you're logged in to the container registry, run the following command to push the Docker image to the registry. Replace `<docker_username>` and `<project_name>` with your Docker username and project name.
    
    ```bash
    docker push <docker_username>/<project_name>:1.1.0

4. **Deploy on Cloud Run**: Go to the Cloud Run console in your preferred cloud provider (such as Google Cloud Platform). Create a new Cloud Run service and provide the following information:

    - Service name: Choose a name for your Cloud Run service.
    - Container image: Specify the image URL of your Docker image from the container registry. It should be `<docker_username>/<project_name>:1.1.0.`
    - Configure additional settings as required (e.g., scaling, environment variables).

    Deploy the Cloud Run service with these configurations.

5. **Access the API**: After the Cloud Run service is successfully deployed, you can access the Kostkater ML Model API at the provided URL. Use this API URL to interact with the Kostkater ML Model and utilize its various services.
