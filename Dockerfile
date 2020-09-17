FROM python:3.8-alpine3.12

WORKDIR /app

# Copy the local project folder to working directory in container
COPY . .

# Use pip to install application's dependencies
RUN pip3 install -r requirements.txt