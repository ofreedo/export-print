# Tenant List — printable page

A one-page, spreadsheet-style view of the property tenant export (`source/tenant-export.csv`),
made to be easy to read on screen and to print cleanly from Safari or Chrome.

**This repo holds tenants' names, emails, phone numbers and rents. Keep it private, and
never turn on GitHub Pages for it.**

## Using it

Open `tenant-list.html` in a browser (double-click works; no server needed).

- **By property** (default): one block per address, sorted by town and then by street name.
  Renters who share a unit share a row shade.
- **By renter (A–Z)**: the export's own order (by last name), with address and unit together.
- **Find**: filters both views. Press Esc to clear. A filtered printout says
  "Showing X of 74" at the top.
- **Show phone & email**: untick to print a copy without contact details.
- **Print**: Letter paper, portrait. Each property block stays on one page, and every block
  has its own column headings, because Safari doesn't repeat table headings on printed pages.

Rent is shown per renter, exactly as exported. Several renters can share one unit, so the
same unit's rent can appear more than once. That's why the page has no rent total.

## Updating with a newer export

- **For a quick look:** click **Open another export…** and pick the new CSV. Nothing is saved.
- **To make it the new default:** replace `source/tenant-export.csv` and run this from this folder:

  ```bash
  python3 -I _build/build.py source/tenant-export.csv tenant-list.html
  ```

  The script embeds the CSV in the page between the `/*CSV*/` and `/*END*/` markers.

Columns are matched by their header names (Renter, Property, Unit, Rent, Lease Start, …).
If a CSV has different headers, the page falls back to showing every column as it is.
