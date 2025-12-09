---
author: "Sangy"
title: "Note Taking System Guide"
draft: false
date: "2025-03-21"
description: "A comprehensive guide to my personal note-taking and blog system with shortcuts and tools"
tags: ["productivity", "notes"]
categories: ["productivity"]
series: []
aliases: []
cover:
  image: 
  caption: 
---

# Note Taking System Guide

## Introduction

Managing personal knowledge and content effectively requires a well-structured system. Over time, I've developed a custom note-taking setup that integrates with my Hugo-based website. This system allows me to create and maintain three types of content: atomic notes for personal knowledge, timeline entries for short thoughts, and longer articles for in-depth exploration of topics.

In this guide, I'll share how I've set up my system and how you might adapt it for your own use.

## The Three Types of Notes

My system is built around three distinct note types, each with its own purpose and formatting:

### 1. Atomic Notes

These are the foundation of my personal knowledge management system. Each atomic note captures a single concept, making it easy to link and combine ideas. They're stored in a private `/drafts` directory and aren't published to the web.

**Key characteristics:**
- Simple, distraction-free format
- Focus on a single idea or concept
- Great for capturing thoughts quickly
- Easily linkable to other notes

### 2. Timeline Notes

Timeline notes appear in chronological order on my website's timeline section. They're perfect for sharing shorter thoughts, interesting resources I've found, or brief updates.

**Key characteristics:**
- Displayed chronologically on the website
- Short-form content
- Includes proper Hugo frontmatter
- Great for quick sharing of ideas and discoveries

### 3. Articles

These are longer, more structured pieces of content organized by category. Articles go through a more thorough editorial process before publication and represent more complete thoughts.

**Key characteristics:**
- Organized by category
- More structured with introduction, sections, and conclusion
- Contains comprehensive metadata
- Includes cover images and proper SEO elements

## Command Shortcuts

To make creating these different types of notes effortless, I've set up these command-line shortcuts:

1. **For Atomic Notes**:
   ```bash
   note "Your Atomic Note Title"
   ```
   Creates a simple note in the `/drafts` directory.

2. **For Timeline Notes**:
   ```bash
   tnote "Your Timeline Note Title"
   ```
   Creates a note in the `/content/timeline` directory with proper Hugo frontmatter.

3. **For Articles**:
   ```bash
   article "Your Article Title"
   ```
   Creates an article in the `/content/posts/{category}` directory, prompting for the category.

## Note Templates

Each note type has its own template structure:

### Atomic Note Template

```markdown
# Note Title

Created: YYYY-MM-DD HH:MM:SS

## Content

Your content here...
```

### Timeline Note Template

```markdown
---
title: "Note Title"
date: YYYY-MM-DD HH:MM:SS
type: "timeline"
layout: "timeline"
draft: false
tags: []
---

# Content

Your content here...
```

### Article Template

```markdown
---
author: "Sangy"
title: "Article Title"
draft: true
date: "YYYY-MM-DD"
description: ""
tags: []
categories: []
series: []
aliases: []
cover:
  image: 
  caption: 
---

# Content

## Introduction

Your introduction here...
```

## Additional Tools in My System

Beyond the basic note creation, I've developed several tools to enhance my workflow:

### Content Processing Tools

- **Format Transcript**: `python format_transcript.py <input_file>` - Takes raw text (like interview transcripts) and formats it into a structured markdown note with proper metadata.

- **Split into Atomic Notes**: `python plan_to_split_atomic.py <input_file>` - Intelligently splits a longer document into multiple atomic notes based on headers or content sections.

### Search Tools

Finding information quickly in your notes is crucial for any PKM system:

- **Enhanced Search**: `python enhanced_search.py <query> [mode]` - Multi-modal search across notes using exact, fuzzy, and semantic matching, helping find content even when you don't remember the exact wording.

- **Search CLI**: `python search_cli.py [query] [-m MODE] [--preview]` - A user-friendly command-line interface that makes searching through notes more intuitive.

### Content Import Tools

These tools help bring external content into my note system:

- **YouTube to Notes**: `python youtube_to_notes.py <youtube_url>` - Extracts content from YouTube videos (transcripts, metadata) and converts them into searchable notes.

- **Webpage to Notes**: `python webpage_to_notes.py <webpage_url>` - Uses Firecrawl to convert webpages into structured notes, preserving the important content while removing unnecessary elements.

## Best Practices

Through years of refining this system, I've developed these best practices:

1. **Keep notes atomic** - Focus on one main concept per note
2. **Use consistent formatting** - Makes processing and searching easier
3. **Add appropriate metadata and tags** - Improves searchability and organization
4. **Use headers for structure** - Makes longer content more scannable
5. **Link related notes when possible** - Creates a web of knowledge
6. **Maintain regular backups** - Protects your knowledge base
7. **Use the appropriate note type for your content**:
   - Timeline notes for shorter thoughts and resources
   - Articles for longer, more structured content
   - Atomic notes for personal knowledge management

## Conclusion

A good note-taking system should fade into the background, making it effortless to capture and retrieve information. The combination of different note types, custom shortcuts, and specialized tools has made my system both powerful and easy to use.

By sharing this system, I hope to inspire others to develop their own approach to personal knowledge management that aligns with their unique workflows and needs.

If you have questions about implementing a similar system or want to share your own approach, feel free to reach out!