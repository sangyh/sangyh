---
title: "Exploring MCP"
date: 2025-03-16 01:32:45
type: "timeline"
layout: "timeline"
draft: false
tags: []
---
_"MCP is an open protocol that standardizes how applications provide context to LLMs"_

The user workflow in the MCP world is a good UX primitive to explore. i'm capturing some interesting early finds here.

- Hosts, Servers, Clients
    - Hosts are user applications that host the clients like AI tools. these clients will talk to servers to perform the required actions
    - servers can be local data sources, web apis, browser etc. with acces to resources, prompts and tools.
    - This is an informative 10min video https://x.com/mckaywrigley/status/1898109392341385509

- user creates a "space" or a server. the server is a virtual session with access to a set of tools like browser, database, linkedin, email etc.
- they interact with the AI agent in a chat-interface and ask it to do things. 
    - this demo is a great example - https://x.com/Karmedge/status/1899825488379392333. he has a private server with access to his apollo, linkedin, email etc. he shares a linkedin post, asks to fetch details of people who commented, get their emials, write personalined emails. 


