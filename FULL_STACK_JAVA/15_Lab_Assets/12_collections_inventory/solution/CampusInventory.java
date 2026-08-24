// SOLUTION — List add-order + Set uniqueness + Map lookup. print+return only.

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
        stock.addItem("P101", "Notebook", 40);
        stock.listItems();
        stock.lookup("P102");
        stock.lookup("P999");
        stock.updatePrice("P101", 55);
        stock.listItems();
        stock.removeItem("P102");
        stock.lookup("P102");
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
        if (sku.trim().length() == 0 || name.trim().length() == 0) {
            System.out.println("sku and name required");
            return;
        }
        if (priceInr <= 0) {
            System.out.println("price must be positive");
            return;
        }
        if (knownSkus.contains(sku)) {
            System.out.println("duplicate SKU: " + sku);
            return;
        }
        catalog.put(sku, new Item(sku, name, priceInr));
        knownSkus.add(sku);
        skuOrder.add(sku);
    }

    void listItems() {
        for (String sku : skuOrder) {
            Item item = catalog.get(sku);
            System.out.println(item.getSku() + " " + item.getName() + " ₹" + item.getPriceInr());
        }
    }

    void lookup(String sku) {
        if (!catalog.containsKey(sku)) {
            System.out.println("not found: " + sku);
            return;
        }
        Item item = catalog.get(sku);
        System.out.println(item.getSku() + " " + item.getName() + " ₹" + item.getPriceInr());
    }

    void updatePrice(String sku, int priceInr) {
        if (priceInr <= 0) {
            System.out.println("price must be positive");
            return;
        }
        Item item = catalog.get(sku);
        if (item == null) {
            System.out.println("not found: " + sku);
            return;
        }
        item.setPriceInr(priceInr);
    }

    void removeItem(String sku) {
        if (!catalog.containsKey(sku)) {
            System.out.println("not found: " + sku);
            return;
        }
        catalog.remove(sku);
        knownSkus.remove(sku);
        skuOrder.remove(sku);
    }
}
