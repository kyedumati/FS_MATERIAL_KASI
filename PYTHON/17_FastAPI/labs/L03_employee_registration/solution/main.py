from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="AcmeHR")

employees = [
    {
        "employee_id": "E-1042",
        "name": "Ananya Rao",
        "designation": "Senior Software Engineer",
        "department": "Engineering",
        "email": "ananya.rao@acme.example",
        "phone": "+91 90000 01042",
    },
    {
        "employee_id": "E-1043",
        "name": "Karthik Menon",
        "designation": "Engineering Manager",
        "department": "Engineering",
        "email": "karthik.menon@acme.example",
        "phone": None,
    },
    {
        "employee_id": "E-1044",
        "name": "Meera Iyer",
        "designation": "Accountant",
        "department": "Finance",
        "email": "meera.iyer@acme.example",
        "phone": None,
    },
    {
        "employee_id": "E-1045",
        "name": "Rahul Sharma",
        "designation": "HR Executive",
        "department": "Human Resources",
        "email": "rahul.sharma@acme.example",
        "phone": None,
    },
    {
        "employee_id": "E-1046",
        "name": "Fatima Khan",
        "designation": "Product Designer",
        "department": "Product",
        "email": "fatima.khan@acme.example",
        "phone": None,
    },
    {
        "employee_id": "E-1047",
        "name": "Arjun Reddy",
        "designation": "QA Engineer",
        "department": "Engineering",
        "email": "arjun.reddy@acme.example",
        "phone": None,
    },
]


class EmployeeCreate(BaseModel):
    employee_id: str = Field(pattern=r"^E-\d{4}$")
    name: str = Field(min_length=1)
    designation: str
    department: str
    email: EmailStr
    phone: str | None = None


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
def create_employee(employee: EmployeeCreate):
    if any(row["employee_id"] == employee.employee_id for row in employees):
        raise HTTPException(status_code=400, detail="Employee id already exists")
    row = employee.model_dump()
    employees.append(row)
    return row


@app.put("/employees/{employee_id}")
def replace_employee(employee_id: str, employee: EmployeeCreate):
    current = find_employee(employee_id)
    row = employee.model_dump()
    row["employee_id"] = employee_id
    index = employees.index(current)
    employees[index] = row
    return row


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
