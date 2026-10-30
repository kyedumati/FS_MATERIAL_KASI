import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
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

    def get_all(self, department=None):
        query = self.db.query(Employee)
        if department is not None:
            query = query.filter(Employee.department == department)
        return query.all()

    def get(self, employee_id):
        return self.db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()

    def count(self):
        return self.db.query(Employee).count()

    def add(self, values):
        self.db.add(Employee(**values))

    def update(self, row, values):
        for key, value in values.items():
            setattr(row, key, value)
        return row

    def delete(self, row):
        self.db.delete(row)


class EmployeeNotFound(Exception):
    pass


class DuplicateEmployeeId(Exception):
    pass


class EmployeeService:
    def __init__(self, db):
        self.db = db
        self.repo = EmployeeRepository(db)

    def get_all(self, department=None):
        return self.repo.get_all(department)

    def get(self, employee_id):
        row = self.repo.get(employee_id)
        if row is None:
            raise EmployeeNotFound(employee_id)
        return row

    # TODO: register(data). Replaces the Lesson 5 version that checked repo.get first.
    # repo.add(data.model_dump()), then commit.
    # A repeated employee_id raises IntegrityError on commit: rollback, then raise DuplicateEmployeeId.
    # Otherwise return self.get(data.employee_id).

    # TODO: replace(employee_id, data). self.get() raises EmployeeNotFound for an unknown id.
    # repo.update the row with every field of data. The id in the path wins.
    # Commit, then return self.get(employee_id).

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
        if self.repo.count() > 0:
            return
        for employee_id, name, designation, department, email, phone in people:
            self.repo.add(
                {
                    "employee_id": employee_id,
                    "name": name,
                    "designation": designation,
                    "department": department,
                    "email": email,
                    "phone": phone,
                }
            )
        self.db.commit()


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


@app.exception_handler(EmployeeNotFound)
def employee_not_found(request: Request, exc: EmployeeNotFound):
    return JSONResponse(status_code=404, content={"detail": "Employee not found"})


@app.exception_handler(DuplicateEmployeeId)
def duplicate_employee_id(request: Request, exc: DuplicateEmployeeId):
    return JSONResponse(status_code=400, content={"detail": "Employee id already exists"})


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
        return EmployeeService(db).get_all(department)
    finally:
        db.close()


@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str):
    db = SessionLocal()
    try:
        return EmployeeService(db).get(employee_id)
    finally:
        db.close()


@app.post("/employees", status_code=201, response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()
    try:
        return EmployeeService(db).register(employee)
    finally:
        db.close()


# TODO: PUT /employees/{employee_id} with response_model=EmployeeOut. Body is EmployeeCreate.
# Return EmployeeService(db).replace(employee_id, employee).


@app.patch("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: str, changes: EmployeeUpdate):
    db = SessionLocal()
    try:
        return EmployeeService(db).update(employee_id, changes)
    finally:
        db.close()


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: str):
    db = SessionLocal()
    try:
        EmployeeService(db).delete(employee_id)
        return Response(status_code=204)
    finally:
        db.close()
