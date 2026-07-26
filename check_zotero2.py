import sqlite3
import os
import shutil

src_db = '/Users/drone_engineer/Zotero/zotero.sqlite'
dst_db = '/tmp/zotero_copy.sqlite'

# Check schema for parent relationship
conn = sqlite3.connect(dst_db, timeout=30)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Check if parentItemID exists
cur.execute("PRAGMA table_info(items)")
cols = [c[1] for c in cur.fetchall()]
print("items columns:", cols)

# Check for parentItemID in any form
if 'parentItemID' in cols:
    print("\nparentItemID found in items table")
    cur.execute("""
        SELECT i.itemID, i.key, it.typeName, i.dateAdded, ir.value as title,
               p.key as parent_key, pr.value as parent_title
        FROM items i
        JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
        LEFT JOIN items p ON i.parentItemID = p.itemID
        LEFT JOIN itemData id ON i.itemID = id.itemID AND id.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
        LEFT JOIN itemDataValues ir ON id.valueID = ir.valueID
        LEFT JOIN itemData pid ON p.itemID = pid.itemID AND pid.fieldID = (SELECT fieldID FROM fields WHERE fieldName = 'title')
        LEFT JOIN itemDataValues pr ON pid.valueID = pr.valueID
        WHERE it.typeName IN ('attachment', 'pdf', 'document')
        ORDER BY i.dateAdded DESC
        LIMIT 20
    """)
else:
    print("\nparentItemID NOT in items table - checking itemData")
    # In Zotero 7, parent relationship might be in itemData
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cur.fetchall()
    print("Tables:", [t[0] for t in tables])
    
    # Check if there's a parentItemID in itemData
    cur.execute("SELECT fieldName FROM fields WHERE fieldName LIKE '%parent%' OR fieldName LIKE '%attach%'")
    fields = cur.fetchall()
    print("Parent/attach fields:", [f[0] for f in fields])

conn.close()
