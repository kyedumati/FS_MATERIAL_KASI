package in.ksr.campusauth;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import jakarta.validation.Valid;
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
@RequestMapping("/products")
public class ProductController {

    private final ProductRepository products;

    public ProductController(ProductRepository products) {
        this.products = products;
    }

    @GetMapping
    public List<ProductResponse> list() {
        List<ProductResponse> body = new ArrayList<>();
        for (Product row : products.findAll()) {
            body.add(ProductMapper.toResponse(row));
        }
        return body;
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable Long id) {
        Product found = products.findById(id).orElse(null);
        if (found != null) {
            return ResponseEntity.ok(ProductMapper.toResponse(found));
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(Map.of("error", "No product " + id));
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ProductResponse add(@Valid @RequestBody ProductRequest incoming) {
        Product saved = products.save(ProductMapper.toEntity(incoming));
        return ProductMapper.toResponse(saved);
    }
}
