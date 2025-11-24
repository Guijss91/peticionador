# Multi-stage build for Tailwind CSS compilation
FROM node:20-alpine AS tailwind-builder

WORKDIR /app

# Install Tailwind CSS
RUN npm install -D tailwindcss@latest

# Copy Tailwind config and source files
COPY tailwind.config.js .
COPY static/src ./static/src
COPY templates ./templates

# Build Tailwind CSS
RUN npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --minify

# Python application stage
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates ./templates
COPY static ./static

# Copy compiled CSS from builder stage
COPY --from=tailwind-builder /app/static/dist/output.css ./static/dist/output.css

# Create dist directory if it doesn't exist
RUN mkdir -p static/dist

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
