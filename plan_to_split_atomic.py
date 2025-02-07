#!/usr/bin/env python3

import sys
import re
from pathlib import Path
from datetime import datetime

def extract_sections(text):
    """Split text into sections based on headers."""
    # Split on markdown headers (## or #)
    sections = re.split(r'\n(?=#{1,2}\s)', text)
    return [s.strip() for s in sections if s.strip()]

def create_atomic_note(content, index, source_file):
    """Create an atomic note with proper metadata."""
    # Extract title from first line (header)
    title_match = re.match(r'#{1,2}\s+(.+)', content.split('\n')[0])
    title = title_match.group(1) if title_match else f"Note {index}"
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    source_name = source_file.stem
    
    note = f"""---
author: "Sangy"
title: "{title}"
draft: false
date: "{timestamp}"
description: "Split from {source_name}"
tags: ["atomic"]
categories: []
series: []
aliases: []
cover:
  image: 
  caption:
---

{content}

---
Source: {source_file.name}
"""
    return note, re.sub(r'[^\w\s-]', '', title.replace(' ', '-'))

def split_into_atomic_notes(input_file):
    """Split a text file into multiple atomic notes."""
    text = input_file.read_text()
    sections = extract_sections(text)
    
    output_dir = Path('content/posts/atomic')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    created_files = []
    for i, section in enumerate(sections, 1):
        note_content, title = create_atomic_note(section, i, input_file)
        output_file = output_dir / f"{title}.md"
        output_file.write_text(note_content)
        created_files.append(output_file)
    
    return created_files

def main():
    if len(sys.argv) != 2:
        print("Usage: plan_to_split_atomic.py <input_file>")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)
    
    created_files = split_into_atomic_notes(input_file)
    print(f"Created {len(created_files)} atomic notes:")
    for file in created_files:
        print(f"- {file}")

if __name__ == "__main__":
    main()
