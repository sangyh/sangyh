---
author: "Sangy"
title: "Omni-channel recruiting agents"
draft: false
date: "2025-10-14"
description: "Designing multi-agent architecture for recruiting"
tags: ["product"]
categories: ["talentprism"]
series: ["talentprism"]
aliases: []
cover:
  image: 
  caption: 
---

The key principle of a recruiting chatbot, agnostic of channel is that it should *Lead the conversation* - this is not a customer service bot. For example, it should guide the candidate from identifying their intent - looking for a job vs status update, to guiding them through the website, as well as enriching their profile to establish future contact channels.

What are the requirements?
1. Identify the user- gather name and contact details

2. If they wish to save their profile or retrive a previous interaction- use  phone no or email to OTP verify. Authenticated user experience should be noticably better than the guest experience. 

3. If they are looking for a job -enable resume upload. This will call the resume parser to perosnalize messages, but also in the background match them to open jobs. 

4. If there are matches - share urls and persist session across pages. Matches can be based semantic search or simple agentic grep+thinking patterns like coding agents. maybe latter is faster and more accurate than semantic search. 

5. If there are no matches - gather preferences and enroll them into job alerts. 

6. Voice experience if desired

7. Save and reload interactions from memory when they return

8. strive for upsell goals like gather referrals, feedback on user experience 

9. when doing outbound campaigns - have a leading message template for the job being advertised but still maintain 

10. regular chat interactions like answer questions about the company or the job based on job description