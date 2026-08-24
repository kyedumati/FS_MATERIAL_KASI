package in.ksr.campuscatalog;

// TODO: @Entity, @Table(name = "campus_products"), @Id, @GeneratedValue IDENTITY
// TODO: jakarta.persistence — not javax.persistence

public class Product {

    private Long id;
    private String name;
    private int priceInr;

    public Product() {
    }

    public Product(String name, int priceInr) {
        this.name = name;
        this.priceInr = priceInr;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPriceInr() {
        return priceInr;
    }

    public void setPriceInr(int priceInr) {
        this.priceInr = priceInr;
    }
}
