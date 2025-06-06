---
author: "Sangy"
title: "Building realistic voice interactions with voice AI"
draft: false
date: "2025-04-23"
description: "Parameters to improving voice AI conversations"
tags: ["llms", "voice-ai"]
categories: ["LLM"]
series: []
aliases: []
cover:
  image: 
  caption: 
---

## Content

Messy. A lot of parameters to tune to cater to a variety of end user conversation styles.

Here is some of the settings I added to Talentprism to lend more control over AI behavior to the users.

### Personality of the interviewer
LLM model - this is the biggest factor the determines personality.  llama models are more verbose and friendly, the open AI and google models is more succinct but speak more when needed. I would recommend trying the google models (flash 2.0)  
Temperature - recommend around 0.7-1 for sufficient randomness in AI responses.  
AI Voice - recommend trying Paige or Ana for a very realistic natural voice  

### Reduce interruptions
Start Speaking Delay -Default is 0.4 secs.  If the user is a slow speaker, increase this to 0.6 seconds. This induces a delay in every AI response (like 2 slow speakers talking to each other).  

### Handle Interruptions
Interruption Sensitivity (default 0.2 sec) and Speech Backoff Time (default 1 sec) - If candidate and AI speak at the same time, the AI stops after 0.2 sec and waits for 1 sec before responding.  

### Extended silence
Idle Timeout (default 10 sec) - if the candidate is silent for certain duration, the AI will say "are you still there" & "prolonged silence will"  
Silence Timeout is when the call will disconnect. default is 30 sec.  

### Other configurations
You can edit other config like the first and last  AI response when the call starts and ends, max call duration, audio or video call,  welcome message, etc.

