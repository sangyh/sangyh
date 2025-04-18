---
author: "Sangy"
title: "Deploying a Django app with Kamal"
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

# Deployment Guide

## Setting Up
Start from a boilerplate - don't reinvent the wheel. Clone repo from github. Use docker, kamal pegasus configuration.


## Update Deploy Config
Update docker and deployment settings (refer [Hosting Multiple Apps on One Droplet](/posts/productivity/droplet-management))

- deployment configuration in `config/deploy.yml`:
- docker-compose and docker-startup
- kamal secrets

```yaml
ALLOWED_HOSTS: "www.example.com,example.com,localhost"
AWS_STORAGE_BUCKET_NAME: '[YOUR-BUCKET-NAME]'
```

## Commit
1. Uncommit static/js and static/css folders
2. Commit to repo

## Domain DNS
Create a DNS record pointing to your server’s IP address.
Open Namecheap domain > DNS settings > Create A record pointing to server IP address.


## Deploy to VPS
Make sure everything is working by deploying to VPS.
1. Creaate repo on DockerHub - name should match the `image` field in deploy.yml.
2. Choose secure, unique, and ideally random values for POSTGRES_PASSWORD and SECRET_KEY.
3. Run `kamal setup`


## Update Settings

### Main Settings File
In `settings.py`, update the following:

- APPS
- BASE_URL 
- PROJECT_METADATA
- LLM setup
- Twilio, CloudFront, Celery beat etc.
- API Keys - VAPI, EXA, Deepgrame etc.

### Production Settings
In `settings_production.py`, configure:

```python
BASE_URL = "https://example.com"

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
ADMINS = [
    ("YourName", os.getenv('ADMIN_EMAIL')),
]
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": os.getenv('SENDGRID_API_KEY'),
    'WEBHOOK_SECRET': os.getenv('SENDGRID_WEBHOOK_SECRET'),
}
```

## Update Secrets
Add secrets to `.kamal` secrets and `config/deploy/yml`:

- ⚠️ NEVER commit actual secrets to your repository
- Use environment variables or dedicated secret management tools
- Store all API keys, passwords, and sensitive data in environment variables
- Consider using tools like `dotenv` for local development and cloud secret managers for production
- Rotate secrets regularly and use different secrets for different environments

## Deploy
Ensure your app is working on the domain before proceeding with further setup.

## Project-Specific Setup

### Management Commands
Run necessary management commands:

```bash
# Local environment
make manage ARGS='bootstrap_skills'

# Other commands
generate_outreachmessagetypes
```

### API Configuration
Configure VAPI server URL and other API endpoints.

## Database Access
Connect to your droplet database:

```bash
# Replace DB_USER with your database username from environment variables
kamal accessory exec postgres -i 'psql -h localhost -p 5432 -U $DB_USER' --reuse
```

## Useful Commands

### Kamal Commands

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

### Local Development Commands

| Command | Description |
|---------|-------------|
| `docker-compose exec web python manage.py makemigrations <app name>` | Create new database migrations for an app |
| `docker-compose exec web python manage.py shell` | Access Django interactive shell |
| `docker exec -it fleet-postgres bash` | Access interactive bash shell in Postgres container |
| `docker compose exec web pip install -r requirements.txt` | Install requirements in docker |
| `docker compose exec web pip list \| grep <package name>` | Check if a package is installed |
| `docker exec -it fleetapp-web-1 bash` | Access interactive bash shell in web container |

### Production Commands

| Command | Description |
|---------|-------------|
| `kamal app exec -i bash` | Access interactive bash shell in the application container |
| `ssh root@[YOUR-SERVER-IP]` | SSH into the deployment droplet |
| `kamal app logs -f -n 1000 -s web` | View last 1000 lines of web service logs with follow mode |
| `kamal app exec 'python manage.py promot_user_to_superuser <user email>'` | Promote a user to superuser status |
| `kamal accessory exec postgres -i 'psql -h localhost -p 5432 -U [database-user]' --reuse` | Connect to Postgres database with psql |

## Logging and Monitoring
- **Error Monitoring**: Sentry
- **Log Forwarding**: Paper Trail 

## References
1. [SaaS Pegasus Kamal Deployment Guide](https://docs.saaspegasus.com/deployment/kamal/?highlight=kamal)