# Ticket: Employee Management Portal Staff Hierarchy

**Customer:** Employee Management Portal (college HR demo)  
**Need:** `Employee` plus `Manager` that **IS-A** employee (bonus on net pay). No copy-paste of name / id fields.

**Teaching-order:** `extends`, `super()`, `@Override`. Core path is **single** class inheritance. Validate with `print` + `return` if needed — **no `throw`**. **No `abstract` / `implements`** (Part 3). No `ArrayList`. No Lombok.

## Starter
Complete `Manager` in `starter/CampusStaff.java`: constructor with `super(...)`, override `net` and `display`.

## Broken
`Manager` copy-pastes fields and skips `super(...)`. `display` is a new method with a typo — not an override.

## Done when
- [ ] `Manager extends Employee` and calls `super(name, empId, basic)`
- [ ] `@Override` on `display` (and `toString` if you override it)
- [ ] Manager net = employee net + bonus
- [ ] `main` prints one employee and one manager
- [ ] `manager instanceof Employee` is true (print it)

## Stretch
- `Faculty extends Employee` with `dept` (hierarchical).
- **Later — Part 3:** `Payable` interface — lab kit [11_campus_wallet](../11_campus_wallet/).
