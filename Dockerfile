FROM ubuntu:latest AS base

# Set the timezone to Buenos Aires
ENV TZ=America/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Update and install wget
RUN apt-get update && apt-get install -y wget python3.10 python3-pip

# Download and install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Copy the files to the container
COPY main.py .
COPY import_data ./import_data
COPY model ./model
COPY data ./data
COPY requirement.txt .

# Install the Python dependencies
RUN pip3 install -r requirement.txt

# Start building the main application image
FROM base AS main

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the default command to run when the container starts
CMD ["python3", "main.py"]