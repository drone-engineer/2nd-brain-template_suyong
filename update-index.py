#!/usr/bin/env python3

import os

# Get the current date for indexing
current_date = "2026-08-17"

# Path to the index file
index_file = "docs/workflow/raw-articles-index.md"

# Read the existing content
with open(index_file, 'r') as f:
    lines = f.readlines()

# Find where the 2026 section is located and add our files at the end of it
new_lines = [
    "- `2026-08-15-px4-release-notes.md` — Official PX4 release notes for 2026-08-15\n",
    "- `2026-08-15-ardupilot-release-notes.md` — Official ArduPilot release notes for 2026-08-15\n", 
    "- `2026-08-15-px4-docs.md` — Official PX4 documentation for 2026-08-15\n",
    "- `2026-08-15-ros2-docs.md` — Official ROS2 documentation for 2026-08-15\n",
    "- `2026-08-15-ros2-drone-github-data.md` — GitHub search results for ROS2 drone projects (2026-08-15)\n",
    "- `2026-08-16-px4-release-notes.md` — Official PX4 release notes for 2026-08-16\n",
    "- `2026-08-16-ardupilot-release-notes.md` — Official ArduPilot release notes for 2026-08-16\n",
    "- `2026-08-16-px4-docs.md` — Official PX4 documentation for 2026-08-16\n",
    "- `2026-08-16-ros2-docs.md` — Official ROS2 documentation for 2026-08-16\n",
    "- `2026-08-16-ros2-drone-github-data.md` — GitHub search results for ROS2 drone projects (2026-08-16)\n",
    "- `2026-08-17-px4-release-notes.md` — Official PX4 release notes for 2026-08-17\n",
    "- `2026-08-17-ardupilot-release-notes.md` — Official ArduPilot release notes for 2026-08-17\n",
    "- `2026-08-17-px4-docs.md` — Official PX4 documentation for 2026-08-17\n",
    "- `2026-08-17-ros2-docs.md` — Official ROS2 documentation for 2026-08-17\n",
    "- `2026-08-17-ros2-drone-github-data.md` — GitHub search results for ROS2 drone projects (2026-08-17)\n"
]

# Find the last section (should be 2026) and add our lines
section_end = None
for i, line in enumerate(lines):
    if line.strip() == "## 2026 (77편)":
        # This is where we insert the new entries with updated count
        section_end = i + 1
        break
        
if section_end is not None:
    # Insert at the correct position after the 2026 section header
    lines.insert(section_end, "## 2026 (80편)\n\n")
    
    # Insert all new entries
    for entry in reversed(new_lines):
        lines.insert(section_end + 1, entry)
        
    # Write back the updated content
    with open(index_file, 'w') as f:
        f.writelines(lines)
        
    print("Successfully updated index file!")
else:
    print("2026 section not found in index file")