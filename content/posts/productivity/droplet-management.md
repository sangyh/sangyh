---
author: "Sangy"
title: "Hosting Multiple Apps on One Droplet"
draft: false
date: "2025-01-26"
description: "Hosting multiple apps on a droplet"
tags: []
categories: ["deployment", "technical"]
series: []
aliases: ["droplet-setup", "multi-app-hosting"] 
cover:
  image: 
  caption: 
---


When running multiple applications on a single server, proper configuration is essential to avoid conflicts and ensure each app runs smoothly. This guide explains how to host multiple applications on one DigitalOcean droplet using Nginx as a reverse proxy.

## Key Points

- Each app runs on a different port (8000 and 8001)
- Both apps share the same IP address (128.199.2.146)
- Nginx proxy routes traffic based on domain names


Files to update:
- config/deploy.yml - update PORT and data directories + host domains
- docker-compose.yml - update PORT and data directories
- docker-startup.yml - update PORT

## Changes to deploy.yml

* Update the data directory for postgres data to create unique paths to avoid conflicts:


```directories:
      - data:/var/lib/rightjoin-postgres/data
```      

Why?
In default config (in fleet app deploy.yml), the container path is /var/lib/postgresql/data (Postgres's default data directory). In rightjoin app, the container path was /var/lib/rightjoin-postgres/data (a custom path)

- `/var/lib/rightjoin-data/postgres`  # update name with app name
- `/var/lib/rightjoin-data/redis`

When Kamal sees this configuration, it will:
- Create a directory on the host machine (likely at /root/fleet-postgres/data)
- Mount this directory to /var/lib/rightjoin-postgres/data inside the container

* Update the data directory for redis data to create unique paths to avoid conflicts:
Rightjoin has a data directory for redis where fleet (Default) does not

For your Redis configuration in the fleet app, I don't have a directories section, but kamal is automatically creating a volume for redis and mounting to /data inside the container. To create a separate dir, add config below similar to rightjoin redis config: 

```
## docker hostname will be 'rightjoin-redis'
  redis:
    image: redis
    host: 128.199.2.146
    directories:
      - data:/data/rightjoin 
```


* Port Configuration

 Set different ports in deploy.yml for each app

```yaml
web:
  hosts:
    - 128.199.2.146
  options:
    expose: "8001"
```

### Configure PORT environment variable

Port 8000 is the default in Kamal, and you only need to specify PORT in the environment when using a non-default port:

```yaml
env:
  clear:
    DJANGO_SETTINGS_MODULE: rightjoin.settings_production
    ALLOWED_HOSTS: "rightjoin.co"
    USE_S3_MEDIA: 'True'
    AWS_STORAGE_BUCKET_NAME: 'rightjoin-media'
    STRIPE_LIVE_MODE: 'True'
    PORT: '8001'  # Add this for non-default port
```

### Update proxy settings to match ports

```yaml
proxy:
  ssl: true
  host: app.rightjoin.co
  app_port: 8001
```

## Domain Setup

Configure DNS A records for both domains to point to the same IP:

| Domain | Points to |
|--------|-----------|
| app.rightjoin.co | 128.199.2.146 |
| customchatbot.ai | 128.199.2.146 |

## Kamal Deployment

- Maintain separate `deploy.yml` for each app
- Perform independent deployments using `kamal redeploy`
- Services are defined by the current working directory

## Database Configuration

### Separate database instances

Configure unique database names and users for each application. Use different data directories to avoid conflicts by updating in `docker-compose.yml` and `deploy.yml`:

```yaml
services:
  db:
    volumes:
      - postgres_data:/var/lib/rightjoin-postgres/data # where rightjoin is the app name

  redis:
    volumes:
      - redis_data:/data/rightjoin
```

By following these steps, you can successfully host multiple applications on a single droplet while keeping their configurations separate and secure.
