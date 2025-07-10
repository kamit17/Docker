#!/usr/bin/env bash
set -e

# 1) As root, install ping & ssh if missing
if ! command -v ping &>/dev/null; then
  apt-get update \
    && apt-get install -y maven iputils-ping openssh-client \
    && rm -rf /var/lib/apt/lists/*
fi

# 2) Drop privileges to 'jenkins' and exec the *original* entrypoint
exec su jenkins -s /bin/bash -c "/usr/local/bin/jenkins.sh \"\$@\"" --
