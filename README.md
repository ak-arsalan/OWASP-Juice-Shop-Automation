# OWASP Juice Shop Test Suite

## Description

This project provides a test suite for the OWASP Juice Shop. The test suite covers the following functionalities:

1. Pagination functionality to show different items per page.
2. Changing the amount of items per page lists the correct amount of items.
3. Changing the language 
4. The login form returns an error message in case of an invalid user password combination.
5. Successful login using valid Credentials

## Security Tests

   Added security tests to demonstrate vulnerabilities such as XSS and SQL Injection.

## Prerequisites

- Docker
- Python
- pip

## Setup

1. **Install Docker:**

   Follow the instructions to install Docker from the [official Docker website](https://www.docker.com/).

2. **Pull the OWASP Juice Shop Docker Image:**

   ```sh
   docker pull bkimminich/juice-shop
   ```
3. **Run the OWASP Juice Shop Docker Container:**

   ```sh
   docker run --rm -p 3000:3000 bkimminich/juice-shop
   ```

4. **Access the Juice Shop Application:**

   Open your browser and navigate to http://localhost:3000.

   **Note:** On macOS and Windows, if you are using Docker Machine instead of the native Docker installation, browse to http://192.168.99.100:3000.

## Clone the git repository

   ```sh
   git clone https://github.com/ak-arsalan/OWASP-Juice-Shop-Automation.git
   ```

## Create Virtual Environment

   ```sh
   python -m venv venv
   ```
## Activate Virtual Environment

   ```sh
   venv/Scripts/activate (Windows) 
   source venv/bin/activate (Mac & Linux)
   ```

## Installation of Dependencies

To install the necessary Python dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

## Running the Tests

1. **Ensure the OWASP Juice Shop application is running.**

2. **Navigate to the project directory and execute the test suite:**
   
   ```sh
   pytest -s
   ```

# Clean up

1. **Stop the Docker container:**

   ```sh
   docker stop $(docker ps -q --filter ancestor=bkimminich/juice-shop)
   ```

2. **Remove unused Docker resources:**

   ```sh
   docker system prune -af
   ```