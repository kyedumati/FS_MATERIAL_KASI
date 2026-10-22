from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

app = FastAPI(title="AcmeHR")

employees = [
    {
        "employee_id": "E-1042",
        "name": "Ananya Rao",
        "designation": "Senior Software Engineer",
        "department": "Engineering",
        "email": "ananya.rao@acme.example",
        "phone": "+91 90000 01042",
        "salary": 90000,
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


class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    designation: str | None = None
    department: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

    @field_validator("name", "designation", "department", "email")
    @classmethod
    def not_null(cls, value):
        if value is None:
            raise ValueError("cannot be null")
        return value


class EmployeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    employee_id: str
    name: str
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


@app.get("/employees", response_model=list[EmployeeOut])
def list_employees(department: str | None = None):
    if department is None:
        return employees
    return [employee for employee in employees if employee["department"] == department]


@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str):
    return find_employee(employee_id)


@app.post("/employees", status_code=201, response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate):
    if any(row["employee_id"] == employee.employee_id for row in employees):
        raise HTTPException(status_code=400, detail="Employee id already exists")
    employees.append(employee.model_dump())
    return employees[-1]


@app.put("/employees/{employee_id}", response_model=EmployeeOut)
def replace_employee(employee_id: str, employee: EmployeeCreate):
    current = find_employee(employee_id)
    row = employee.model_dump()
    row["employee_id"] = employee_id
    index = employees.index(current)
    employees[index] = row
    return row


@app.patch("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: str, changes: EmployeeUpdate):
    current = find_employee(employee_id)
    current.update(changes.model_dump(exclude_unset=True))
    current["employee_id"] = employee_id
    return current


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: str):
    current = find_employee(employee_id)
    employees.remove(current)
    return Response(status_code=204)
