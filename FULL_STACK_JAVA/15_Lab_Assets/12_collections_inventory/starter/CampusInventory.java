// STARTER — Collections. List + Set + Map. Compiles; finish add/list/lookup. No throw.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class CampusInventory {
    public static void main(String[] args) {
        Inventory stock = new Inventory();
        stock.addItem("P101", "Notebook", 40);
        stock.addItem("P102", "Pen", 10);
        stock.addItem("P101", "Notebook", 40); // should reject duplicate SKU
        stock.listItems();
        stock.lookup("P102");
        stock.lookup("P999"); // missing — print, no crash
        // TODO: update price of P101 to 55, then list again
        // TODO: remove P102, then lookup P102
    }
}

class Item {
    private String sku;
    private String name;
    private int priceInr;

    Item(String sku, String name, int priceInr) {
        this.sku = sku;
        this.name = name;
        this.priceInr = priceInr;
    }

    String getSku() {
        return sku;
    }

    String getName() {
        return name;
    }

    int getPriceInr() {
        return priceInr;
    }

    void setPriceInr(int priceInr) {
        this.priceInr = priceInr;
    }
}

class Inventory {
    private List<String> skuOrder = new ArrayList<>();
    private Set<String> knownSkus = new HashSet<>();
    private Map<String, Item> catalog = new HashMap<>();

    void addItem(String sku, String name, int priceInr) {
        // TODO: reject blank sku/name and price <= 0 (print + return)
        // TODO: if knownSkus.contains(sku) print duplicate SKU and return
        // TODO: put Item in catalog; add sku to set and order list
    }

    void listItems() {
        // TODO: walk skuOrder; print sku, name, ₹price
    }

    void lookup(String sku) {
        // TODO: if !catalog.containsKey(sku) print not found and return
        // TODO: else print the item
    }

    void updatePrice(String sku, int priceInr) {
        // TODO: reject price <= 0; missing SKU prints not found
    }

    void removeItem(String sku) {
        // TODO: missing SKU prints not found; else remove from map + set + list
    }
}
