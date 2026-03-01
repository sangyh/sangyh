---
author: "Sangy"
title: "My AI agent found a bug, researched the fix, and shipped a PR while I slept"
draft: true
date: "2026-03-01"
description: "How an autonomous AI coding agent went from spotting a UX issue in interview recordings to shipping a multi-layered fix with 20 tests"
tags: ["product", "ai-agents", "voice-ai"]
categories: ["talentprism"]
series: ["talentprism"]
aliases: []
cover:
  image: 
  caption: 
---

I woke up to a PR notification this morning. My AI agent, Kaju, had found a bug in our voice interview system, researched the root cause, and shipped a fix — all without me.

Here's how that happened.

## The signal

TalentPrism runs AI voice interviews for recruiting. Candidates call in, talk to an AI, and we collect structured data for recruiters.

Kaju does routine quality reviews of interview transcripts. During one of these reviews, he flagged something in a candidate's second attempt: mid-conversation, the candidate said "Hello?" — the universal sign for "I think the call dropped."

That's a problem. If candidates think the line went dead, they hang up. You lose the interview. You lose the data. Worst case, you lose the candidate.

## From signal to investigation

Kaju filed a GitHub issue, tagged it P2, and started digging. The question was simple: why is there a silence gap long enough for a candidate to think nobody's there?

Three possible causes:
1. LLM inference latency (thinking too long before responding)
2. TTS generation delay (text-to-speech taking too long)
3. False endpointing (AI thinks the candidate stopped talking when they didn't — ambient noise triggers this)

## The fix: not one thing, four things

What I liked about the solution is that it wasn't a single tweak. Kaju identified that the real answer was layered:

**Backchannel responses.** Enable VAPI's backchannel feature so the AI produces small acknowledgments — "uh-huh", "I see" — while the candidate is speaking. Even if there's processing time, the candidate never hears dead silence. This is how humans work. We nod. We go "mmhmm." The absence of that in AI calls is what feels robotic.

**Background denoising.** Without noise filtering, ambient sounds (traffic, TV, job site noise) were causing false endpointing. The AI would think the candidate stopped talking, pause to formulate a response, then realize — oh wait, they're still going. That back-and-forth creates the exact kind of awkward silence that makes people say "Hello?"

**Lower input sensitivity.** Reduced the minimum characters needed before the AI starts processing. Faster trigger, faster response.

**Latency monitoring.** This is the one that matters long-term. The PR adds p50/p90/p95 latency tracking extracted from VAPI's end-of-call reports, stored on every call record. So now we can actually *see* latency trends instead of discovering problems when candidates start hanging up.

## The meta-point

The total PR: 6 files changed meaningfully, 2 migrations, 20 tests, admin panel updates so we can toggle everything per-assistant.

But the interesting part isn't the code. It's the loop:

1. Agent reviews interview quality (routine task)
2. Spots anomaly in transcript (pattern recognition)
3. Files issue with context (documentation)
4. Researches root cause across multiple possible explanations (investigation)
5. Implements layered fix addressing immediate UX + long-term observability (engineering)
6. Ships PR with tests (execution)

No human in the loop until the PR notification hit my inbox.

I've been thinking a lot about what AI agents are actually good for. Not the hype-cycle "AGI will replace all jobs" stuff — the practical, boring, compounding stuff. An agent that reviews transcripts every day will catch things you won't. Not because it's smarter. Because it doesn't skip days. It doesn't get bored of reading transcripts. It doesn't think "eh, one candidate said Hello, probably fine."

The compound effect of an agent that shows up every single day and pays attention is wild. This bug could've gone unnoticed for weeks. How many candidates would've hung up thinking the call dropped? How much data would we have lost?

## What I'd change

The PR builds are currently failing — CI caught some issues. So it's not a perfect autonomous loop yet. The agent can identify, research, and implement, but the "ship to production without breaking anything" part still needs human review.

Honestly? That's probably the right boundary for now. I want the agent doing 90% of the work autonomously and flagging me for the last 10%. That's a very different job than doing 100% of it myself.

---

*If you're building voice AI applications, the backchannel + denoising combo is worth looking into. It's a small config change that meaningfully changes how candidates perceive call quality. The latency monitoring is table stakes — you should've been tracking this from day one (I wasn't).*
