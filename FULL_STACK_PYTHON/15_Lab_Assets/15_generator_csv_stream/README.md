# Ticket: Stream Rows With `yield`

**Customer:** Analytics  
**Need:** Hand out rows one at a time with `yield` — do not build a giant result list.

## Starter

Complete `iter_rows` in `starter/stream_csv.py` over the in-memory `SAMPLE_ROWS`.

## Broken

`broken/stream_csv.py` returns a full list instead of yielding — fix it.

## Seed

`seed/large_sample.csv` — **Stretch after Files week** (open + `csv.DictReader` + yield).

## Done when

- [ ] `iter_rows` uses `yield` (not `return` of a full list)
- [ ] Printing a few rows works without loading extras into a list first
- [ ] You can explain: call → generator object → `next` / `for` → exhaustion

## After class (optional)

Wire the same idea into `ksr_utils/generators.py` (`read_rows`) as Stretch on the toolkit kit.
