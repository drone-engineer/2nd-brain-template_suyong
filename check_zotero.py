import sqlite3
import os
import shutil

# Copy database files to avoid lock
src_db = '/Users/drone_engineer/Zotero/zotero.sqlite'
src_wal = '/Users/drone_engineer/Zotero/zotero.sqlite-wal'
dst_db = '/tmp/zotero_copy.sqlite'
dst_wal = '/tmp/zotero_copy.sqlite-wal'

# Remove old copies
for f in [dst_db, dst_wal, dst_db + '-shm']:
    if os.path.exists(f):
        os.remove(f)

# Copy
shutil.copy2(src_db, dst_db)
if os.path.exists(src_wal):
    shutil.copy2(src_wal, dst_wal)

conn = sqlite3.connect(dst_db, timeout=30)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Check schema
cur.execute("PRAGMA table_info(items)")
cols = cur.fetchall()
print("items table columns:", [c[1] for c in cols])

# Total items (excluding notes and annotations)
cur.execute("""
    SELECT COUNT(*) FROM items i 
    JOIN itemTypes it ON i.itemTypeID = it.itemTypeID 
    WHERE it.typeName NOT IN ('note', 'annotation')
""")
print('Total non-note items:', cur.fetchone()[0])

# Recent items (last 7 days)
cur.execute("""
    SELECT i.itemID, i.key, it.typeName, i.dateAdded, i.dateModified, ir.value as title
    FROM items i 
    JOIN itemTypes it ON i.itemTypeID = it.itemTypeID 
    LEFT JOIN itemData id ON i.itemID = id.itemID AND id.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
    LEFT JOIN itemDataValues ir ON id.valueID = ir.valueID 
    WHERE it.typeName NOT IN ('note', 'annotation')
    AND i.dateAdded >= date('now', '-7 days')
    ORDER BY i.dateAdded DESC
    LIMIT 30
""")
rows = cur.fetchall()
print(f'\nRecent items (last 7 days): {len(rows)}')
for r in rows:
    title = r["title"][:80] if r["title"] else "(no title)"
    print(f'  {r["dateAdded"]} | {r["typeName"]} | {r["key"]} | {title}')

# Check for items with PDF attachments
cur.execute("""
    SELECT i.itemID, i.key, it.typeName, i.dateAdded, ir.value as title,
           COUNT(a.itemID) as attachment_count
    FROM items i
    JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
    LEFT JOIN itemData id ON i.itemID = id.itemID AND id.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
    LEFT JOIN itemDataValues ir ON id.valueID = ir.valueID
    LEFT JOIN items a ON a.parentItemID = i.itemID AND a.itemType IN (SELECT itemTypeID FROM itemTypes WHERE typeName IN ('pdf', 'attachment', 'document', 'file'))
    WHERE it.typeName NOT IN ('note', 'annotation')
    AND i.dateAdded >= date('now', '-14 days')
    GROUP BY i.itemID
    ORDER BY i.dateAdded DESC
    LIMIT 30
""")
rows = cur.fetchall()
print(f'\nRecent items with attachments (last 14 days):')
for r in rows:
    title = r["title"][:60] if r["title"] else "(no title)"
    print(f'  {r["dateAdded"]} | {r["typeName"]} | {r["key"]} | atts={r["attachment_count"]} | {title}')

conn.close()
