---
author: "Sangy"
title: "One droplet to serve them all"
draft: false
date: "2025-01-26"
description: "Hosting multiple apps on a droplet"
tags: ["hugo", "blog", "netlify"]
categories: ["deployment", "tech"]
series: ["documentation"]
aliases: ["droplet-setup", "multi-app-hosting"] 
cover:
  image: images/image.png
  caption: "laptop"
---


Key Points:

Each app runs on a different port (8000 and 8001)
Both apps share the same IP address (128.199.2.146)
Nginx proxy routes traffic based on domain names

Step-by-Step:

Directory Structure

Separate data directories for each app
    /projects/rightjoin_III/deploy.yml  # service: rightjoin
    /projects/fleet/deploy.yml          # service: fleet
Unique paths for postgres and redis data
Example: /var/lib/rightjoin-data/postgres and /var/lib/rightjoin-data/redis


Port Configuration

Set different ports in deploy.yml for each app
    web:
        hosts:
        - 128.199.2.146
        options:
        expose: "8001"
Configure PORT environment variable - port 8000 is the default in Kamal, & you only need to specify PORT in the environment when using a non-default port.

    env:
    clear:
        DJANGO_SETTINGS_MODULE: rightjoin.settings_production
        ALLOWED_HOSTS: "rightjoin.co"
        USE_S3_MEDIA: 'True'
        AWS_STORAGE_BUCKET_NAME: 'rightjoin-media'
        STRIPE_LIVE_MODE: 'True'
        PORT: '8001'  # Add this
Update proxy settings to match ports
    proxy:
        ssl: true
        host: app.rightjoin.co
        app_port: 8001


Domain Setup

Configure DNS A records for both domains to same IP
Example:

app.rightjoin.co → 128.199.2.146
customchatbot.ai → 128.199.2.146



Kamal Deployment

Separate deploy.yml for each app
Independent deployments using kamal redeploy
Services defined by current working directory


Database Configuration

Separate postgres instances
Unique database names and users
Different data directories to avoid conflicts (update in docker-compose.yml and deploy.yml)
    services:
        db:
            volumes:
            - postgres_data:/var/lib/rightjoin-postgres/data # where rightjoin is the app name

        redis:
            volumes:
            - redis_data:/data/rightjoin
