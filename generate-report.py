#!/usr/bin/env python3

import os
import glob
from datetime import datetime

def generate_daily_report(date_str):
    print(f"Generating report for {date_str}")
    
    # Create report file name
    report_file = f"docs/workflow/daily-report-{date_str}.md"
    
    # Find all articles for this date
    pattern = f"raw/articles/{date_str}-*.md"
    files = glob.glob(pattern)
    
    with open(report_file, 'w') as f:
        f.write(f"# Daily Report {date_str}\n\n")
        
        f.write("## Raw Articles Processed\n\n")
        
        # Process each file
        for file_path in sorted(files):
            filename = os.path.basename(file_path)
            f.write(f"- [{filename}]({file_path})\n")
            
            # Try to extract a meaningful summary from the first few lines
            try:
                with open(file_path, 'r') as article_file:
                    lines = article_file.readlines()
                    if lines:
                        f.write("  - ")
                        content_preview = " ".join(lines[:3])
                        # Remove any control characters and excessive whitespace
                        import re
                        clean_content_preview = re.sub(r'[^\w\s.,!?;:-]', '', content_preview)
                        f.write(f"{clean_content_preview.strip()[:200]}...\n\n")
            except Exception as e:
                f.write("  - Error reading file\n\n")
    
    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 generate-report.py <date>")
        sys.exit(1)
        
    date_str = sys.argv[1]
    generate_daily_report(date_str)