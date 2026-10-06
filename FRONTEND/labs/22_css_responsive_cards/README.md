# Ticket: Employee Directory Cards

**Customer:** Acme HR  
**Need:** Three employee cards that wrap, with a min-width breakpoint.

`flex-wrap` moves a card to the next line when the row is full. A `min-width` media query changes the layout from a chosen width upward. They do different jobs.

`flex-basis` is on the main axis. Put `flex: 1 1 260px` inside the row query. On a column, that 260px would be height, not width.
