# flask-on-docker

![tests](https://github.com/rutisoniaisimbi4/flask-on-docker/actions/workflows/tests.yml/badge.svg)

## Overview

This repo contains a Dockerized Flask web application backed by PostgreSQL, served in production by Gunicorn and Nginx. The app supports a simple REST API including a file upload endpoint, and is designed to mirror the core of Instagram's original tech stack.

## Build Instructions

### Development
```bash
docker compose up -d --build
curl http://localhost:5010
```

### Production
```bash
docker compose -f docker-compose.prod.yml up -d --build
curl http://localhost:5010
```

### Upload a file
```bash
curl -F "file=@/path/to/file" http://localhost:5010/upload
```

### View uploaded file
```bash
curl http://localhost:5010/mediafiles/<filename>
```
