# Offline Rundeck + PostgreSQL Docker Setup

This repository provides everything you need to build, save, and run a full Rundeck + PostgreSQL stack in an **offline** or air-gapped environment. It uses a custom Debian-based Docker image for Rundeck with your configuration baked in, and a Docker Compose file that leverages host networking to ensure accessibility.

## Repository Structure

```text
rundeck-offline-build/
├── Dockerfile
├── entrypoint.sh
├── rundeck-config.properties
├── rundeck.war
└── docker-compose.yml
```

1. **Dockerfile** – Builds a Debian-slim image with OpenJDK, your Rundeck WAR, configuration, and an entrypoint script.
2. **entrypoint.sh** – Startup script that launches Rundeck with JVM flags forcing the server to bind on `0.0.0.0:4440`.
3. **rundeck-config.properties** – Rundeck application config (base URL, DB settings, storage plugins).
4. **rundeck.war** – The Rundeck WAR file you downloaded (version must match your target).
5. **docker-compose.yml** – Orchestrates PostgreSQL and the custom Rundeck container in host network mode.

## Prerequisites (Build Machine)

- Docker Engine (with `docker build`, `docker save`).
- Internet access to pull base images and download the Rundeck WAR.
- `wget` or browser to download the Rundeck WAR from [https://download.rundeck.com/community/](https://download.rundeck.com/community/)

## 1. Download the Rundeck WAR

On your build machine:

```bash
cd rundeck-offline-build
wget https://download.rundeck.com/community/GA/rundeck-4.10.0/rundeck-4.10.0.war -O rundeck.war
```

## 2. Build & Save Docker Images

```bash
# Build custom Rundeck image
docker build -t rundeck-offline:latest .

# Save the Rundeck image to a tarball
docker save -o rundeck-offline.tar rundeck-offline:latest

# Pull and save PostgreSQL image
docker pull postgres:15.2
docker save -o postgres-15.2.tar postgres:15.2
```

Copy these `.tar` files plus the 5 repository files to your **offline** server.

## 3. Load & Run on Offline Server

```bash
# Load images
docker load -i postgres-15.2.tar
docker load -i rundeck-offline.tar

# Start the stack
docker-compose up -d
```

- **Rundeck** will be reachable at `http://localhost:4440` (login: `admin` / `admin`).
- **PostgreSQL** data persists in the `dbdata` volume.

## 4. Verification

```bash
# Check containers
docker ps

# Confirm Rundeck is binding on all interfaces
docker exec -it rundeck-offline_build_rundeck_1 netstat -tulpn | grep 4440
# Should show :::4440 (host network mode)
```

## Customization

- **Change DB:** Edit `rundeck-config.properties` to point to another database.
- **Add Plugins:** COPY plugin `.jar` files into `/rundeck/lib/` in the Dockerfile.
- **SSL/HTTPS:** Mount or bake your certs and add `-Dserver.ssl.*` flags in `entrypoint.sh`.

## FAQs

**Q: Why host networking?**\
Rundeck’s embedded server sometimes binds only to `127.0.0.1` inside the container. Host networking maps container localhost to the host’s localhost.

**Q: How to add more users?**\
Mount a custom `realm.properties` at `/home/rundeck/etc/realm.properties` via `docker-compose.yml`.

## License

This project is provided under the MIT License. See [LICENSE](LICENSE) for details.

