#!/usr/bin/env python3
"""Deep diagnostic: compare byte-level hash vs regex-extracted hash."""
import re, hashlib

REPO = "/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template"
fname = "2026-08-23-px4-release-notes.md"
fpath = f"{REPO}/raw/articles/{fname}"

# Read as bytes
with open(fpath, "rb") as f:
    raw_bytes = f.read()

# Read as text
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

# Method 1: Find frontmatter closing "---\n" as bytes
fm_end_byte = raw_bytes.find(b"\n---\n", 4)
body_bytes = raw_bytes[fm_end_byte + 5:]
hash_from_bytes = hashlib.sha256(body_bytes).hexdigest()

# Method 2: Regex on text
fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
body_text = fm_match.group(2)
hash_from_text = hashlib.sha256(body_text.encode("utf-8")).hexdigest()

# Get declared hash
fm_text = fm_match.group(1)
sha_match = re.search(r'sha256:\s*([a-f0-9]{64})', fm_text)
declared = sha_match.group(1)

print(f"File: {fname}")
print(f"Declared hash:     {declared}")
print(f"Hash from bytes:   {hash_from_bytes}")
print(f"Hash from text:    {hash_from_text}")
print(f"Bytes match text:  {body_bytes == body_text.encode('utf-8')}")
print(f"Body bytes len:    {len(body_bytes)}")
print(f"Body text len:     {len(body_text)}")

# If they don't match, find where they differ
if body_bytes != body_text.encode("utf-8"):
    for i, (b, t) in enumerate(zip(body_bytes, body_text.encode("utf-8"))):
        if b != t:
            print(f"\nFirst difference at byte {i}:")
            print(f"  bytes[{i-10}:{i+10}]: {repr(body_bytes[max(0,i-10):i+10])}")
            print(f"  text [{i-10}:{i+10}]: {repr(body_text.encode('utf-8')[max(0,i-10):i+10])}")
            break
    if len(body_bytes) != len(body_text.encode("utf-8")):
        print(f"\nLength mismatch! body_bytes={len(body_bytes)}, text_bytes={len(body_text.encode('utf-8'))}")
        # Show the end of each
        print(f"  body_bytes end: {repr(body_bytes[-20:])}")
        print(f"  text_bytes end: {repr(body_text.encode('utf-8')[-20:])}")

# Also check: is the declared hash matching either?
print(f"\nDeclared matches bytes hash: {declared == hash_from_bytes}")
print(f"Declared matches text hash:  {declared == hash_from_text}")
