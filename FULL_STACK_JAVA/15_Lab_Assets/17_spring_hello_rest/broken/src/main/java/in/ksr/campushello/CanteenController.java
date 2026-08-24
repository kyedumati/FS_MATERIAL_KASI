package in.ksr.campushello;

import java.util.ArrayList;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

// BROKEN: list is Java toString; path variable name mismatch; POST has no @RequestBody / 201.
@RestController
public class CanteenController {

    private final List<CanteenItem> items = new ArrayList<>();

    public CanteenController() {
        items.add(new CanteenItem(1, "Idli", 40));
        items.add(new CanteenItem(2, "Filter coffee", 25));
    }

    @GetMapping("/canteen/items")
    public String list() {
        return items.toString();
    }

    @GetMapping("/canteen/items/{itemId}")
    public CanteenItem getById(@PathVariable int id) {
        return items.get(0);
    }

    @PostMapping("/canteen/items")
    public CanteenItem add(CanteenItem incoming) {
        items.add(incoming);
        return incoming;
    }
}
