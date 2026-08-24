package in.ksr.campuscatalog;

import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/products")
public class ProductController {

    // TODO: constructor-inject ProductRepository (no ArrayList)
    // Stretch / React recap: @CrossOrigin(origins = "http://localhost:5173") — not Done when

    @GetMapping
    public List<Product> list() {
        // TODO: findAll(), map each Product -> ProductResponse
        return List.of();
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable Long id) {
        // TODO: findById; 200 + ProductResponse if found, 404 Map if missing
        return ResponseEntity.notFound().build();
    }

    @PostMapping
    public Product add(@RequestBody Product incoming) {
        // TODO: @Valid @RequestBody ProductRequest
        // TODO: map to entity, setId(null), save, return ProductResponse 201
        return incoming;
    }
}
