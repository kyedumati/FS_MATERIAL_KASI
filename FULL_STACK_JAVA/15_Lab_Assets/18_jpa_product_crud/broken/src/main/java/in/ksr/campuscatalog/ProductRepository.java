package in.ksr.campuscatalog;

import org.springframework.data.jpa.repository.JpaRepository;

// BROKEN: id type must match Product's Long @Id — not Integer.
public interface ProductRepository extends JpaRepository<Product, Integer> {
}
