FROM python:3.12-slim

# Update the system and install necessary packages
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
       build-essential \
       postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pip and pipenv
RUN pip install --upgrade pip setuptools pipenv watchdog

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Default command (can be overridden by docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
