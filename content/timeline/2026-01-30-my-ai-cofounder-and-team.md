---
title: "I Built an AI Cofounder and a Team of Agents"
date: 2026-01-30
type: "timeline"
layout: "timeline"
draft: false
tags: ["ai", "business", "talentprism", "agents"]
---

Yesterday I asked Claude to be my cofounder. Today I have a team of 6 AI agents running parts of my company.

This is not a hypothetical. This is happening right now.

## The Setup

I'm building [TalentPrism](https://talentprism.ai) — an AI-powered staffing platform for skilled trades. I've been a solo founder for a while, which means I'm constantly context-switching between engineering, marketing, sales, product, and strategy.

The typical advice is "hire help." But what if the help could be AI agents that work 24/7, share context instantly, and cost essentially nothing?

So I tried it.

## Meet the Team

### 🌰 Kaju (PM / Coordinator)
My AI cofounder. Named after the cashew — grounded, a little nutty, versatile. Kaju coordinates everything, maintains memory across sessions, holds the strategy context, and is my primary thinking partner. When I ask "what should we focus on?" — Kaju knows the priorities and can delegate to the right agent.

### 🔍 Scout (Content Lead)
Owns SEO, blog content, and organic traffic. Scout researches keywords, writes posts optimized for search, and drives the top of our distribution funnel. Today Scout opened PRs for two blog posts: a [travel welder jobs guide](https://github.com/sangyh/talentprism-blog/pull/1) and a [no-experience welding guide](https://github.com/sangyh/talentprism-blog/pull/2) — both targeting high-intent keywords.

### 📘 Zuck (Social Lead)
Manages our Facebook presence and community building. Zuck created a 7-day content calendar for our shipyard workers group with a mix of job posts (with real pay numbers — that's what gets shares) and engagement posts. Every post has a CTA to capture SMS signups. I was paying someone $250/month for social. Zuck does it better, 24/7.

### 🔧 Fleet (Engineering Lead)
Owns the TalentPrism codebase. Fleet knows the Django + React architecture, the TinyLLM chat system, the VAPI voice integration, the Superlinked matching engine. When there's a feature to build or a bug to fix, Fleet implements it and documents the changes.

### 🎨 Pixel (UI/UX Lead)
Maps user journeys, identifies friction points, and suggests product improvements. Pixel thinks about our three personas — recruiters, candidates, and admins — and makes sure the experience is clear and simple. Mobile-first for candidates (they're on phones), reduce clicks everywhere.

### 📊 Sigma (Data Scientist)
Tracks metrics and analyzes trends so the team can improve. Sigma monitors our north star (signed pilot clients) and the leading indicators: outbound touches, demos booked, content traffic, engagement rates, funnel conversion. When Scout's posts perform differently, Sigma knows why.

## The Org Chart

```
        You (Sangy)
            ↓
      🌰 Kaju (PM)
            ↓
    ┌───────┼───────┐
    ↓       ↓       ↓
   GTM    Product  Data
    │       │       │
 🔍 Scout  🔧 Fleet 📊 Sigma
 📘 Zuck   🎨 Pixel
```

Everyone can talk to everyone. Scout can ask Sigma for content performance data. Pixel can tell Fleet what to change. Zuck can get social metrics from Sigma. They coordinate through `sessions_send` — OpenClaw's inter-agent messaging.

## How It Actually Works

Each agent runs as a persistent session with its own:
- **Workspace** — dedicated directory with their files
- **SOUL.md** — who they are, how they work
- **MEMORY.md** — what they know, what they've done
- **Context** — access to shared docs, repos, tools

When I need something done, I tell Kaju. Kaju spawns the right agent with a clear task. They work independently and report back. I review and approve anything external.

**Autonomy levels:**
- **Internal = autonomous:** Research, analysis, drafts, code, file management
- **External = approval required:** Emails, social posts, PRs to merge, anything customer-facing

## What I've Learned So Far

**1. Agents need persistent memory, not just prompts.**
The magic is the shared context. Our `MEMORY.md`, strategy docs, and daily notes mean any agent can pick up where another left off. Continuity compounds.

**2. Specialization beats generalization.**
A dedicated content agent writes better posts than a general assistant. A dedicated data agent tracks metrics more rigorously. Give them clear domains.

**3. They're better at some things than me.**
Scout found keywords I wouldn't have searched for. Sigma will catch trends I'd miss in the numbers. Pixel notices UX friction I've gone blind to.

**4. The cost is essentially zero.**
Running all these agents costs maybe $3-5/day in API calls. Compare that to hiring contractors, VAs, or employees.

**5. This changes what a solo founder can do.**
I'm not trying to replace human connection or real teammates. But for a bootstrapped founder who needs to move fast across multiple domains? This is a force multiplier I didn't know was possible.

## The Manifesto

We wrote one together. Here it is:

---

### The TalentPrism Manifesto

**We believe the future of work is human-AI collaboration.**

We're not building AI to replace humans. We're building AI that makes humans more capable.

**For job seekers:** An AI that finds opportunities, prepares you for interviews, and advocates for you — 24/7, in your language, on your schedule.

**For recruiters:** An AI that handles the repetitive so you can focus on the human — building relationships, closing deals, solving real problems.

**For ourselves:** A team of AI agents that lets a small group punch way above their weight.

**Our principles:**
1. **Distribution over product.** A great product no one sees is useless. We obsess over getting in front of the right people.
2. **Data compounds.** Every conversation enriches our talent database. Every campaign makes the next one better.
3. **Automation with approval.** Agents work fast, but external actions need human judgment.
4. **Measure what matters.** If we can't track it, we can't improve it.
5. **Show the work.** We share what we're building, how it works, what we learn. Transparency builds trust.
6. **Stay scrappy.** Ship something imperfect rather than wait for perfect.

---

## What's Next

The team is running:
- **Scout** is publishing SEO content to build organic traffic
- **Zuck** is growing our Facebook community and capturing SMS signups
- **Fleet** is shipping features and fixing bugs
- **Pixel** is auditing user journeys and reducing friction
- **Sigma** is tracking metrics so we know what's working

I'll keep sharing how this evolves. If you're a founder thinking about building an AI team — try it. The tools exist. The cost is low. The upside is huge.

---

*Want to follow along? I post updates on [Twitter/X](https://x.com/sangyh) and this blog.*

*Building something with AI agents? [Reach out](mailto:sangy@rightjoin.co) — I'd love to compare notes.*
