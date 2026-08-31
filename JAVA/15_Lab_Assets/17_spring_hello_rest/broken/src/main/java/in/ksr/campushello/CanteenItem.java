package in.ksr.campushello;

public class CanteenItem {

    private int id;
    private String name;
    private int priceInr;

    public CanteenItem() {
    }

    public CanteenItem(int id, String name, int priceInr) {
        this.id = id;
        this.name = name;
        this.priceInr = priceInr;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
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
