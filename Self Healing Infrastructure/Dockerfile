# Use the official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and app
COPY webhook_app.py /app/webhook_app.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
	&& pip install ansible \
	&& ansible-galaxy collection install community.docker

# Copy playbooks directory (if exists)
#COPY playbooks /playbooks

# Expose port
EXPOSE 5001

# Run the app
CMD ["python", "/app/webhook_app.py"]
