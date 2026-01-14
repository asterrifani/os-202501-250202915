# Menggunakan Python 3.11 slim sebagai base image
FROM python:3.11-slim


# Set working directory
WORKDIR /app

# Install dependencies
# psutil untuk monitoring CPU dan memory
RUN pip install --no-cache-dir psutil

# Copy aplikasi ke container
COPY app.py .

# Pastikan script executable
RUN chmod +x app.py

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python3", "app.py"]