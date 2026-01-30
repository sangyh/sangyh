---
author: "Sangy"
title: "AgentLens: The Tool I Wish Existed"
draft: false
date: "2026-02-03"
description: "A product idea for context capture that makes AI agents actually useful for UX"
tags: ["product", "ai-agents", "ux"]
categories: ["product"]
series: []
aliases: []
cover:
  image: 
  caption: 
---

I've been thinking about the gap between what AI agents *can* do and what they actually *see*.

## The Problem

AI agents are incredibly good at reasoning about UX, support issues, and user flows. But getting the right context into their prompts? Manual and messy.

**What agents need to be useful:**
- Screenshot (what does the user see?)
- DOM state (what's clickable?)
- Action history (what did they just do?)
- Timing (where did they hesitate?)

**What exists today:**
- Playwright/Puppeteer = raw screenshots + full DOM (too noisy, dev-only)
- Hotjar/FullStory = session recordings (for humans, not AI)
- Browser agents (Skyvern, etc.) = capture their own actions, not arbitrary sessions

**The gap:** No clean way to package browser context for AI agent consumption.

---

## What I Wish Existed

A **"Context Packager for AI Agents"** — something that captures user sessions and packages them into agent-ready prompts with the right amount of context. Not too much (token limits). Not too little (missing info).

### Two Form Factors

**1. Chrome Extension (for non-technical folks)**

UX researchers, QA contractors, support agents, PMs — anyone who needs to capture user flows.

- Install extension
- Click "Start Recording" on any website
- Do the flow (click, scroll, type, hesitate)
- Click "Stop"
- Get shareable output: annotated screenshots, action timeline, agent-ready prompt blob

Why an extension? No integration needed. Works on any website (including competitors!). Non-technical users can capture. Instant distribution via Chrome Web Store.

**2. SDK (for developers)**

For product teams embedding capture in their own apps:

```javascript
import { AgentLens } from 'agentlens';

AgentLens.init({ 
  captureOn: 'error' | 'support-click' | 'always',
  mask: ['input[type=password]', '.sensitive'],
});

const context = AgentLens.getContext();
// → { screenshot, elements, actions, timing }
```

Real-time support integration. Trigger captures programmatically. Deeper integration for on-prem and privacy-sensitive deployments.

---

## The Magic: Smart Compression

The real value is fitting meaningful context into 8-32k tokens.

**Screenshot handling:** Capture at key moments (click, error, hesitation). Annotate with element labels. Compress to optimal resolution for vision models.

**DOM compression:** Not full DOM (way too big). Extract interactive elements only. Semantic labels ("Login button", "Email field"). Include state (disabled, selected, error).

**Action timeline:**
```
0.0s  → Page load (screenshot 1)
2.3s  → Click "Create Campaign" 
8.1s  → Hesitation (5.6s pause) ⚠️
8.1s  → Click "Need help?" tooltip
12.4s → Fill "Campaign Name" field
```

---

## Use Cases

| Use Case | Output |
|----------|--------|
| **UX Audit** | "Here's where users get stuck" |
| **Support** | "User is on step 3, seeing error X" |
| **User Testing** | Structured findings report |
| **Competitive Analysis** | "Their checkout is 3 fewer clicks" |

---

## Why This Is Hard (and why it doesn't exist yet)

1. **Compression quality** — fit useful context in token limits
2. **Annotation accuracy** — semantic labels, not just CSS selectors
3. **Privacy** — auto-mask sensitive data (PII, passwords)
4. **Speed** — real-time for support use cases
5. **Cross-browser** — consistent capture across Chrome, Safari, Firefox

---

## The Positioning

**"Loom for AI agents"** or **"Hotjar → AI pipeline"**

Hotjar captures sessions for humans to watch. This captures sessions for AI to reason about.

---

If you're building something like this or want to jam on the idea, hit me up.

