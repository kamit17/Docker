FROM ak6790435/jenkins-docker-enabled

USER root
# Install Maven (and clean up apt lists)
RUN apt-get update && apt-get install -y maven \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
