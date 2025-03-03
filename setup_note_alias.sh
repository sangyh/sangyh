#!/bin/bash

# setup_note_alias.sh - Sets up aliases for the new_note.sh script
# Usage: ./setup_note_alias.sh

# Get the absolute path to the new_note.sh script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
NOTE_SCRIPT="$SCRIPT_DIR/new_note.sh"

# Check which shell the user is using
if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
    echo "Found .zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
    echo "Found .bashrc"
else
    echo "Could not find .zshrc or .bashrc. Please manually add the aliases to your shell configuration file."
    echo "Add these lines to your shell configuration file:"
    echo "alias note='$NOTE_SCRIPT'"
    echo "alias tnote='$NOTE_SCRIPT --type timeline'"
    echo "alias article='$NOTE_SCRIPT --type article'"
    exit 1
fi

# Add aliases if they don't exist
echo "" >> "$SHELL_RC"
echo "# Aliases for creating different types of notes" >> "$SHELL_RC"

# Check and add the 'note' alias
if ! grep -q "alias note=" "$SHELL_RC"; then
    echo "alias note='$NOTE_SCRIPT'" >> "$SHELL_RC"
    echo "Added alias 'note' to $SHELL_RC"
else
    echo "Alias 'note' already exists in $SHELL_RC"
fi

# Check and add the 'tnote' alias for timeline notes
if ! grep -q "alias tnote=" "$SHELL_RC"; then
    echo "alias tnote='$NOTE_SCRIPT --type timeline'" >> "$SHELL_RC"
    echo "Added alias 'tnote' to $SHELL_RC"
else
    echo "Alias 'tnote' already exists in $SHELL_RC"
fi

# Check and add the 'article' alias for article notes
if ! grep -q "alias article=" "$SHELL_RC"; then
    echo "alias article='$NOTE_SCRIPT --type article'" >> "$SHELL_RC"
    echo "Added alias 'article' to $SHELL_RC"
else
    echo "Alias 'article' already exists in $SHELL_RC"
fi

echo ""
echo "Setup complete! To use the aliases immediately, run:"
echo "source $SHELL_RC"
echo ""
echo "After that, you can create different types of notes with:"
echo "note \"Your Atomic Note Title\"      # Creates a note in the notes/ directory"
echo "tnote \"Your Timeline Note Title\"   # Creates a note in the content/timeline/ directory"
echo "article \"Your Article Title\"       # Creates an article in the content/posts/ directory" 