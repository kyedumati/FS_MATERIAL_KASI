package in.ksr.campusauth;

public class ProductMapper {

    private ProductMapper() {
    }

    public static Product toEntity(ProductRequest request) {
        Product product = new Product();
        product.setId(null);
        product.setName(request.getName());
        product.setPriceInr(request.getPriceInr());
        return product;
    }

    public static ProductResponse toResponse(Product product) {
        return new ProductResponse(product.getId(), product.getName(), product.getPriceInr());
    }
}
