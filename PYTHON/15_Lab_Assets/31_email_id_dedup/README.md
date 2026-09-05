# Ticket: Clean Duplicate IDs Before Import

**Customer:** Swiggy ops importing product / email lists  
**Need:** Remove duplicates from a comma-separated list; preserve first-seen order.

## Starter
Open `starter/dedup.py` — finish `deduplicate`.

## Broken
`broken/dedup.py` loses order or crashes on empty tokens.

## Done when
- [ ] `101,102,101,103` → unique count 3, order preserved
- [ ] Empty tokens after split are ignored
- [ ] Optional mode uses `set` (order may change)

## Stretch
- Case-insensitive email dedupe keeping first-seen casing
