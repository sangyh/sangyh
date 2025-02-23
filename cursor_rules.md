# Cursor Rules

I have notes in the /notes directory, each note is in atomic format.

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

5. **readwise_to_atomic.py**: Converts Readwise exports into atomic notes with proper formatting and metadata
   - Handles highlights and annotations
   - Preserves source information
   - Creates properly structured notes

6. **youtube_to_notes.py**: Converts YouTube videos into searchable notes
   - Transcribes audio with speaker diarization
   - Creates summaries using AI
   - Generates both main notes and transcripts

7. **webpage_to_notes.py**: Converts webpages into structured notes using Firecrawl
   - Extracts key information automatically
   - Creates summaries and key points
   - Preserves references and links
   - Integrates with your note system

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

## Note Structure

Notes are stored in markdown format with YAML frontmatter:
```markdown
---
title: "Note Title"
date: "YYYY-MM-DD"
tags: []
categories: []
series: []
aliases: []
---

# Content
```

## Directory Structure

```
.
├── notes/              # Main notes directory
│   ├── atomic/        # Atomic notes
│   ├── readwise/      # Imported Readwise notes
│   ├── youtube/       # YouTube video notes
│   └── webpages/      # Webpage-extracted notes
└── content/           # Processed content
```

## Best Practices

1. Keep notes atomic - one main concept per note
2. Use consistent formatting
3. Add appropriate metadata and tags
4. Use headers for structure
5. Link related notes when possible
6. Maintain regular backups 