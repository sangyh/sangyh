---
author: "Sangy"
title: "Steps to deploy"
draft: false
date: "2025-01-03"
description: "using Hugo, PaperMod and Netlify."
tags: ["hugo", "blog", "netlify"]
categories: ["deployment", "tech"]
series: ["documentation"]
aliases: ["deployment-guide", "deploy-steps"]
cover:
  image: images/image.png
  caption: "laptop"
---


### Setting Up
Start from a boilder plate- don't reinvent the wheel.


### Initial Commit

### Update Deploy config
`config\deploy.yml`
ALLOWED_HOSTS: "www.customchatbot.ai,customchatbot.ai,localhost"
AWS_STORAGE_BUCKET_NAME: 'rightjoin-media'

### Update Settings
`settings.py`
APPS
BASE_URL 
PROJECT_METADATA
LLM setup
Twilio, CloudFront, Celery beat etc
API Keys - VAPI, EXA Deepgrame etc

`settings_production.py`
BASE_URL = "https://rightjoin.co"

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
ADMINS = [
    ("SangyH", "sangy@rightjoin.co"),
]
SERVER_EMAIL = "sangy@rightjoin.co"
DEFAULT_FROM_EMAIL = "sangy@rightjoin.co"
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": os.getenv('SENDGRID_API_KEY', default=None),
    'WEBHOOK_SECRET': 'OBFtyrZV1LubKJVz:r40kSYpGmguGEPH6',
}

### Update secrets
Add secrets to .kamal secrets and config/deploy/yml

### Deploy
App should be working on domain before processing

### Project specific setup
management commands - 
    bootstrap_skills - `make manage ARGS='bootstrap_skills'` on local and    
    generate_outreachmessagetypes
vapi server url

### Command to connect to droplet DB

`kamal accessory exec postgres -i 'psql -h localhost -p 5432 -U <youruser>' --reuse`

### Commands

| Command | Description |
|---------|-------------|
| `kamal deploy` | Deploy the application |
| `kamal rollback` | Rollback to previous version |
| `kamal lock` | Lock deployments |
| `kamal unlock` | Unlock deployments |
| `kamal app exec` | Execute command in app container |
| `kamal app logs` | View application logs |
| `kamal accessory exec` | Execute command in accessory container |
| `kamal accessory logs` | View accessory container logs |


Commonly used commands

Local Development Commands
| Command | Description |
|---------|-------------|
| `docker-compose exec web python manage.py makemigrations <app name>` | Create new database migrations for an app |
| `docker-compose exec web python manage.py shell` | Access Django interactive shell |
| `docker exec -it fleet-postgres bash` | Access interactive bash shell in Postgres container |
| `docker compose exec web pip install -r requirements.txt` | Install requirements in docker |
| `docker compose exec web pip list \| grep <package name>` | Check if a package is installed |
| `docker exec -it fleetapp-web-1 bash` | Access interactive bash shell in web container |


Production Commands
| Command | Description |
|---------|-------------|
| `kamal app exec -i bash` | Access interactive bash shell in the application container |
| `ssh root@128.199.2.146` | SSH into the deployment droplet |
| `kamal app logs -f -n 1000 -s web` | View last 1000 lines of web service logs with follow mode |
| `kamal app exec 'python manage.py promot_user_to_superuser <user email>'` | Promote a user to superuser status |
| `kamal accessory exec postgres -i 'psql -h localhost -p 5432 -U <youruser>' --reuse` | Connect to Postgres database with psql |

### Logging
Error Monitoring - Sentry
Log  Forwarding- Paper Trail 


### References
1. https://docs.saaspegasus.com/deployment/kamal/?highlight=kamal