#!/bin/bash

# GitHub ROS2 Drone Data Collection Script
# This script searches for ROS2 drone related repositories on GitHub

# Keywords to search
KEYWORDS=(
    "ros2 drone detection"
    "autonomous drone ros2"
    "navigation ros2 drone"
    "PX4 bridge ros2"
    "YOLO ros2 drone"
    "Zenoh ros2 drone"
    "MediaPipe ros2 drone"
    "SLAM ros2 drone"
    "ArUco ros2 drone"
)

# Output file
OUTPUT_FILE="raw/articles/2026-09-07-ros2-drone-github-data.md"

# Create output directory if it doesn't exist
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Start writing the markdown file
echo "# ROS2 Drone GitHub Data Collection" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Add timestamp
echo "## Data Collection Date: 2026-09-07" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Iterate through keywords and search GitHub
for keyword in "${KEYWORDS[@]}"; do
    echo "Searching for: $keyword"
    
    # Create search query for GitHub API
    QUERY=$(echo "$keyword" | sed 's/ /+/g')
    
    # Make the API request to GitHub
    RESPONSE=$(curl -s "https://api.github.com/search/repositories?q=${QUERY}+in:name,description,readme&sort=stars&order=desc&per_page=5" \
        -H "Accept: application/vnd.github.v3+json" \
        -H "User-Agent: ROS2-Drone-Data-Collector")
    
    # Write section header
    echo "## $keyword" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Check if response has items and extract repository data properly
    if echo "$RESPONSE" | grep -q '"items"'; then
        # Count repositories found
        REPO_COUNT=$(echo "$RESPONSE" | jq '.items | length')
        echo "Found $REPO_COUNT repositories for '$keyword'" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        
        # Process each repository item
        echo "$RESPONSE" | jq -r '.items[] | "* [\\(.full_name)](\\(.html_url))\n  - Description: \\(.description)\n  - Stars: \\(.stargazers_count)\n  - Forks: \\(.forks_count)\n  - Language: \\(.language)\n  - Last updated: \\(.updated_at)\n  - Owner: [\\(.owner.login)](\\(.owner.html_url))\n"' | sed 's/\\//g' >> "$OUTPUT_FILE"
    else
        echo "No repositories found or error occurred." >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    fi
    
    echo "" >> "$OUTPUT_FILE"
    
    # Rate limiting
    sleep 1
done

echo ""
echo "Data collection complete. Results saved to $OUTPUT_FILE"