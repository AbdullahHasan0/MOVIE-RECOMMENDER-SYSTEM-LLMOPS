## Parent Image
FROM python:3.10-slim

## Essential Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work Directory
WORKDIR /app

## Installing System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying all contects from local to app
COPY . .

## Run setup.py
RUN pip install --no-cache-dir -e .

## Used PORTS
EXPOSE 8501

# run the application
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]