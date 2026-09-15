#!/usr/bin/env python3
"""
Fetch PX4 release notes from GitHub API
"""

import requests
import datetime
import json

# PX4 repository URL
PX4_REPO_URL = "https://api.github.com/repos/PX4/PX4-Autopilot/releases"

# Headers for GitHub API
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "ROS2-Drone-Report-Script"
}

def fetch_px4_releases():
    """Fetch latest PX4 releases"""
    response = requests.get(PX4_REPO_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching PX4 releases: {response.status_code} - {response.text}")
        return None

def main():
    """Main function to collect PX4 release notes"""
    
    # Get today's date for filename
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"raw/articles/{today}-px4-release-notes.md"
    
    print("Fetching latest PX4 releases...")
    releases = fetch_px4_releases()
    
    if releases:
        # Initialize markdown content
        markdown_content = f"""# PX4 Release Notes - {today}

This report contains the latest release notes from the PX4 Autopilot repository.

## Latest Releases

"""
        
        # Process up to 5 releases
        for i, release in enumerate(releases[:5]):
            markdown_content += f"""### [{release['name']}]({release['html_url']})

- **Published**: {release['published_at']}
- **Tag**: {release['tag_name']}
- **Description**:
{release['body']}

"""
        
        # Write to file
        with open(filename, 'w') as f:
            f.write(markdown_content)
        
        print(f"Data successfully written to {filename}")
    else:
        print("Failed to fetch PX4 releases")

if __name__ == "__main__":
    main()