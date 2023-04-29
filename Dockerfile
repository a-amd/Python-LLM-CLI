FROM python:3.11.3-alpine3.17

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt .

# Pip install
RUN pip install -r requirements.txt

# Copy all files from current directory to /app
COPY . .

# Run the command
CMD ["python3", "app.py"]