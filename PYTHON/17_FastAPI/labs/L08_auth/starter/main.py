from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, SessionLocal, engine
from models import Employee, User
from routers.auth import router as auth_router
from routers.employees import router as employees_router
from security import hash_password

SEED = [
    ("E-1042", "Ananya Rao", "Senior Software Engineer", "Engineering", "ananya.rao@acme.example", "+91 90000 01042"),
    ("E-1043", "Karthik Menon", "Engineering Manager", "Engineering", "karthik.menon@acme.example", None),
    ("E-1044", "Meera Iyer", "Accountant", "Finance", "meera.iyer@acme.example", None),
    ("E-1045", "Rahul Sharma", "HR Executive", "Human Resources", "rahul.sharma@acme.example", None),
    ("E-1046", "Fatima Khan", "Product Designer", "Product", "fatima.khan@acme.example", None),
    ("E-1047", "Arjun Reddy", "QA Engineer", "Engineering", "arjun.reddy@acme.example", None),
]


def seed(db):
    if db.query(Employee).count() == 0:
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
    if db.query(User).count() == 0:
        db.add(
            User(
                email="ananya.rao@acme.example",
                password_hash=hash_password("Acme#1042"),
                role="employee",
            )
        )
        db.add(
            User(
                email="rahul.sharma@acme.example",
                password_hash=hash_password("Acme#1045"),
                role="hr",
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
app.include_router(employees_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}
