import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+mysqlconnector://trainee:password123@localhost:3306/training_db",
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

SEED = [
    ("E-1042", "Ananya Rao", "Senior Software Engineer", "Engineering", "ananya.rao@acme.example", "+91 90000 01042"),
    ("E-1043", "Karthik Menon", "Engineering Manager", "Engineering", "karthik.menon@acme.example", None),
    ("E-1044", "Meera Iyer", "Accountant", "Finance", "meera.iyer@acme.example", None),
    ("E-1045", "Rahul Sharma", "HR Executive", "Human Resources", "rahul.sharma@acme.example", None),
    ("E-1046", "Fatima Khan", "Product Designer", "Product", "fatima.khan@acme.example", None),
    ("E-1047", "Arjun Reddy", "QA Engineer", "Engineering", "arjun.reddy@acme.example", None),
]


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    employee_id = Column(String(10), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    designation = Column(String(80), nullable=False)
    department = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=True)


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


def seed(db):
    if db.query(Employee).count() > 0:
        return
    for employee_id, name, designation, department, email, phone in SEED:
        db.add(
            Employee(
                employee_id=employee_id,
                name=name,
                designation=designation,
                department=department,
                email=email,
                phone=phone,
            )
        )
    db.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        seed(db)
    finally:
        db.close()
    yield


app = FastAPI(title="AcmeHR", lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/employees", response_model=list[EmployeeOut])
def list_employees(department: str | None = None):
    db = SessionLocal()
    try:
        query = db.query(Employee)
        if department is not None:
            query = query.filter(Employee.department == department)
        return query.all()
    finally:
        db.close()


@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str):
    db = SessionLocal()
    try:
        row = db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return row
    finally:
        db.close()


# TODO: POST /employees with status 201 and response_model=EmployeeOut.
# Body is EmployeeCreate. add, commit, refresh, return the row.
# A repeated employee_id raises IntegrityError: rollback, then 400 "Employee id already exists".


# TODO: PUT /employees/{employee_id}. Body is EmployeeCreate.
# Unknown id is 404. Copy every field onto the row. The id in the path wins. Commit.


# TODO: PATCH /employees/{employee_id}. Body is EmployeeUpdate.
# Unknown id is 404. Copy only changes.model_dump(exclude_unset=True). Commit.


# TODO: DELETE /employees/{employee_id} with status 204.
# Unknown id is 404. delete, commit, return Response(status_code=204).
