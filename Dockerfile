# Use an official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /

# Copy the requirements file to the container
COPY requirements.txt .

# Install required packages
RUN pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Specify the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]