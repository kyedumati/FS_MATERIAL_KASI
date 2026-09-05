# Ticket: Swiggy Canteen Inventory

**Customer:** Swiggy / CampusCart canteen  
**Need:** Track items by **SKU**. Lookup must be instant. Duplicate SKUs must be rejected. Listing must follow **add-order**, not hash-bucket order.

**Teaching-order:** `List` / `ArrayList`, `Set` / `HashSet`, `Map` / `HashMap`. Code to the **interface**. Validate with `print` + `return` — **no `throw` / `try` / `catch`**. No files. No Spring. No Lombok. No JDBC.

## Starter
Complete `addItem`, `listItems`, `lookup`, `updatePrice`, and `removeItem` in `starter/CampusInventory.java`. Keep `Item` fields **private**.

## Broken
Lookup of a missing SKU **crashes** (`get` then use the result). Duplicate SKUs are stored. List walks the map (order is not add-order). Remove leaves the list/set stale.

## Done when
- [ ] `List<String> skuOrder`, `Set<String> knownSkus`, `Map<String, Item> catalog` — left side is the **interface**
- [ ] Duplicate SKU prints a message and returns (Set or `containsKey`)
- [ ] `lookup` / `updatePrice` / `removeItem` on a missing SKU print **not found** (no crash)
- [ ] `listItems` walks **skuOrder**, not `catalog.keySet()`
- [ ] Remove updates **map + set + list**
- [ ] `Item` fields stay private; no public `priceInr`
- [ ] No `throw` / `try` / `catch`
- [ ] No Spring / Lombok / JDBC / files

## Stretch
- Tiny CLI menu (Add / Lookup / List / Update price / Remove / Quit) around `Inventory`.
- Placement-cell **contacts**: `Map<String, String>` name → phone plus `Set<String>` unique emails.
- **Later — Exceptions week:** `throw` on blank SKU; catch in the menu.
- **Later — Files week:** save/load a CSV of SKUs.
