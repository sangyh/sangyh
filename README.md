# Personal Website & Note-Taking System

A Hugo-based personal website with integrated note-taking system that features both a chronological timeline for shorter thoughts and a separate section for longer articles.

## Features

- **Dual Content Structure**: Separate sections for timeline entries (short thoughts, resources) and longer articles
- **Chronological Timeline**: A visually appealing timeline view for shorter notes and resources
- **Article Repository**: Organized collection of longer, more structured content
- **Custom Homepage**: Showcases both timeline entries and articles
- **Note Creation Tools**: Command-line tools for quickly creating different types of content

## Tools Overview

### 1. Note Creation (`new_note.py` / `new_note.sh`)
Creates new notes of different types with proper formatting and metadata.

```bash
# Using the Python script directly
python new_note.py [--type TYPE] "Note Title"

# Using the shell script
./new_note.sh [--type TYPE] "Note Title"

# Using aliases (after setup)
note "Your Atomic Note Title"      # Creates a note in the notes/ directory
tnote "Your Timeline Note Title"   # Creates a note in the content/notes/ directory
article "Your Article Title"       # Creates an article in the content/posts/ directory
```

Types:
- `atomic`: Personal knowledge notes (default)
- `timeline`: Short thoughts and resources for the timeline
- `article`: Longer, structured content for the articles section

### 2. Format Transcript (`format_transcript.py`)
Formats raw text into a structured markdown note with proper metadata.

```bash
python format_transcript.py <input_file>
```

### 3. Split into Atomic Notes (`plan_to_split_atomic.py`)
Splits a long text file into multiple atomic notes based on headers.

```bash
python plan_to_split_atomic.py <input_file>
```

### 4. Enhanced Search (`enhanced_search.py`)
Performs multi-modal search across notes using exact, fuzzy, and semantic matching.

```bash
python enhanced_search.py <query> [mode]
```

Modes: all, exact, fuzzy, semantic

### 5. Search CLI (`search_cli.py`)
A user-friendly command-line interface for searching through notes.

```bash
python search_cli.py [query] [-m MODE] [--preview]
```

Options:
- `-m, --mode`: Search mode (all, exact, fuzzy, semantic)
- `--preview`: Show preview of matched files
- Without query: enters interactive mode

### 6. YouTube to Notes (`youtube_to_notes.py`)
Converts YouTube videos into searchable notes.

```bash
python youtube_to_notes.py <youtube_url>
```

### 7. Webpage to Notes (`webpage_to_notes.py`)
Converts webpages into structured notes using Firecrawl.

```bash
python webpage_to_notes.py <webpage_url>
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up the note creation aliases:
```bash
chmod +x setup_note_alias.sh
./setup_note_alias.sh
source ~/.zshrc  # or ~/.bashrc
```

## Content Types

### Atomic Notes
- Stored in the `/notes` directory
- Simple format with title and content
- Used for personal knowledge management

### Timeline Notes
- Stored in the `/content/notes` directory
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
type: "note"
layout: "note"
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
├── notes/              # Atomic notes directory
├── content/            # Hugo content directory
│   ├── notes/          # Timeline notes
│   └── posts/          # Articles by category
├── layouts/            # Custom Hugo layouts
│   └── _default/       # Layout templates
├── assets/             # CSS and other assets
│   └── css/extended/   # Custom CSS
├── new_note.py         # Note creation script
├── new_note.sh         # Shell wrapper for note creation
├── setup_note_alias.sh # Script to set up aliases
└── other tools...      # Other note management tools
```

## Website Features

- **Custom Homepage**: Shows both timeline entries and articles
- **Timeline View**: Chronological display of shorter notes
- **Article Section**: Organized by categories
- **Responsive Design**: Works well on all devices
- **Tag Support**: Content organized by tags
- **Search Functionality**: Find content easily

## Best Practices

1. Keep notes atomic - one main concept per note
2. Use consistent formatting
3. Add appropriate metadata and tags
4. Use headers for structure
5. Link related notes when possible
6. Maintain regular backups
7. Use the appropriate note type for your content:
   - Use timeline notes for shorter thoughts and resources
   - Use articles for longer, more structured content
   - Use atomic notes for personal knowledge management
