#!/usr/bin/env python3
"""
Fetch ArduPilot release notes from GitHub API
"""

import requests
import datetime
import json

# ArduPilot repository URL
ARDUPILOT_REPO_URL = "https://api.github.com/repos/ArduPilot/ardupilot/releases"

# Headers for GitHub API
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "ROS2-Drone-Report-Script"
}

def fetch_ardupilot_releases():
    """Fetch latest ArduPilot releases"""
    response = requests.get(ARDUPILOT_REPO_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching ArduPilot releases: {response.status_code} - {response.text}")
        return None

def main():
    """Main function to collect ArduPilot release notes"""
    
    # Get today's date for filename
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"raw/articles/{today}-ardupilot-release-notes.md"
    
    print("Fetching latest ArduPilot releases...")
    releases = fetch_ardupilot_releases()
    
    if releases:
        # Initialize markdown content
        markdown_content = f"""# ArduPilot Release Notes - {today}

This report contains the latest release notes from the ArduPilot repository.

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
        print("Failed to fetch ArduPilot releases")

if __name__ == "__main__":
    main()