---
author: "Sangy"
title: "Building My AI Assistant with OpenClaw: A Weekend Setup Guide"
draft: false
date: "2026-01-30"
description: "How I set up OpenClaw on a VPS to create a personal AI assistant that can manage my email, calendar, Twitter, and more"
tags: ["ai", "automation", "openclaw", "productivity"]
categories: ["hacking"]
series: []
aliases: []
cover:
  image: 
  caption: 
---

I spent this weekend setting up [OpenClaw](https://github.com/openclaw/openclaw) — an open-source framework for building personal AI assistants. The result? An AI that can read my emails, check my calendar, draft tweets, and actually *do things* on my behalf.

Here's how I did it.

## What is OpenClaw?

OpenClaw is a self-hosted AI agent framework. Think of it as the infrastructure for giving Claude (or other LLMs) access to your tools and services. It handles:

- **Session management** — maintains conversation context
- **Tool integration** — browser automation, shell commands, APIs
- **Channel plugins** — WhatsApp, Telegram, Discord, etc.
- **Memory** — persistent context across sessions

The key difference from ChatGPT or Claude.ai? It runs on *your* infrastructure, with access to *your* stuff.

## The Setup

I'm running OpenClaw on an AWS EC2 instance (Ubuntu). Here's what I connected:

### 1. Browser Automation

OpenClaw can control a headless Chrome browser. This required some Linux-specific setup:

```bash
# Install Chrome (not the snap version — it has sandbox issues)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y

# Virtual display for headless operation
sudo apt install xvfb
nohup Xvfb :99 -screen 0 1920x1080x24 &
```

Then configure OpenClaw:
```json
{
  "browser": {
    "enabled": true,
    "executablePath": "/usr/bin/google-chrome-stable",
    "headless": true,
    "noSandbox": true,
    "attachOnly": true
  }
}
```

**Gotcha:** Twitter/X blocks headless browser logins aggressively. I ended up using the [bird CLI](https://github.com/steipete/bird) instead — it uses cookie auth and works great.

### 2. Twitter/X via Bird CLI

Bird is a fast CLI for Twitter that uses cookie authentication:

```bash
npm install -g @steipete/bird
```

Export your cookies from a logged-in browser session:
```bash
export AUTH_TOKEN="your_auth_token"
export CT0="your_ct0_cookie"
bird whoami  # Should show your handle
```

Now the AI can post tweets, read mentions, search, etc.

### 3. Google Workspace (Gmail, Calendar, Drive, Docs)

This was the most valuable integration. I set up OAuth with read-only scopes:

1. Created a Google Cloud project
2. Enabled Gmail, Drive, Calendar, and Docs APIs
3. Set up OAuth consent screen (Internal for Workspace)
4. Created Web Application credentials
5. Ran the OAuth flow to get refresh tokens

The scopes I used:
- `gmail.readonly`
- `drive.readonly`
- `calendar.readonly`
- `documents.readonly`

I wrote a helper script that handles token refresh automatically:

```bash
./google-api.sh gmail unread 5      # List unread emails
./google-api.sh calendar upcoming    # Show upcoming events
./google-api.sh drive search "TalentPrism"  # Search Drive
```

### 4. Email (Himalaya CLI)

For email that isn't Google, I use [Himalaya](https://github.com/pimalaya/himalaya) — a CLI email client:

```bash
himalaya envelope list              # List inbox
himalaya message read <id>          # Read email
himalaya message write              # Compose
```

## The Workspace Structure

OpenClaw uses a workspace folder with special files:

```
~/clawd/
├── AGENTS.md      # Instructions for the AI
├── SOUL.md        # Personality/tone guidelines
├── USER.md        # Info about me
├── MEMORY.md      # Long-term memory (curated)
├── TOOLS.md       # Local tool configurations
├── HEARTBEAT.md   # Periodic check instructions
└── memory/
    └── 2026-01-30.md  # Daily notes
```

The AI reads these files at the start of each session. `MEMORY.md` persists important context — decisions, preferences, project details. Daily notes in `memory/` capture raw logs.

## What Can It Do Now?

After setup, my AI assistant (named Kaju 🌰) can:

- **Read my Gmail** and summarize important emails
- **Check my calendar** for upcoming meetings
- **Search Google Drive** for documents
- **Draft and post tweets** (when I approve)
- **Review documents** and provide summaries
- **Remember context** across sessions

Example interaction:
```
Me: "Can you review Joe's most recent email?"
Kaju: [searches Gmail, finds email, provides summary with action items]

Me: "Draft a reply"
Kaju: [drafts reply, sends to my inbox for review]
```

## Lessons Learned

1. **Snap packages suck for automation** — Chrome's snap version has AppArmor issues. Use the .deb.

2. **Twitter hates bots** — Don't try to automate login. Use cookie auth (bird CLI) or the official API.

3. **OAuth is worth the hassle** — App passwords work but OAuth gives you scoped, revocable access.

4. **Memory files are crucial** — Without `MEMORY.md`, every session starts from scratch. Invest in documenting context.

5. **Read-only is a good start** — I intentionally limited Google access to read-only. I can expand later once I trust the setup.

## What's Next

- **Write access** for calendar (create events) and drafts (compose emails)
- **Proactive notifications** — alert me about important emails or calendar conflicts
- **GitHub integration** — PR reviews, issue triage
- **Voice interface** — already have ElevenLabs set up via the `sag` skill

The dream is an AI that handles the administrative overhead of life — triaging email, managing calendar, keeping notes organized — so I can focus on the actual work.

---

*Running OpenClaw? I'd love to hear about your setup. Find me on Twitter [@sangyh2](https://twitter.com/sangyh2).*
