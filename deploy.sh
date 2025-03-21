#!/bin/bash

# deploy.sh - Automated script for building and deploying the Hugo site
# Usage: ./deploy.sh [commit message]

# Default commit message if none provided
COMMIT_MSG=${1:-"Update site content"}

echo "🚀 Starting deployment process..."

# 1. Build the site with Hugo
echo "🔨 Building site with Hugo..."
hugo

# Check if Hugo build was successful
if [ $? -ne 0 ]; then
    echo "❌ Hugo build failed. Aborting deployment."
    exit 1
fi
echo "✅ Hugo build completed successfully!"

# 2. Add all changes to git
echo "📝 Adding changes to git..."
git add .

# 3. Commit changes with the provided message
echo "💾 Committing changes: \"$COMMIT_MSG\""
git commit -m "$COMMIT_MSG"

# 4. Push changes to the remote repository
echo "☁️ Pushing changes to remote repository..."
git push origin main

# Check if git push was successful
if [ $? -ne 0 ]; then
    echo "❌ Git push failed. Please check your network connection or repository permissions."
    exit 1
fi

echo "✅ Deployment completed successfully! Your changes should be live soon."

# Optional: Print URL to the deployed site
echo "🌐 Visit your site at: https://your-site-url.com"

# Note: Replace 'your-site-url.com' with your actual domain 