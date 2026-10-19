"""Embed a tenant export CSV into tenant-list.html.

Usage (from the export-print folder):
    python3 -I _build/build.py source/tenant-export.csv tenant-list.html

Everything between the /*CSV*/ and /*END*/ markers in the page is replaced,
so this can be re-run whenever a newer export comes in.
"""
import json
import re
import sys
from pathlib import Path

csv_path, html_path = Path(sys.argv[1]), Path(sys.argv[2])
text = csv_path.read_text(encoding="utf-8-sig")
# "</" is escaped so the data can never close the <script> tag early.
data = json.dumps({"name": csv_path.name, "text": text}).replace("</", "<\\/")

html = html_path.read_text(encoding="utf-8")
html, count = re.subn(r"/\*CSV\*/.*?/\*END\*/", lambda m: "/*CSV*/" + data + "/*END*/", html, flags=re.S)
if count != 1:
    sys.exit("Could not find the /*CSV*/ ... /*END*/ markers in " + str(html_path))
html_path.write_text(html, encoding="utf-8")

rows = sum(1 for line in text.splitlines() if line.strip()) - 1
print(f"Embedded {rows} rows from {csv_path.name} into {html_path.name}")
