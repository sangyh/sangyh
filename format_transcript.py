#!/usr/bin/env python3

import sys
import re
from pathlib import Path
from datetime import datetime

def format_title(text):
    """Convert text to title case and clean it for filename use."""
    return re.sub(r'[^\w\s-]', '', text.title().replace(' ', '-'))

def format_transcript(text):
    """Format raw text into a structured markdown document."""
    lines = text.strip().split('\n')
    
    # Extract or create title from first non-empty line
    title = next((line for line in lines if line.strip()), "Untitled Note")
    
    # Create metadata
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    formatted = f"""---
author: "Sangy Hanumasagar"
title: "{title}"
draft: false
date: "{timestamp}"
description: ""
tags: []
categories: []
series: []
aliases: []
cover:
  image: 
  caption:
---

"""
    
    # Add content with proper markdown formatting
    content_lines = [line for line in lines if line.strip() and line.strip() != title]
    formatted += "\n".join(content_lines)
    
    return formatted, format_title(title)

def main():
    if len(sys.argv) != 2:
        print("Usage: format_transcript.py <input_file>")
        sys.exit(1)
        
    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)
        
    # Read and format content
    text = input_file.read_text()
    formatted_content, title = format_transcript(text)
    
    # Create output file
    output_file = Path('content/posts') / f"{title}.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(formatted_content)
    print(f"Created formatted note: {output_file}")

if __name__ == "__main__":
    main()
