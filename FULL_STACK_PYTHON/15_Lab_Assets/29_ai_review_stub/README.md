**Sessions:** optional after S95

# Ticket: Optional AI Recommend Endpoint

**Customer:** CampusCart stretch goal  
**Need:** Given a short text review, return a tiny “sentiment” score using a simple sklearn pipeline (or a stub if sklearn not installed).

**Note:** Optional — never blocks placement sessions.

## Starter
Implement `score_review` in `starter/recommend.py`.

## Done when
- [ ] Returns a dict `{"label": "pos"|"neg"|"neu", "score": float}`
- [ ] Empty text → clear error, no crash
