# Cursor Rules

I have notes in the /drafts directory, each note is in atomic format.

## Available Tools

You have several tools at your disposal:

1. **format_transcript.py**: Formats text nicely into a markdown file
   - Adds proper YAML frontmatter
   - Creates consistent formatting
   - Handles metadata automatically

2. **plan_to_split_atomic.py**: Splits a long text file into atomic notes
   - Creates individual notes for each concept
   - Maintains proper linking and references
   - Preserves metadata across splits

3. **enhanced_search.py**: Performs multi-modal search (exact, fuzzy, and semantic) across notes and sources
   - Supports multiple search modes
   - Includes metadata search
   - Provides context in results

4. **search_cli.py**: Command-line interface for enhanced_search.py, making it easier to search through notes
   - User-friendly interface
   - Preview functionality
   - Rich text output

5. **youtube_to_notes.py**: Converts YouTube videos into searchable notes
   - Transcribes audio with speaker diarization
   - Creates summaries using AI
   - Generates both main notes and transcripts

6. **webpage_to_notes.py**: Converts webpages into structured notes using Firecrawl
   - Extracts key information automatically
   - Creates summaries and key points
   - Preserves references and links
   - Integrates with your note system

7. **new_note.py/new_note.sh**: Creates new notes quickly
   - Generates properly formatted note files
   - Opens the note in your default editor
   - Handles duplicate filenames automatically
   - Can be used via shell script shortcut
   - Supports multiple note types:
     - `atomic`: Creates notes in the /drafts directory (default)
     - `timeline`: Creates timeline notes in the content/timeline directory
     - `article`: Creates longer articles in the content/posts directory

## Usage Guidelines

If I ask you to do a task, you should:

1. First determine if the task is possible with the tools you have
2. If it is, use the appropriate tool
3. If possible to do without a tool, proceed directly
4. If a new tool is needed, suggest it with a plan

For comprehensive searches:
- Use enhanced_search.py first for quick results
- Fall back to manual search if needed
- Consider using multiple search modes

## Note Types

### Atomic Notes
- Stored in the `/drafts` directory
- Simple format with title and content
- Used for personal knowledge management

### Timeline Notes
- Stored in the `/content/timeline` directory
- Displayed in a chronological timeline on the website
- Used for shorter thoughts, resources, and discoveries
- Created with: `new_note.py --type timeline "Note Title"` or `tnote "Note Title"`

### Articles
- Stored in the `/content/posts/{category}` directory
- Used for longer, more structured content
- Displayed in the articles section of the website
- Created with: `new_note.py --type article "Article Title"` or `article "Article Title"`

## Note Structure

Notes are stored in markdown format with appropriate frontmatter based on type:

### Atomic Notes
```markdown
# Note Title

Created: YYYY-MM-DD HH:MM:SS

## Content
```

### Timeline Notes
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
```

### Articles
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
```

## Directory Structure

```
.
├── drafts/              # Atomic notes directory
├── content/            # Hugo content directory
│   ├── timeline/       # Timeline notes
│   └── posts/          # Articles by category
└── assets/             # CSS and other assets
```

## Best Practices

1. Keep notes atomic - one main concept per note
2. Use consistent formatting
3. Add appropriate metadata and tags
4. Use headers for structure
5. Link related notes when possible
6. Maintain regular backups 