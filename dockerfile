# Use Ubuntu as the base image
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y git docker.io docker-compose python3 python3-pip

# Clone the Git repository
RUN git clone https://github.com/Pythagora-io/gpt-pilot.git

# Replace the docker-compose.yml with your custom file
# Note: You need to have your custom docker-compose.yml in the build context
COPY ./custom-docker-compose.yml /gpt-pilot/docker-compose.yml

# Expose port 7681 for the web terminal
EXPOSE 7681 80 443

# Set the working directory
WORKDIR /gpt-pilot

# Run Docker Compose build and up commands
# Note: Docker-in-Docker requires privileged mode to run
CMD ["sh", "-c", "docker-compose build && docker-compose up"]