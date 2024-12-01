# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy server files
COPY ../server /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the server
CMD ["python", "app.py"]
