---
title: "MCP Deepdive"
date: "2025-04-02"
draft: false
tags: ["AI", "MCP", "Protocol", "LangChain"]
description: "A deep dive into the Model Control Protocol (MCP), exploring its architecture, key components, and real-world applications"
author: "Sangy"
categories: ["AI", "Development"]
series: ["MCP"]
aliases: ["/mcp-guide", "/model-control-protocol"]
cover:
  image: 
  caption: "MCP Architecture Overview"
---

MCP is an open protocol that revolutionizes how AI applications and agents interact with tools and data sources. Let's dive into what makes it special.

![MCP Architecture Diagram](/images/mcp-deep-dive.png)

MCP's architecture consists of two main components:
- **Clients**: These host AI applications
- **Servers**: Provide federated access to systems and tools relevant to specific tasks

## Key Components

MCP operates through three primary mechanisms:

1. **Tools** (Model Controlled)
   - Controlled by the model
   - Model decides when to invoke functions to take actions

2. **Resources** (Application Controlled)
   - Represents data exposed to applications
   - Includes files, databases, and other data sources

3. **Prompts** (User Controlled)
   - User invokes prompt templates (e.g., slash commands)

## What Makes MCP Special?

- **Dynamic Nature**: Resources and prompts can be dynamic, allowing applications to subscribe to them. When changes occur, the application gets notified to take follow-up actions.

- **Context Management**: MCP's vision extends beyond just providing context to the LLM - it's about what context is given to the application itself.

- **Agent Framework Integration**: While agent frameworks design how the LLM performs in a loop and determine context usage, MCP protocol facilitates bringing that context to the LLM.

## Real-World Applications

Several exciting implementations and tools have emerged:

- **Zapper MCP**: Bringing new capabilities to the ecosystem
- **Remote MCP**: Extending functionality across distributed systems
- **MCP Think Tool**: Enhancing thinking capabilities
- **MCP Inspector**: Testing MCP servers

## MCPDoc Server

A notable implementation by LangChain that:
- Provides MCP host applications (like Cursor, Windsurf, Claude Code/Desktop) with:
  1. User-defined list of llms.txt files
  2. Simple fetch_docs tool to read URLs within provided llms.txt files
- Enables audit capabilities for tool calls and returned context
- Can be used with tools like `llmstxt_architect` for creating llms.txt files

---

This protocol represents a significant step forward in AI application integration, offering a structured way to manage model-tool interactions while maintaining flexibility and control across different components of the system. 


[update - 4/2/25]
The easiest way to build an MCP Server using 
@GoogleDeepMind

1. Use Gitingest to get all the code and docs from the FastMCP repo
2. Download the code into a txt file
3. Go to AI Studio, upload the file, define what kind of MCP Server you want to build
4. Gemini 2.5 Pro builds it for you.

- https://x.com/_philschmid/status/1912497457444896991


[update]
Highly recommended by [Neils Rogge](https://x.com/NielsRogge) "MCP crash course for Python developers"  - https://x.com/NielsRogge/status/1913679695192670392?t=dC5024fM34pHDzuUdmfYSg&s=08