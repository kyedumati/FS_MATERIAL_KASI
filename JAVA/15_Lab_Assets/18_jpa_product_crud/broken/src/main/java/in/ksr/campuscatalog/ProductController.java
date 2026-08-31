package in.ksr.campuscatalog;

import java.util.ArrayList;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// BROKEN: still an in-memory list — restart wipes snacks. Use ProductRepository.
// BROKEN: JSON is the entity (no ProductRequest / ProductResponse / mapper).
// BROKEN: POST has no @Valid — blank name still "saves".
// BROKEN: no @RestControllerAdvice 400 body (and pom is missing starter-validation).
@RestController
@RequestMapping("/products")
public class ProductController {

    private final List<Product> items = new ArrayList<>();

    @GetMapping
    public List<Product> list() {
        return items;
    }

    @GetMapping("/{id}")
    public Product getById(@PathVariable Long id) {
        return items.get(0);
    }

    @PostMapping
    public Product add(@RequestBody Product incoming) {
        items.add(incoming);
        return incoming;
    }
}
