# Use an official Python runtime as the base image
FROM python:3.9.7-slim

# Set the working directory
WORKDIR /app

# Copy the consumer code to the container
COPY consumer.py .

# Install the required packages
RUN pip install confluent-kafka

# Run the consumer code
CMD ["python", "consumer.py"]