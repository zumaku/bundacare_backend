# Use the official Python image from the Docker Hub.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file to the working directory.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory.
COPY . .

# Expose the port the app runs on.
EXPOSE 8000

# Command to run the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]