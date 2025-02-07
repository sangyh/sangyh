#!/usr/bin/env python3

import sys
import json
from pathlib import Path
from datetime import datetime
import re
import yaml
from typing import Dict, List, Any

def sanitize_title(title: str) -> str:
    """Convert title to a valid filename."""
    # Remove invalid filename characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces and other characters with hyphens
    sanitized = re.sub(r'[\s\-]+', '-', sanitized)
    return sanitized.strip('-')

def format_highlight(highlight: Dict[str, Any]) -> str:
    """Format a single highlight with metadata."""
    note = f"> {highlight['text']}\n\n"
    
    if highlight.get('note'):
        note += f"**Note**: {highlight['note']}\n\n"
    
    metadata = []
    if highlight.get('location'):
        metadata.append(f"Location: {highlight['location']}")
    if highlight.get('highlighted_at'):
        metadata.append(f"Highlighted: {highlight['highlighted_at']}")
    
    if metadata:
        note += "_" + " | ".join(metadata) + "_\n\n"
    
    return note

def create_atomic_note(
    title: str,
    highlights: List[Dict[str, Any]],
    source: Dict[str, Any],
    output_dir: Path
) -> Path:
    """Create an atomic note from highlights."""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    sanitized_title = sanitize_title(title)
    
    # Create frontmatter
    frontmatter = {
        "author": "Sangy",
        "title": title,
        "draft": False,
        "date": timestamp,
        "description": f"Notes and highlights from {source.get('title', 'Unknown')}",
        "tags": ["readwise", source.get("category", "book")],
        "categories": ["reading-notes"],
        "series": [],
        "aliases": [sanitized_title],
        "cover": {
            "image": "",
            "caption": ""
        }
    }
    
    # Create note content
    content = f"""---
{yaml.dump(frontmatter, default_flow_style=False)}---

## Highlights

"""
    
    # Add formatted highlights
    for highlight in highlights:
        content += format_highlight(highlight)
    
    # Add source information
    content += f"\n## Source\n\n"
    content += f"- **Title**: {source.get('title', 'Unknown')}\n"
    content += f"- **Author**: {source.get('author', 'Unknown')}\n"
    if source.get('source_url'):
        content += f"- **URL**: {source.get('source_url')}\n"
    
    # Write to file
    output_file = output_dir / f"{sanitized_title}.md"
    output_file.write_text(content)
    return output_file

def process_readwise_export(export_file: Path, output_dir: Path) -> List[Path]:
    """Process a Readwise export JSON file into atomic notes."""
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Read and parse export file
    data = json.loads(export_file.read_text())
    
    # Group highlights by source
    sources: Dict[str, Dict] = {}
    for highlight in data:
        source_id = highlight.get("book_id")
        if source_id not in sources:
            sources[source_id] = {
                "metadata": {
                    "title": highlight.get("book_title", "Unknown"),
                    "author": highlight.get("author", "Unknown"),
                    "source_url": highlight.get("source_url", ""),
                    "category": highlight.get("category", "book")
                },
                "highlights": []
            }
        sources[source_id]["highlights"].append(highlight)
    
    # Create atomic notes for each source
    created_files = []
    for source_data in sources.values():
        file = create_atomic_note(
            title=source_data["metadata"]["title"],
            highlights=source_data["highlights"],
            source=source_data["metadata"],
            output_dir=output_dir
        )
        created_files.append(file)
    
    return created_files

def main():
    if len(sys.argv) != 2:
        print("Usage: readwise_to_atomic.py <readwise_export.json>")
        sys.exit(1)
    
    export_file = Path(sys.argv[1])
    if not export_file.exists():
        print(f"Error: File {export_file} does not exist")
        sys.exit(1)
    
    output_dir = Path("content/posts/readwise")
    created_files = process_readwise_export(export_file, output_dir)
    
    print(f"\nCreated {len(created_files)} atomic notes:")
    for file in created_files:
        print(f"- {file}")

if __name__ == "__main__":
    main()
