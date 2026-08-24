package in.ksr.campusauth;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public class ProductRequest {

    @NotBlank
    @Size(max = 80)
    private String name;

    @NotNull
    @Min(1)
    private Integer priceInr;

    public ProductRequest() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getPriceInr() {
        return priceInr;
    }

    public void setPriceInr(Integer priceInr) {
        this.priceInr = priceInr;
    }
}
