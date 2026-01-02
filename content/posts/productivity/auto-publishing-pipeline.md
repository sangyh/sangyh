---
title: "Building a publishing pipeline for Talentprism blog"
date: 2025-12-25
draft: false
tags: ["automation", "Talentprism"]
categories: ["productivity"]
summary: "I wanted my AI writing tool to publish directly to my blog. Here's how I wired up Arvow, Cloudflare Workers, GitHub, and Vercel into one seamless pipeline."
---

### The Problem

I use [Arvow](https://arvow.com) to help me write blog posts. It's great at generating content, but the publishing workflow was manual—copy the markdown, create a file, commit to GitHub, wait for deploy. Boring.

I wanted a one-click flow: **write in Arvow → click publish → live on my blog**.

### The Architecture

Here's the flow:

```
┌─────────┐      ┌────────────────────┐      ┌────────────┐      ┌─────────┐
│  Arvow  │ ──── │ Cloudflare Worker  │ ──── │   GitHub   │ ──── │ Vercel  │
└─────────┘      └────────────────────┘      └────────────┘      └─────────┘
     │                    │                        │                  │
  Publish          Validate secret           Store .md file      Build Hugo
  article          Transform to Hugo         Trigger deploy       Go live!
```

The whole thing took about 30 minutes to set up, and now I never touch the terminal to publish.

### How Each Piece Works

#### 1. Arvow → Cloudflare Worker

When I click "publish" in Arvow, it fires a webhook to my Cloudflare Worker with the article title, content (in markdown!), tags, and a thumbnail.

#### 2. Cloudflare Worker → GitHub

The Worker does three things:
- Validates the secret header (so randos can't spam my blog)
- Wraps the content in Hugo frontmatter
- Creates the file in my GitHub repo via the REST API

It's about 100 lines of JavaScript. The Worker runs on Cloudflare's edge network, so it's fast and free.

#### 3. GitHub → Vercel

My blog repo is connected to Vercel. Any push to `main` triggers an automatic deploy. So the moment the Worker creates the file, Vercel starts building.

#### 4. Vercel → Live Blog

Vercel runs Hugo, generates the static site, and deploys. About 30 seconds after I click "publish" in Arvow, the post is live.

### Why I Love This

- **Zero friction** — Write, click, it's live
- **Git history** — Every post is a commit I can revert
- **Free** — Cloudflare free tier + Vercel free tier + GitHub free
- **Extensible** — Could add image optimization, social sharing, whatever

### What's Next

I'm thinking about adding:
- Automatic tweet when a post publishes
- Image upload to Cloudflare R2
- A "schedule for later" feature using Cloudflare Queues

For now, this setup is exactly what I needed. Sometimes the best automation is the one you can build in an afternoon.

---

*Want the code? Hit me up on Twitter.*
