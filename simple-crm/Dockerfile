# 1. Start from a Python base image
FROM python:3.9-slim

# 2. Set a working directory
WORKDIR /app

# 3. Copy the requirements.txt file
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install -r requirements.txt

# 5. Copy the app directory
COPY app ./app

# 6. Expose port 5000
EXPOSE 5000

# 7. Specify the command to run the application
CMD ["python", "app/main.py"]
