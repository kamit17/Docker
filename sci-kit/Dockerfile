#Dockerfile

#Specify the base image that we are building the image on top of
FROM matthewfeickert/intro-to-docker:latest

#Build the image as root user
USER root

#Run some bash commands to install packages
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install cowsay && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt-get/lists/** && \
    ln -s /usr/games/cowsay /usr/bin/cowsay
RUN pip install --no-cache-dir -q scikit-learn

#This sets the default working directory when a container is launched from the image
WORKDIR /home/docker

#Run as docker user by default when the container starts up
USER docker
