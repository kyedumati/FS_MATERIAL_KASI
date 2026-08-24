package in.ksr.campushello;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/canteen/items")
public class CanteenController {

    private final List<CanteenItem> items = new ArrayList<>();
    private int nextId = 1;

    public CanteenController() {
        items.add(new CanteenItem(nextId++, "Idli", 40));
        items.add(new CanteenItem(nextId++, "Filter coffee", 25));
        items.add(new CanteenItem(nextId++, "Masala dosa", 60));
    }

    @GetMapping
    public List<CanteenItem> list() {
        return items;
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable int id) {
        for (CanteenItem item : items) {
            if (item.getId() == id) {
                return ResponseEntity.ok(item);
            }
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(Map.of("error", "No item " + id));
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public CanteenItem add(@RequestBody CanteenItem incoming) {
        incoming.setId(nextId);
        nextId++;
        items.add(incoming);
        return incoming;
    }
}
