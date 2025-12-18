# Use an official Python runtime as a parent image
FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

HEALTHCHECK --start-period=10s --interval=10s --timeout=5s --retries=3 \
  CMD curl -f http://0.0.0.0:8080/healthcheck/ || exit 1

# Run app.py when the container launches
CMD ["uvicorn", "book_api.main:app", "--host", "0.0.0.0", "--port", "8080"]