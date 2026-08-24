// BROKEN — copy-paste fields; no super; display misspelled so it is not an override.

public class CampusStaff {
    public static void main(String[] args) {
        Employee e = new Employee("Ravi", 501, 30000);
        Manager m = new Manager("Meera", 900, 30000, 8000);
        e.display();
        m.display();   // still prints the Employee line — Manager.disply never runs
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
}

class Manager extends Employee {
    String name;     // Bug 1: shadows parent instead of reusing it
    int empId;
    double basic;
    double bonus;

    Manager(String name, int empId, double basic, double bonus) {
        super("", 0, 0);   // Bug 2: does not pass the real values
        this.name = name;
        this.empId = empId;
        this.basic = basic;
        this.bonus = bonus;
    }

    double net() {
        return basic * 0.9 + bonus;
    }

    void disply() {   // Bug 3: typo — not an override
        System.out.println(name + " (Mgr) net ₹" + (int) net());
    }
}
