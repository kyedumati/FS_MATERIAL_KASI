from fastapi import FastAPI, HTTPException

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
