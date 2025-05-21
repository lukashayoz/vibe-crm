# Simple CRM Demo

A very simple CRM application for demo purposes, built with Flask and PostgreSQL.

## How to Run Locally

### Using Docker Compose (Recommended)

1.  **Start the application with Docker Compose:**
    ```bash
    docker-compose up -d
    ```

2.  **Access the application:**
    Open your browser and go to [http://localhost:5000](http://localhost:5000).

3.  **Shut down the application:**
    ```bash
    docker-compose down
    ```

### Using Docker Only

1.  **Build the Docker image:**
    ```bash
    docker build -t simple-crm-demo .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 simple-crm-demo
    ```

3.  **Access the application:**
    Open your browser and go to [http://localhost:5000](http://localhost:5000).

## Database Configuration

The application is set up to use PostgreSQL. By default, it connects to a database at `postgresql://postgres:postgres@db:5432/crm`.

For production use, set the `DATABASE_URL` environment variable to your production database connection string.

## Running Tests

To run the tests:

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```
