from fastapi import FastAPI, HTTPException, Response

app = FastAPI(title="AcmeHR")

employees = [
    {
        "employee_id": "E-1042",
        "name": "Ananya Rao",
        "designation": "Senior Software Engineer",
        "department": "Engineering",
    },
    {
        "employee_id": "E-1043",
        "name": "Karthik Menon",
        "designation": "Engineering Manager",
        "department": "Engineering",
    },
    {
        "employee_id": "E-1044",
        "name": "Meera Iyer",
        "designation": "Accountant",
        "department": "Finance",
    },
    {
        "employee_id": "E-1045",
        "name": "Rahul Sharma",
        "designation": "HR Executive",
        "department": "Human Resources",
    },
    {
        "employee_id": "E-1046",
        "name": "Fatima Khan",
        "designation": "Product Designer",
        "department": "Product",
    },
    {
        "employee_id": "E-1047",
        "name": "Arjun Reddy",
        "designation": "QA Engineer",
        "department": "Engineering",
    },
]


def find_employee(employee_id: str) -> dict:
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/employees")
def list_employees(department: str | None = None):
    if department is None:
        return employees
    return [employee for employee in employees if employee["department"] == department]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: str):
    return find_employee(employee_id)


@app.post("/employees", status_code=201)
def create_employee(employee: dict):
    # TODO: replace dict with an EmployeeCreate model.
    # employee_id matches E- and 4 digits, for example E-1048.
    # name has at least 1 character.
    # email is an email address.
    # phone is optional.
    # A repeated employee_id returns 400 with detail "Employee id already exists".
    if "employee_id" not in employee or "name" not in employee:
        raise HTTPException(status_code=400, detail="employee_id and name are required")
    employees.append(employee)
    return employee


@app.put("/employees/{employee_id}")
def replace_employee(employee_id: str, employee: dict):
    current = find_employee(employee_id)
    employee["employee_id"] = employee_id
    index = employees.index(current)
    employees[index] = employee
    return employee


@app.patch("/employees/{employee_id}")
def update_employee(employee_id: str, changes: dict):
    current = find_employee(employee_id)
    current.update(changes)
    current["employee_id"] = employee_id
    return current


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: str):
    current = find_employee(employee_id)
    employees.remove(current)
    return Response(status_code=204)
