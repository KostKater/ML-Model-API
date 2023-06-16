# Kostkater ML Model API Tutorial

This tutorial provides step-by-step instructions on how to replicate and deploy the Kostkater ML Model API using Docker and Cloud Run. The Kostkater API is a machine learning model API that offers services related to Kostkater, an meal recommendation and planning.

## Access the Current API 

You can access the Kostkater ML Model API at the following URL: https://kostkater-api-bs2yfqpjra-et.a.run.app/

## Prerequisites

Before getting started, make sure you have the following:

- Docker installed on your machine
- Basic knowledge of Docker and containerization concepts

## Deployment Steps

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
