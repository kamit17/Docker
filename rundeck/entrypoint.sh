#!/bin/bash
set -e

# Launch Rundeck, force binding on all interfaces
exec java \
  -Xmx512m \
  -Xms256m \
  -Dgrails.server.host=0.0.0.0 \
  -Dserver.port=4440 \
  -Dfile.encoding=UTF-8 \
  -Dgrails.serverURL=http://0.0.0.0:4440 \
  -jar /rundeck/rundeck.war
