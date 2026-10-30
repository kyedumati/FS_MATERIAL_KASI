import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from sqlalchemy import Column, Integer, String, create_engine
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


# TODO: class Employee(Base) for the table "employee".
# Columns: id (primary key), employee_id (unique), name, designation,
# department, email, and phone (the only one that may be NULL).
# Match the CREATE TABLE in Lesson 5, section 1.


class EmployeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    employee_id: str
    name: str
    designation: str
    department: str
    email: EmailStr
    phone: str | None = None


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


class EmployeeRepository:
    def __init__(self, db):
        self.db = db

    # TODO: get_all(department=None). Query Employee. Filter by department when it is given.
    # TODO: get(employee_id). Filter on Employee.employee_id. Return one_or_none().
    # TODO: count(). The number of rows in the table.
    # TODO: add(values). values is a dict of columns. db.add(Employee(**values)).

    def update(self, row, values):
        for key, value in values.items():
            setattr(row, key, value)
        return row

    def delete(self, row):
        self.db.delete(row)


class EmployeeService:
    def __init__(self, db):
        self.db = db
        self.repo = EmployeeRepository(db)

    def get_all(self, department=None):
        return self.repo.get_all(department)

    def get(self, employee_id):
        row = self.repo.get(employee_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return row

    def register(self, data):
        if self.repo.get(data.employee_id) is not None:
            raise HTTPException(status_code=400, detail="Employee id already exists")
        self.repo.add(data.model_dump())
        self.db.commit()
        return self.get(data.employee_id)

    def update(self, employee_id, changes):
        row = self.get(employee_id)
        self.repo.update(row, changes.model_dump(exclude_unset=True))
        self.db.commit()
        return self.get(employee_id)

    def delete(self, employee_id):
        row = self.get(employee_id)
        self.repo.delete(row)
        self.db.commit()

    def seed(self, people):
        # TODO: if the repository count is above 0, return.
        # Otherwise repo.add() one dict per tuple in people, then self.db.commit().
        pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        EmployeeService(db).seed(SEED)
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


# TODO: GET /employees with response_model=list[EmployeeOut].
# Open db = SessionLocal(). Return EmployeeService(db).get_all(department).
# Close the session in finally.


# TODO: GET /employees/{employee_id} with response_model=EmployeeOut.
# Return EmployeeService(db).get(employee_id). The service raises 404 for an unknown id.


# TODO: POST /employees with status 201 and response_model=EmployeeOut. Body is EmployeeCreate.
# Return EmployeeService(db).register(employee).


# TODO: PATCH /employees/{employee_id} with response_model=EmployeeOut. Body is EmployeeUpdate.
# Return EmployeeService(db).update(employee_id, changes).


# TODO: DELETE /employees/{employee_id} with status 204.
# Call EmployeeService(db).delete(employee_id), then return Response(status_code=204).
