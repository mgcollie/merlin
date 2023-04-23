# Use an official Python runtime as a parent image
FROM python:3.10.8-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create a non-root user with a specific UID and GID
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} merlingroup && \
    useradd -u ${UID} -g ${GID} -m merlin

# Install any needed packages specified in requirements.txt
COPY --chown=merlin requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt


# Make a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY --chown=merlin . /app

# Set the user
USER merlin

# Run the Python script when the container launches
ENTRYPOINT ["python", "main.py"]
