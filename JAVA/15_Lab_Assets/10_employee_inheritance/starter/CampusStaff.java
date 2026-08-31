// STARTER — OOP Part 2. extends + super. No throw. No interfaces.

public class CampusStaff {
    public static void main(String[] args) {
        Employee e = new Employee("Ravi", 501, 30000);
        Manager m = new Manager("Meera", 900, 30000, 8000);
        e.display();
        m.display();
        System.out.println("m is Employee? " + (m instanceof Employee));
    }
}

class Employee {
    private String name;
    private int empId;
    protected double basic;

    Employee(String name, int empId, double basic) {
        this.name = name;
        this.empId = empId;
        this.basic = basic;
    }

    double net() {
        return basic * 0.9;
    }

    void display() {
        System.out.println(name + " (" + empId + ") net ₹" + (int) net());
    }

    String getName() {
        return name;
    }

    int getEmpId() {
        return empId;
    }

    @Override
    public String toString() {
        return name + " (" + empId + ")";
    }
}

class Manager extends Employee {
    private double bonus;

    Manager(String name, int empId, double basic, double bonus) {
        super(name, empId, basic);
        this.bonus = bonus;
    }

    // TODO: @Override double net() { return super.net() + bonus; }

    // TODO: @Override void display() { print name, empId, net }
}
