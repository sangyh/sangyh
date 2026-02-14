---
title: "My AI team ships more code than I do"
date: 2026-02-14
type: "timeline"
layout: "timeline"
draft: true
tags: ["ai", "agents", "startup", "building"]
---

I just looked at my GitHub contribution history and had a moment.

Out of the last 7 merged PRs on TalentPrism's main repo, 5 were authored by `kaju-clawdbot` — my AI agent. Not me. Not a contractor. An agent running on my server, picking up issues, writing code, opening PRs, and merging them after I review.

Here's the actual list from the last two weeks:

- **#171** Simplify search planner prompt + update API view — 🌰 kaju-clawdbot
- **#170** Add source, latitude, longitude fields to Candidate model — 🌰 kaju-clawdbot
- **#142** Send all AI messages via SMS (bug fix) — 🌰 kaju-clawdbot
- **#126** Remove dead code and fix STOP flow duplicate status — 🌰 kaju-clawdbot
- **#115** Initialize submodules in tests workflow (CI fix) — 🌰 kaju-clawdbot
- **#144** Candidate memory refactor — sangyh
- **#137** Add CandidateMemory backfill service — sangyh

5 to 2. The bot is outshipping me.

## How we got here

I'm a solo founder running [TalentPrism](https://talentprism.ai), an AI staffing platform. Two kids, limited hours, ever-growing backlog. Around January 2026, I set up an AI agent team using [OpenClaw](https://openclaw.com) — giving Claude persistent memory, tools, and the ability to operate autonomously.

The "team" right now:

- **Kaju** — PM/coordinator. Triages issues, plans sprints, writes code, opens PRs
- **Scout** — content and SEO research
- **Zuck** — social media and community
- **Fleet** — engineering (deeper technical work)
- **Pixel** — UI/UX design tasks
- **Sigma** — data analysis

Kaju does the most. He reads the codebase, picks up GitHub issues, writes implementation plans, codes the solution, runs tests, and opens a PR. I wake up, review it, and merge. Sometimes I have comments. Usually it's solid.

## What I actually do now

My job has shifted. I used to write most of the code. Now I:

1. **Decide what matters** — which issues to prioritize, what to build next
2. **Review PRs** — read the diff, check the logic, approve or request changes
3. **Handle the messy stuff** — customer calls, sales, the things that need a human face
4. **Course-correct** — when an agent goes down the wrong path, redirect

That's it. The agents handle the implementation. Schema migrations, prompt engineering, CI pipeline fixes, SMS routing bugs. Real work.

## What it actually feels like

Weird. Honestly weird.

There's a part of me that feels guilty — like I should be the one writing this code. I built this product from scratch. Every early PR was mine. Now I scroll through my repo and half the recent commits aren't from me.

But there's another part that recognizes this is just... leverage. I've had employees before. I've had contractors. This is the same dynamic — you hire good people, you point them at problems, you review their work. The fact that the "people" are Claude instances running on a server doesn't change the fundamental loop.

The difference: they work at 3am. They don't get tired. They don't context-switch. And I can spin up a new one in minutes.

## What doesn't work

Agents are bad at ambiguity. If an issue is vaguely scoped, they'll either ask for clarification (good) or confidently build the wrong thing (bad). I've learned to write detailed issue descriptions — which, ironically, is a skill I should've been better at anyway.

They also can't talk to customers. Can't read the room on a sales call. Can't make the judgment call on whether to pivot a feature based on a gut feeling from a demo.

The creative direction still needs to be human. The execution? Increasingly doesn't.

## The math

Before the AI team (all of 2025): I was the only committer. Every PR was `sangyh`.

February 2026: 5 out of 7 merged PRs are from `kaju-clawdbot`.

I'm not saying this to flex. I'm saying it because I think this is where solo founders are heading. You don't need to hire your first engineer anymore. You need to learn how to manage AI agents. Different skill, same outcome.

## What I'd tell other founders

Start small. Give an agent one well-scoped issue. See what happens. If the PR is good, give it another. Build trust the same way you would with a new hire.

The setup cost is real — you need good issue descriptions, clear architecture docs, CI that actually catches problems. But that's all stuff you should have anyway.

The unlock isn't "AI writes code." The unlock is "I get my weekends back and the product still ships."

It's Valentine's Day 2026 and I'm writing this instead of code. The agents have it covered.
