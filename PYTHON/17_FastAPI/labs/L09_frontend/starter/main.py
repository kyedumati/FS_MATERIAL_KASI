from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from database import Base, SessionLocal, engine
from routers.auth import router as auth_router
from routers.employees import router as employees_router
from services.auth_service import AuthService, InvalidCredentials
from services.employee_service import DuplicateEmployeeId, EmployeeNotFound, EmployeeService

SEED = [
    ("E-1042", "Ananya Rao", "Senior Software Engineer", "Engineering", "ananya.rao@acme.example", "+91 90000 01042"),
    ("E-1043", "Karthik Menon", "Engineering Manager", "Engineering", "karthik.menon@acme.example", None),
    ("E-1044", "Meera Iyer", "Accountant", "Finance", "meera.iyer@acme.example", None),
    ("E-1045", "Rahul Sharma", "HR Executive", "Human Resources", "rahul.sharma@acme.example", None),
    ("E-1046", "Fatima Khan", "Product Designer", "Product", "fatima.khan@acme.example", None),
    ("E-1047", "Arjun Reddy", "QA Engineer", "Engineering", "arjun.reddy@acme.example", None),
]

USERS = [
    ("ananya.rao@acme.example", "Acme#1042", "employee"),
    ("rahul.sharma@acme.example", "Acme#1045", "hr"),
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        EmployeeService(db).seed(SEED)
        AuthService(db).seed(USERS)
    finally:
        db.close()
    yield


app = FastAPI(title="AcmeHR", lifespan=lifespan)
# TODO: add CORSMiddleware. Allow http://127.0.0.1:5500 and http://localhost:5500,
# every method, and every header (the Authorization header carries the token).
app.include_router(employees_router)
app.include_router(auth_router)


@app.exception_handler(EmployeeNotFound)
def employee_not_found(request: Request, exc: EmployeeNotFound):
    return JSONResponse(status_code=404, content={"detail": "Employee not found"})


@app.exception_handler(DuplicateEmployeeId)
def duplicate_employee_id(request: Request, exc: DuplicateEmployeeId):
    return JSONResponse(status_code=400, content={"detail": "Employee id already exists"})


@app.exception_handler(InvalidCredentials)
def invalid_credentials(request: Request, exc: InvalidCredentials):
    return JSONResponse(status_code=401, content={"detail": "Wrong email or password"})


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}
