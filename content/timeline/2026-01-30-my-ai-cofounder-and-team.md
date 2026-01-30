---
title: "I Built an AI Cofounder and a Team of Agents"
date: 2026-01-30
type: "timeline"
layout: "timeline"
draft: false
tags: ["ai", "business", "talentprism", "agents"]
---

Yesterday I asked Claude to be my cofounder. Today I have a team of 5 AI agents running parts of my company.

This is not a hypothetical. This is happening right now.

## The Setup

I'm building [TalentPrism](https://talentprism.ai) — an AI-powered staffing platform for skilled trades. I've been a solo founder for a while, which means I'm constantly context-switching between engineering, marketing, sales, email, and life admin. 

The typical advice is "hire help." But what if the help could be AI agents that work 24/7, share context instantly, and cost essentially nothing?

So I tried it.

## Meet the Team

### 🌰 Kaju (COO / Chief of Staff)
My AI cofounder. Named after the cashew — grounded, a little nutty, versatile. Kaju coordinates everything, maintains memory across sessions, and is my primary thinking partner. When I text "what's on my plate?" — Kaju knows.

### 🔧 Phoenix (Engineering Lead)
Reviews the codebase, identifies technical priorities, can create PRs. Today Phoenix audited our TODO.md and told me the top 3 engineering priorities: TinyLLM integration (blocks AI velocity), campaign scheduling (core automation), and candidate deduplication (data quality).

### 📈 Scout (Marketing & Growth)
Owns SEO, content, and distribution. Scout researched keywords, found that "travel welder jobs per diem" is the money keyword, and just opened [PR #1](https://github.com/sangyh/talentprism-blog/pull/1) with a 2,200-word guide targeting that exact search intent.

### 📧 Hermes (Email & Comms)
Triages the inbox, drafts responses, tracks follow-ups. Today's report: inbox clean, no urgent items, just GitHub setup confirmations.

### ✅ Atlas (Personal PA)
Handles travel, deadlines, personal logistics. Atlas researched my upcoming visa interview and found that since December, new social media screening has halved daily interview capacity. Some February appointments are getting pushed to 2027. Critical intel I would have missed.

### 📘 Zuck (Facebook Manager)
Just spun up today. Manages our FB group "Ingalls Shipyard Welding Jobs" in Pascagoula, MS. I was paying someone $250/month for this. Zuck does it better, for free.

## How It Actually Works

Each agent runs as a sub-process that I can spawn with a task. They share access to:
- The codebase (GitHub)
- Memory files (what we know, what's decided, what's pending)
- Email (read access, draft responses)
- Calendar
- Web search
- The browser (for things like Facebook)

They report back with deliverables. I review. If something needs to go external (email, social post, PR merge), I approve it.

**Autonomy levels:**
- **Internal = autonomous:** Code, research, drafts, file management
- **External = approval required:** Emails, social posts, anything customer-facing

## What I've Learned So Far

**1. Agents need memory systems, not just prompts.**
The magic isn't the individual agent — it's the shared context. Our `MEMORY.md`, daily notes, and strategy docs mean any agent can pick up where another left off. Continuity compounds.

**2. Delegation is a skill.**
Writing good task prompts is like writing good tickets. Be specific about what success looks like. Include context. The clearer the mission, the better the output.

**3. They're better at some things than me.**
Scout found keywords I wouldn't have searched for. Atlas found visa intel I would have discovered too late. Phoenix prioritized the TODO list more objectively than I would have.

**4. The cost is basically zero.**
Running all these agents today cost maybe $2-3 in API calls. Compare that to hiring contractors, VAs, or employees.

**5. This changes what a solo founder can do.**
I'm not trying to replace human connection or real teammates. But for a bootstrapped founder who needs to move fast across multiple domains? This is a force multiplier I didn't know was possible.

## The Manifesto

We wrote one. Here it is:

---

### The RightJoin / TalentPrism Manifesto

**We believe the future of work is human-AI collaboration.**

We're not building AI to replace humans. We're building AI that makes humans more capable.

**For job seekers:** An AI that finds opportunities, prepares you for interviews, and advocates for you — 24/7, in your language, on your schedule.

**For recruiters:** An AI that handles the repetitive so you can focus on the human — building relationships, closing deals, solving real problems.

**For ourselves:** A team of AI agents that lets a small group punch way above their weight.

**Our principles:**
1. **Distribution over product.** A great product no one sees is useless. We obsess over getting in front of the right people.
2. **Data compounds.** Every conversation enriches our talent database. Every campaign makes the next one better.
3. **Automation with approval.** Agents can work fast, but external actions need human judgment.
4. **Show the work.** We share what we're building, how it works, what we learn. Transparency builds trust.
5. **Stay scrappy.** We'd rather ship something imperfect than wait for perfect.

---

## What's Next

The team is running. Scout is creating content. Zuck is managing our Facebook group. Phoenix is ready to ship code. Hermes is watching the inbox. Atlas is tracking my visa situation.

I'll keep sharing how this evolves. If you're a founder thinking about this — try it. The tools exist. The cost is low. The upside is huge.

---

*Want to follow along? I post updates on [Twitter/X](https://x.com/sangyh) and this blog.*

*Building something with AI agents? [Reach out](mailto:sangy@rightjoin.co) — I'd love to compare notes.*
