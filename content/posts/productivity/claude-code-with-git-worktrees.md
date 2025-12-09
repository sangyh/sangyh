---
author: "Sangy"
title: "Supercharging Claude Code with Git Worktrees and Docker"
draft: false
date: "2025-08-10"
description: "How I eliminated merge conflicts and 10x'd my productivity by running multiple Claude Code sessions in parallel using Git worktrees and orchestrated Docker containers"
tags: ["claude", "productivity"]
categories: ["productivity", "development"]
series: []
aliases: []
cover:
  image: 
  caption: 
---


I've been using Claude Code extensively for the past few months, and I stumbled onto a workflow that completely changed how I ship features. The problem? Working on multiple features simultaneously meant constant merge conflicts. When Claude and I would work on `feature-auth` and `feature-payments` in parallel, we'd inevitably touch the same files and create a merge nightmare.

The solution came from an [Incident.io blog post](https://incident.io/blog/shipping-faster-with-claude-code-and-git-worktrees) about using Git worktrees. But my Django setup with Docker added a layer of complexity that took some engineering to solve.

## The Problem with Parallel Development

Here's what would happen before:
1. Start working on `feature-auth` with Claude
2. Get interrupted to fix a bug on `main`
3. Switch branches, fix the bug
4. Switch back to `feature-auth`
5. Meanwhile, work on `feature-payments` in another session
6. Both features modify `models.py` or `views.py`
7. Merge conflict hell

Working on multiple features meant either accepting the conflicts or working sequentially. Both killed productivity.

## Enter Git Worktrees

Git worktrees let you have multiple branches checked out simultaneously in different directories. Instead of switching branches, you just `cd` to a different folder. Each worktree is completely isolated - no more conflicts from parallel development.

But here's where it got interesting for my stack.

## The Docker Challenge

My Django app runs in Docker with PostgreSQL and Redis containers. Creating a worktree meant I'd need:
- Separate containers for each worktree
- Unique ports (can't have two Django apps on :8000)
- But shared database and Redis (I don't want data silos)

This is where most tutorials stop. "Just use worktrees!" they say. But what about the database migrations? The Redis cache? The Celery workers?

## My Solution: Orchestrated Worktree Setup

I built three interconnected bash scripts that handle the entire workflow:

### 1. The User Interface Layer (`git-worktree-helper.sh`)
```bash
# Create and enter a worktree with automatic Docker setup
wt project-name new-feature

# List all worktrees with their Docker status
wl

# Start/stop containers for a specific worktree
wstart project-name new-feature
wstop project-name new-feature
```

### 2. The Orchestration Layer (`setup-worktree.sh`)
This ensures the main containers are running, creates the shared Docker network, and manages the complete setup workflow. It's smart enough to:
- Auto-calculate port offsets (8001, 8002, etc.)
- Connect to the shared network
- Copy necessary files from the main project

### 3. The Configuration Layer (`worktree-docker-setup.sh`)
The Docker-specific magic happens here:
- Copies the main project's `.env` (with all your API keys)
- Adds worktree-specific settings
- Points `DATABASE_URL` and `REDIS_URL` to the shared containers

## The Architecture

```
Main Project (port 8000)
├── PostgreSQL (shared)
├── Redis (shared)
└── Docker Network: project-name
    ├── Worktree 1 (port 8001)
    ├── Worktree 2 (port 8002)
    └── Worktree N (port 8000+N)
```

Each worktree gets its own web and Vite containers but shares the database and Redis. This means:
- Migrations apply to all worktrees
- Session data persists across worktrees
- No data duplication

## The Workflow

Now my workflow looks like this:

```bash
# Working on authentication feature
wt project-name auth-feature
# Claude and I modify models.py, views.py, etc.

# Simultaneously working on payments
wt project-name payments-feature  
# Claude modifies the SAME files - no conflicts!

# Urgent bug comes in
wt project-name hotfix-bug
# Fix it in isolation, push it, done

# Each feature develops independently
# No stepping on each other's toes
```

## The Hidden Benefits

What I didn't expect:

1. **True Parallel Development**: I can have Claude working on different features that touch the same files without any conflicts
2. **Clean Merges**: Each feature merges cleanly to main because they developed in isolation
3. **Safe Experimentation**: Risky refactors get their own worktree. If it goes sideways, just `wr` (remove) it
4. **Container Isolation**: Each worktree's logs are separate. No more grep-ing through combined logs
5. **API Key Sharing**: The `.env` is copied from main, so all my OpenAI/Anthropic keys just work
6. **Context Preservation**: Claude maintains separate conversation context per directory - bonus!

## Implementation Tips

A few things I learned the hard way:

- **Container Names Matter**: Docker Compose uses underscores, bash uses hyphens. The scripts handle this translation.
- **Port Management**: I use the worktree's position in the directory list as the port offset. Simple and predictable.
- **Cleanup is Critical**: The `wclean` command removes merged worktrees automatically. Run it weekly.

## The Results

Still testing out this system - will post an update on whether this sticks or not.

The real win isn't just the speed - it's eliminating merge conflicts entirely. I can work on three features that all modify the same core files, and each merges cleanly when ready. No more "let me finish feature A before starting feature B because they touch the same code."

