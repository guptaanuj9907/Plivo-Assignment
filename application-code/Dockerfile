# Stage 1: Build stage
FROM python:3.9-slim AS build

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Stage 2: Runtime stage
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
