FROM debian:bullseye-slim

# 1. Install Java & tools
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    curl \
    procps \
    net-tools \
    vim \
 && rm -rf /var/lib/apt/lists/*

# 2. Create non-root user
RUN useradd -ms /bin/bash rundeck

# 3. Create dirs & set ownership
RUN mkdir -p /rundeck /rundeck/etc /rundeck/data \
 && chown -R rundeck:rundeck /rundeck

# 4. Copy WAR + config
COPY rundeck.war /rundeck/rundeck.war
COPY rundeck-config.properties /rundeck/etc/rundeck-config.properties
RUN chown rundeck:rundeck /rundeck/rundeck.war /rundeck/etc/rundeck-config.properties

# 5. Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 6. Switch user, expose port, launch
USER rundeck
WORKDIR /rundeck
EXPOSE 4440
ENTRYPOINT ["/entrypoint.sh"]
