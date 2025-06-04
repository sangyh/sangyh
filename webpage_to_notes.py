#!/usr/bin/env python3

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field
from firecrawl import FirecrawlApp

class ExtractSchema(BaseModel):
    title: str = Field(description="The title of the webpage")
    summary: str = Field(description="A comprehensive summary of the webpage content")
    key_points: List[str] = Field(description="Key points extracted from the webpage")
    references: List[str] = Field(description="Any references or links mentioned in the webpage")

def create_note(url: str, extracted_data: dict) -> tuple[str, str]:
    """Format extracted data into a structured markdown document."""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    # Create metadata
    formatted = f"""---
author: "Sangy Hanumasagar"
title: "{extracted_data['title']}"
draft: false
date: "{timestamp}"
description: "Notes extracted from webpage using Firecrawl"
tags: ["webpage", "notes", "firecrawl"]
categories: ["web-research"]
series: []
aliases: []
cover:
  image: 
  caption:
---

## Source
{url}

## Summary
{extracted_data['summary']}

## Key Points
"""
    
    # Add key points
    for point in extracted_data['key_points']:
        formatted += f"- {point}\n"
    
    # Add references if any
    if extracted_data['references']:
        formatted += "\n## References\n"
        for ref in extracted_data['references']:
            formatted += f"- {ref}\n"
    
    # Create safe filename from title
    safe_title = "".join(c for c in extracted_data['title'] if c.isalnum() or c in (' ', '-')).strip()
    safe_title = safe_title.replace(' ', '-')
    
    return formatted, safe_title

def process_webpage(url: str, api_key: Optional[str] = None) -> tuple[str, Path]:
    """Process a webpage using Firecrawl and convert it to a note."""
    # Use API key from environment if not provided
    api_key = api_key or os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        raise ValueError("Firecrawl API key not found. Please provide it as an argument or set FIRECRAWL_API_KEY environment variable.")
    
    app = FirecrawlApp(api_key=api_key)
    
    # Extract data using Firecrawl
    data = app.extract(
        [url],
        {
            'prompt': '''Extract the following information from this webpage:
                        1. A clear title
                        2. A comprehensive summary
                        3. Key points or takeaways
                        4. Any references or important links''',
            'schema': ExtractSchema.model_json_schema(),
        }
    )
    
    if not data or not data[0]:
        raise RuntimeError(f"Failed to extract data from {url}")
    
    # Format the extracted data into a note
    note_content, title = create_note(url, data[0])
    
    # Create output directory if it doesn't exist
    output_dir = Path('drafts/webpages')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save the note
    output_file = output_dir / f"{title}.md"
    output_file.write_text(note_content)
    
    return note_content, output_file

def main():
    parser = argparse.ArgumentParser(description="Convert webpages to markdown notes using Firecrawl")
    parser.add_argument("url", help="URL of the webpage to process")
    parser.add_argument("--api-key", help="Firecrawl API key (optional if FIRECRAWL_API_KEY environment variable is set)")
    
    args = parser.parse_args()
    
    try:
        _, output_file = process_webpage(args.url, args.api_key)
        print(f"Created note: {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 