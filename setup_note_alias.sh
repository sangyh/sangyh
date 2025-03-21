#!/bin/bash

# setup_note_alias.sh - Sets up aliases for the new_note.sh script and deployment tools
# Usage: ./setup_note_alias.sh

# Get the absolute path to the scripts
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
NOTE_SCRIPT="$SCRIPT_DIR/new_note.sh"
DEPLOY_SCRIPT="$SCRIPT_DIR/deploy.sh"
PUBLISH_SCRIPT="$SCRIPT_DIR/publish.sh"

# Make scripts executable
chmod +x "$NOTE_SCRIPT"
chmod +x "$DEPLOY_SCRIPT"
chmod +x "$PUBLISH_SCRIPT"

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
    echo "alias deploy='$DEPLOY_SCRIPT'"
    echo "alias publish='$PUBLISH_SCRIPT'"
    echo "alias publish-article='$PUBLISH_SCRIPT -t article'"
    echo "alias publish-timeline='$PUBLISH_SCRIPT -t timeline'"
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

# Add deployment aliases
echo "" >> "$SHELL_RC"
echo "# Aliases for deploying and publishing the website" >> "$SHELL_RC"

# Check and add the 'deploy' alias
if ! grep -q "alias deploy=" "$SHELL_RC"; then
    echo "alias deploy='$DEPLOY_SCRIPT'" >> "$SHELL_RC"
    echo "Added alias 'deploy' to $SHELL_RC"
else
    echo "Alias 'deploy' already exists in $SHELL_RC"
fi

# Check and add the 'publish' alias
if ! grep -q "alias publish=" "$SHELL_RC"; then
    echo "alias publish='$PUBLISH_SCRIPT'" >> "$SHELL_RC"
    echo "Added alias 'publish' to $SHELL_RC"
else
    echo "Alias 'publish' already exists in $SHELL_RC"
fi

# Check and add the 'publish-article' alias
if ! grep -q "alias publish-article=" "$SHELL_RC"; then
    echo "alias publish-article='$PUBLISH_SCRIPT -t article'" >> "$SHELL_RC"
    echo "Added alias 'publish-article' to $SHELL_RC"
else
    echo "Alias 'publish-article' already exists in $SHELL_RC"
fi

# Check and add the 'publish-timeline' alias
if ! grep -q "alias publish-timeline=" "$SHELL_RC"; then
    echo "alias publish-timeline='$PUBLISH_SCRIPT -t timeline'" >> "$SHELL_RC"
    echo "Added alias 'publish-timeline' to $SHELL_RC"
else
    echo "Alias 'publish-timeline' already exists in $SHELL_RC"
fi

echo ""
echo "Setup complete! To use the aliases immediately, run:"
echo "source $SHELL_RC"
echo ""
echo "After that, you can use these commands:"
echo ""
echo "# For creating notes:"
echo "note \"Your Atomic Note Title\"      # Creates a note in the notes/ directory"
echo "tnote \"Your Timeline Note Title\"   # Creates a note in the content/timeline/ directory"
echo "article \"Your Article Title\"       # Creates an article in the content/posts/ directory"
echo ""
echo "# For deploying your site:"
echo "deploy \"Commit message\"            # Builds and deploys your site with the given commit message"
echo ""
echo "# For creating and publishing in one step:"
echo "publish \"Note Title\"               # Creates a note (default: article) and deploys the site"
echo "publish-article \"Article Title\"    # Creates an article and deploys the site"
echo "publish-timeline \"Timeline Title\"  # Creates a timeline note and deploys the site"
echo "publish --deploy-only -m \"Message\" # Only deploys the site without creating a note" 