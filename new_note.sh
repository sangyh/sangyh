#!/bin/bash

# new_note.sh - Shortcut script to create a new atomic note
# Usage: ./new_note.sh [--type|-t TYPE] "Note Title"
# Types: atomic (default), timeline, note, article
# 
# - atomic: Creates notes in the /drafts directory
# - timeline/note: Creates timeline notes in the content/timeline directory
# - article: Creates articles in the content/posts/{category} directory

# Make the script executable with: chmod +x new_note.sh
# You can also create an alias in your .zshrc or .bashrc:
# alias note='path/to/new_note.sh'
# alias tnote='path/to/new_note.sh --type timeline'
# alias article='path/to/new_note.sh --type article'

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the Python script with any arguments passed to this script
python3 "$SCRIPT_DIR/new_note.py" "$@" 