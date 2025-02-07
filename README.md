# Personal Note-Taking System

A collection of tools for managing and searching through a personal knowledge base of atomic notes.

## Tools Overview

### 1. Format Transcript (`format_transcript.py`)
Formats raw text into a structured markdown note with proper metadata.

```bash
python format_transcript.py <input_file>
```

### 2. Split into Atomic Notes (`plan_to_split_atomic.py`)
Splits a long text file into multiple atomic notes based on headers.

```bash
python plan_to_split_atomic.py <input_file>
```

### 3. Enhanced Search (`enhanced_search.py`)
Performs multi-modal search across notes using exact and fuzzy matching.

```bash
python enhanced_search.py <query> [mode]
```

Modes: all, exact, fuzzy

### 4. Search CLI (`search_cli.py`)
A user-friendly command-line interface for searching through notes.

```bash
python search_cli.py [query] [-m MODE] [--preview]
```

Options:
- `-m, --mode`: Search mode (all, exact, fuzzy)
- `--preview`: Show preview of matched files
- Without query: enters interactive mode

### 5. Readwise to Atomic (`readwise_to_atomic.py`)
Converts Readwise exports into atomic notes with proper formatting and metadata.

```bash
python readwise_to_atomic.py <readwise_export.json>
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Note Structure

Notes are stored in markdown format with YAML frontmatter for metadata:

```markdown
---
title: "Note Title"
date: "2024-01-01 12:00:00"
tags: []
---

# Note Title

Content goes here...
```

## Directory Structure

```
.
├── notes/              # Main notes directory
│   ├── atomic/        # Atomic notes
│   └── readwise/      # Imported Readwise notes
├── format_transcript.py
├── plan_to_split_atomic.py
├── enhanced_search.py
├── search_cli.py
├── readwise_to_atomic.py
└── requirements.txt
```

## Features

- Markdown-based note format with YAML frontmatter
- Automatic metadata generation
- Multi-modal search (exact and fuzzy matching)
- Interactive search interface
- Readwise import support
- Atomic note generation from longer content
- Rich CLI output with previews

## Best Practices

1. Keep notes atomic - one main concept per note
2. Use consistent formatting
3. Add appropriate metadata and tags
4. Use headers for structure
5. Link related notes when possible
6. Regular backups of your notes directory
