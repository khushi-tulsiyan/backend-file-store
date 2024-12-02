# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy server files
COPY ./server /app/

# Set the path explicitly to the requirements file
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port
EXPOSE 5000

# Run the server
CMD ["python", "app.py"]
