#!/usr/bin/env python3

"""
Daily YouTube Scout - Hunter-Killer Drone System
"""

import os
import sys
import json
import requests
from datetime import datetime

# Configuration for YouTube API (replace with your own API key from Google Cloud Console)
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY') or 'YOUR_YOUTUBE_API_KEY_HERE'
assert YOUTUBE_API_KEY != 'YOUR_YOUTUBE_API_KEY_HERE', "Please set YOUTUBE_API_KEY environment variable"

# Base URL for YouTube Data API v3
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

# Keywords to search for in titles, descriptions, and tags related to Hunter-Killer drones
QUERY_KEYWORDS = [
    "Hunter-Killer drone",
    "Autonomous killer drone", 
    "killer drone system",
    "drone swarm kill chain",
    "C-UAS kill chain"
]

# Set up headers for API request
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def get_today_str():
    """Returns today's date in YYYY-MM-DD format"""
    return datetime.now().strftime('%Y-%m-%d')

def search_youtube_videos():
    """
    Search for YouTube videos using the specified keywords
    Returns a list of video metadata objects.
    """
    results = []
    
    for keyword in QUERY_KEYWORDS:
        params = {
            'key': YOUTUBE_API_KEY,
            'q': keyword,
            'part': 'snippet',
            'type': 'video',
            'maxResults': 5,
            'order': 'relevance'
        }

        try:
            response = requests.get(BASE_URL, headers=HEADERS, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Process each video in the search results
            for item in data['items']:
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                channel = item['snippet']['channelTitle']
                url = f"https://youtu.be/{video_id}"
                thumbnail_url = item['snippet']['thumbnails']['default']['url']
                description = item['snippet'].get('description', '')
                publish_time = item['snippet'].get('publishedAt')
                
                results.append({
                    'meta': {
                        'id': video_id,
                        'title': title,
                        'uploader': channel,
                        'url': url,
                        'duration': None,
                        'view_count': None,
                        'published': publish_time
                    },
                    'raw': f"raw/youtube/{get_today_str()}-{video_id}.md"
                })
        except Exception as e:
            print(f"Error during search for {keyword}: {e}", file=sys.stderr)
            
    return results

def save_to_file(raw_path, video_info):
    """
    Save the raw YouTube video metadata to a Markdown file.
    """
    try:
        # Create directory if needed
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        
        # Generate markdown content
        markdown_content = f"""---
title: {video_info['meta']['title']}
channel: {video_info['meta']['uploader']}
url: {video_info['meta']['url']}
published: {video_info['meta']['published']}
duration_s: {video_info['meta']['duration']}
views: {video_info['meta']['view_count']}
collected: {get_today_str()}
sha256: {None}
source_type: youtube
---

# {video_info['meta']['title']}

- 채널: {video_info['meta']['uploader']}
- URL: {video_info['meta']['url']}
- 업로드: {video_info['meta']['published']}
- 조회수: {video_info['meta']['view_count']}
- 길이(초): {video_info['meta']['duration']}
- 수집: {get_today_str()} (매일 YouTube 스카우트 — Hunter-Killer 계열)

## 자막/설명 요약
(자막 없음)

---
*raw evidence — immutable. YouTube 캡처.*
"""
        with open(raw_path, 'w') as f:
            f.write(markdown_content)
            
    except Exception as e:
        print(f"Error saving {raw_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Only proceed if we have an API key
    if YOUTUBE_API_KEY is None or YOUTUBE_API_KEY == 'YOUR_YOUTUBE_API_KEY_HERE':
        print(json.dumps({'error': 'YOUTUBE_API_KEY not provided'}), file=sys.stderr)
        sys.exit(1)

    # Search for YouTube videos based on keywords
    search_results = search_youtube_videos()
    
    # Save each result to a file in raw/youtube/
    for video_info in search_results:
        save_to_file(video_info['raw'], video_info)
        
    # Output search results to stdout for logging purposes 
    print(json.dumps(search_results))
