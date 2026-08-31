# Ticket: TechMart Hello REST (in-memory catalog)

**Customer:** CampusCart / TechMart canteen screen  
**Need:** Two JSON pings (`GET /hello`, `GET /health`) **plus** an in-memory canteen **list**, **GET by id**, and **POST**. No database this ticket.

**Teaching-order:** `@RestController`, `@GetMapping` / `@PostMapping`, JSON `Map` / `List`, `HttpStatus` / `@ResponseStatus` / `ResponseEntity` lite (200 / 201 / 404), `@PathVariable`, `@RequestBody`, in-memory `ArrayList`. `spring-boot-starter-web` only. `jakarta.*` if you import servlet types. No JPA / `@Entity`. No Security / JWT. No DTO layer / `@Valid` / Postman collection. No Lombok. No `DataSource` / Hikari / MySQL. Thymeleaf is **not** required (optional one-pager is Stretch in the module).

Each of `starter/`, `broken/`, and `solution/` is a Maven tree. Open the folder that contains **`pom.xml`**.

## Starter
Complete TODOs in `HelloController` and `CanteenController`. `CanteenItem` getters/setters are already there. Seed at least two snacks. Server assigns ids on POST.

## Broken
`@Controller` instead of `@RestController` (view lookup, not JSON). List returns `toString()`. `@PathVariable` name does not match `{itemId}`. POST missing `@RequestBody` and **201**. Fix until curl matches Done when.

## Run

```bash
cd starter          # or broken / solution
mvn spring-boot:run
```

Second terminal:

```bash
curl http://localhost:8080/hello
curl http://localhost:8080/health
curl http://localhost:8080/canteen/items
curl http://localhost:8080/canteen/items/1
curl http://localhost:8080/canteen/items/99
curl -X POST http://localhost:8080/canteen/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Pani puri","priceInr":30}'
```

## Done when
- [ ] `mvn spring-boot:run` starts (Tomcat on the configured port)
- [ ] GET `/hello` JSON with a message
- [ ] GET `/health` JSON with `status` UP
- [ ] GET `/canteen/items` JSON **array** from an in-memory `List`
- [ ] GET `/canteen/items/{id}` uses `@PathVariable` — **200** or **404**
- [ ] POST `/canteen/items` uses `@RequestBody` — **201**; server sets `id`
- [ ] No JPA, Security, Thymeleaf, Lombok, JDBC starter, or DataSource required
- [ ] `target/` is gitignored; `.env` not committed

## Stretch
- `GET /canteen/items?maxPrice=40` with `@RequestParam`.
- Optional Thymeleaf **one** page (`starter-thymeleaf` + `templates/canteen.html`) — not the ticket.
- Lombok getters — optional, not in Done when.
- **Later — JPA:** persist snacks in MySQL. **Later —** `@Valid`, DTOs, Postman.
