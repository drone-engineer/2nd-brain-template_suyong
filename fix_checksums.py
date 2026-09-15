#!/usr/bin/env python3

import hashlib
import os
import re

def fix_sha256_in_file(file_path):
    """Calculate and update SHA256 for a file"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Find the end of frontmatter (after second ---)
        frontmatter_end = content.find(b'---\n\n') + 4
        if frontmatter_end == 3:  # not found
            print(f"Error: Could not find frontmatter in {file_path}")
            return False
        
        body = content[frontmatter_end:]
        
        # Calculate SHA256
        sha256 = hashlib.sha256(body).hexdigest()
        
        # Read file lines to find the existing sha256 line
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        # Find and replace the sha256 line
        for i, line in enumerate(lines):
            if line.startswith('sha256:'):
                lines[i] = f'sha256: {sha256}\n'
                break
        
        with open(file_path, 'w') as f:
            f.writelines(lines)
            
        print(f"Updated SHA256 for {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def fix_missing_frontmatter(file_path):
    """Fix missing frontmatter in file"""
    try:
        # Check if file has frontmatter first line
        with open(file_path, 'r') as f:
            content = f.read()
        
        # If doesn't start with ---, it's missing frontmatter
        if not content.strip().startswith('---'):
            print(f"Error: Missing frontmatter in {file_path}")
            return False
            
        return True
        
    except Exception as e:
        print(f"Error checking frontmatter for {file_path}: {e}")
        return False

if __name__ == "__main__":
    # Files with known issues from the check-gate-b script
    files_to_fix = [
        'raw/articles/2026-08-29-px4-release-notes.md',
        'raw/articles/2026-08-29-ros2-release-notes.md',
        'raw/articles/2026-08-29-ros2-drone-tech-report.md',
        'raw/articles/2026-08-31-ardupilot-release-notes.md',
        'raw/articles/2026-08-31-px4-docs.md',
        'raw/articles/2026-08-31-px4-release-notes.md',
        'raw/articles/2026-08-31-ros2-docs.md',
        'raw/articles/2026-08-31-ros2-drone-github-data.md',
        'raw/articles/2026-08-31-ros2-release-notes.md',
        'raw/articles/2026-09-03-px4-v1.17-release-notes.md',
        'raw/articles/2026-09-03-ros2-drone-github-data.md',
        'raw/articles/2026-09-04-px4-release-notes.md'
    ]
    
    print("Fixing SHA256 checksums for relevant files...")
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            fix_sha256_in_file(file_path)
        else:
            print(f"File not found: {file_path}")