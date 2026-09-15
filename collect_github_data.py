#!/usr/bin/env python3
"""
Collect ROS2 drone GitHub data using GitHub API
"""

import requests
import json
import datetime
from pathlib import Path

# GitHub API endpoint
GITHUB_API_URL = "https://api.github.com/search/repositories"

# Search terms
search_terms = [
    "ros2 drone detection",
    "autonomous drone ros2",
    "navigation ros2 drone",
    "PX4 bridge ros2",
    "YOLO ros2 drone",
    "Zenoh ros2 drone",
    "MediaPipe ros2 drone",
    "SLAM ros2 drone",
    "ArUco ros2 drone"
]

# Headers for GitHub API (optional but recommended)
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "ROS2-Drone-Search-Script"
}

def search_github(query, per_page=30):
    """Search GitHub repositories with the given query"""
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }
    
    response = requests.get(GITHUB_API_URL, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def format_repo_data(repo):
    """Format repository data for markdown"""
    formatted = f"""
### [{repo['name']}]({repo['html_url']})

- **Description**: {repo['description'] or 'No description'}
- **Stars**: {repo['stargazers_count']}
- **Forks**: {repo['forks_count']}
- **Language**: {repo['language'] or 'Not specified'}
- **Created**: {repo['created_at']}
- **Updated**: {repo['updated_at']}
- **Owner**: [{repo['owner']['login']}]({repo['owner']['html_url']})
"""
    return formatted

def main():
    """Main function to collect ROS2 drone data"""
    
    # Get today's date for filename
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"raw/articles/{today}-ros2-drone-github-data.md"
    
    # Initialize markdown content
    markdown_content = f"""# ROS2 Drone Technology GitHub Data - {today}

This report contains the latest GitHub data on ROS2 drone technologies, 
including detection, autonomous navigation, PX4 bridge, YOLO, Zenoh, MediaPipe, SLAM, and ArUco implementations.

## Search Terms Used
- ros2 drone detection
- autonomous drone ros2
- navigation ros2 drone
- PX4 bridge ros2
- YOLO ros2 drone
- Zenoh ros2 drone
- MediaPipe ros2 drone
- SLAM ros2 drone
- ArUco ros2 drone

## Results

"""
    
    # Loop through each search term
    for i, term in enumerate(search_terms):
        print(f"Searching for: {term}")
        results = search_github(term)
        
        if results and 'items' in results:
            markdown_content += f"""

---

## {term}

"""
            
            # Process up to 10 repositories
            for repo in results['items'][:10]:
                markdown_content += format_repo_data(repo)
    
    # Write to file
    with open(filename, 'w') as f:
        f.write(markdown_content)
    
    print(f"Data successfully written to {filename}")

if __name__ == "__main__":
    main()