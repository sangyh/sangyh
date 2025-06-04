#!/usr/bin/env python3
import os
import sys
import datetime
import subprocess
from pathlib import Path

def create_new_note(title=None, note_type="atomic"):
    """
    Create a new note file in the appropriate directory.
    
    Args:
        title (str, optional): The title of the note. If not provided, will prompt the user.
        note_type (str, optional): Type of note to create. Options: "atomic", "timeline", "article".
                                  Default is "atomic" for notes in the drafts directory.
    
    Returns:
        str: The path to the created note file.
    """
    # Get the current date for frontmatter
    current_date = datetime.datetime.now()
    date_str = current_date.strftime("%Y-%m-%d")
    datetime_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Get the title from the user if not provided
    if not title:
        title = input("Enter note title: ")
    
    # Determine the directory and filename based on note_type
    if note_type == "timeline" or note_type == "note":
        # Timeline notes go in content/timeline with slug-style filenames
        notes_dir = Path("content/timeline")
        slug = title.lower().replace(" ", "-")
        # Remove special characters from slug
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        filename = f"{date_str}-{slug}.md"
    elif note_type == "article":
        # Articles go in content/posts with a category subdirectory
        category = input("Enter category (business, productivity, llms, etc.): ")
        notes_dir = Path("content/posts") / category
        slug = title.lower().replace(" ", "-")
        # Remove special characters from slug
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        filename = f"{slug}.md"
    else:  # Default atomic notes
        # Atomic notes go in the drafts directory with the original title
        notes_dir = Path("drafts")
        filename = title.strip()
    
    # Create the directory if it doesn't exist
    if not notes_dir.exists():
        notes_dir.mkdir(parents=True)
        print(f"Created directory at {notes_dir}")
    
    filepath = notes_dir / filename
    
    # Check if the file already exists
    if filepath.exists():
        print(f"Note '{filename}' already exists. Adding timestamp to avoid overwriting.")
        timestamp = current_date.strftime("%Y%m%d_%H%M%S")
        if note_type == "timeline" or note_type == "article":
            # For Hugo content, insert timestamp before extension
            name, ext = os.path.splitext(filename)
            filename = f"{name}-{timestamp}{ext}"
        else:
            # For atomic notes, append timestamp to filename
            filename = f"{filename}_{timestamp}"
        filepath = notes_dir / filename
    
    # Create the file with appropriate template based on note_type
    with open(filepath, "w") as f:
        if note_type == "timeline" or note_type == "note":
            # Hugo frontmatter for timeline notes
            f.write("---\n")
            f.write(f'title: "{title}"\n')
            f.write(f'date: {datetime_str}\n')
            f.write('type: "timeline"\n')
            f.write('layout: "timeline"\n')
            f.write('draft: false\n')
            f.write('tags: []\n')
            f.write('---\n\n')
            f.write(f"# {title}\n\n")
        elif note_type == "article":
            # Hugo frontmatter for articles
            f.write("---\n")
            f.write(f'author: "Sangy"\n')
            f.write(f'title: "{title}"\n')
            f.write('draft: true\n')
            f.write(f'date: "{date_str}"\n')
            f.write(f'description: ""\n')
            f.write('tags: []\n')
            f.write('categories: []\n')
            f.write('series: []\n')
            f.write('aliases: []\n')
            f.write('cover:\n')
            f.write('  image: \n')
            f.write('  caption: \n')
            f.write('---\n\n')
            f.write(f"# {title}\n\n")
            f.write("## Introduction\n\n")
        else:
            # Simple template for atomic notes
            f.write(f"# {title}\n\n")
            f.write(f"Created: {datetime_str}\n\n")
            f.write("## Content\n\n")
    
    print(f"Created new note: {filepath}")
    return filepath

def open_file(filepath):
    """
    Open a file with the default editor.
    
    Args:
        filepath (Path): The path to the file to open.
    """
    try:
        # Try to use the EDITOR environment variable
        editor = os.environ.get("EDITOR")
        if editor:
            subprocess.run([editor, filepath])
        else:
            # Fall back to platform-specific defaults
            if sys.platform == "darwin":  # macOS
                subprocess.run(["open", filepath])
            elif sys.platform == "win32":  # Windows
                os.startfile(filepath)
            else:  # Linux and others
                subprocess.run(["xdg-open", filepath])
    except Exception as e:
        print(f"Error opening file: {e}")
        print(f"You can manually open the file at: {filepath}")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Create a new note file.")
    parser.add_argument("title", nargs="?", help="The title of the note")
    parser.add_argument("--type", "-t", choices=["atomic", "timeline", "note", "article"], 
                        default="atomic", help="Type of note to create")
    args = parser.parse_args()
    
    # Create the note and open it
    filepath = create_new_note(args.title, args.type)
    open_file(filepath) 