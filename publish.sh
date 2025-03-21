#!/bin/bash

# publish.sh - Combined script for creating notes and publishing the site
# Usage: 
#   ./publish.sh -t [type] -m [commit message] "Note Title"
#   ./publish.sh --deploy-only -m "Commit message"

# Set default values
NOTE_TYPE="article"
COMMIT_MSG="Update site content"
CREATE_NOTE=true
DEPLOY_SITE=true
NOTE_TITLE=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--type)
            NOTE_TYPE="$2"
            shift 2
            ;;
        -m|--message)
            COMMIT_MSG="$2"
            shift 2
            ;;
        --deploy-only)
            CREATE_NOTE=false
            shift
            ;;
        --no-deploy)
            DEPLOY_SITE=false
            shift
            ;;
        *)
            NOTE_TITLE="$1"
            shift
            ;;
    esac
done

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to create a new note
create_note() {
    if [ -z "$NOTE_TITLE" ]; then
        echo "❌ Error: Note title is required when creating a note."
        echo "Usage: ./publish.sh -t [type] -m [commit message] \"Note Title\""
        exit 1
    fi
    
    echo "📝 Creating new $NOTE_TYPE note: \"$NOTE_TITLE\"..."
    python3 "$SCRIPT_DIR/new_note.py" --type "$NOTE_TYPE" "$NOTE_TITLE"
    
    # Check if note creation was successful
    if [ $? -ne 0 ]; then
        echo "❌ Note creation failed."
        exit 1
    fi
    
    echo "✅ Note created successfully!"
    
    # Pause to allow editing the file
    echo "⏱️ Press Enter when you're done editing the note to continue with deployment..."
    read
}

# Function to deploy the site
deploy_site() {
    echo "🚀 Starting deployment process..."
    
    # Build the site with Hugo
    echo "🔨 Building site with Hugo..."
    hugo
    
    # Check if Hugo build was successful
    if [ $? -ne 0 ]; then
        echo "❌ Hugo build failed. Aborting deployment."
        exit 1
    fi
    echo "✅ Hugo build completed successfully!"
    
    # Add all changes to git
    echo "📝 Adding changes to git..."
    git add .
    
    # Commit changes with the provided message
    echo "💾 Committing changes: \"$COMMIT_MSG\""
    git commit -m "$COMMIT_MSG"
    
    # Push changes to the remote repository
    echo "☁️ Pushing changes to remote repository..."
    git push origin main
    
    # Check if git push was successful
    if [ $? -ne 0 ]; then
        echo "❌ Git push failed. Please check your network connection or repository permissions."
        exit 1
    fi
    
    echo "✅ Deployment completed successfully! Your changes should be live soon."
    
    # Replace with your actual site URL
    echo "🌐 Visit your site at: https://your-site-url.com"
}

# Main execution flow
if [ "$CREATE_NOTE" = true ]; then
    create_note
fi

if [ "$DEPLOY_SITE" = true ]; then
    deploy_site
fi

echo "✨ All operations completed!" 