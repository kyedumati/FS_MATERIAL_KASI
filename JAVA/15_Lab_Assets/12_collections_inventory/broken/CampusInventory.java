// BROKEN — NPE on missing lookup; duplicates allowed; list ignores add-order; remove is partial.

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
        stock.addItem("P101", "Duplicate", 99); // Bug 1: should reject duplicate SKU
        stock.listItems();
        stock.lookup("P102");
        stock.lookup("P999"); // Bug 2: crashes — get without containsKey
        stock.updatePrice("P101", 55);
        stock.removeItem("P102");
        stock.lookup("P102");
        stock.listItems();
    }
}

class Item {
    String sku;           // Bug 3: fields should be private
    String name;
    int priceInr;

    Item(String sku, String name, int priceInr) {
        this.sku = sku;
        this.name = name;
        this.priceInr = priceInr;
    }
}

class Inventory {
    private List<String> skuOrder = new ArrayList<>();
    private Set<String> knownSkus = new HashSet<>();
    private Map<String, Item> catalog = new HashMap<>();

    void addItem(String sku, String name, int priceInr) {
        catalog.put(sku, new Item(sku, name, priceInr)); // overwrites; never checks Set
        skuOrder.add(sku);                               // duplicate SKU also appended
    }

    void listItems() {
        for (String sku : catalog.keySet()) {            // Bug 4: map order, not skuOrder
            Item item = catalog.get(sku);
            System.out.println(item.sku + " " + item.name + " ₹" + item.priceInr);
        }
    }

    void lookup(String sku) {
        Item item = catalog.get(sku);                    // null when missing
        System.out.println(item.sku + " " + item.name + " ₹" + item.priceInr);
    }

    void updatePrice(String sku, int priceInr) {
        catalog.get(sku).priceInr = priceInr;            // NPE if missing; smashes field
    }

    void removeItem(String sku) {
        catalog.remove(sku);                             // Bug 5: set + list still hold sku
    }
}
