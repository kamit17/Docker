FROM tomcat:9.0.85-jdk17-temurin

# Optional timezone
ENV TZ=UTC

# Copy custom user config
COPY ./tomcat-conf/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

# Copy manager context to remove IP restrictions
COPY ./tomcat-manager-context/context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
