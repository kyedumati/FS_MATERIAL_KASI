import os

import mysql.connector
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "trainee",
    "password": os.getenv("DB_PASSWORD", "password123"),
    "database": "training_db",
}


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
        cursor = self.db.cursor(dictionary=True)
        try:
            if department is None:
                cursor.execute(
                    "SELECT employee_id, name, designation, department, email, phone "
                    "FROM employee"
                )
            else:
                cursor.execute(
                    "SELECT employee_id, name, designation, department, email, phone "
                    "FROM employee WHERE department = %s",
                    (department,),
                )
            return cursor.fetchall()
        finally:
            cursor.close()

    def get(self, employee_id):
        cursor = self.db.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT employee_id, name, designation, department, email, phone "
                "FROM employee WHERE employee_id = %s",
                (employee_id,),
            )
            return cursor.fetchone()
        finally:
            cursor.close()

    def add(self, values):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "INSERT INTO employee (employee_id, name, designation, department, email, phone) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (values["employee_id"], values["name"], values["designation"], values["department"], values["email"], values["phone"]),
            )
        finally:
            cursor.close()

    def update(self, row, values):
        row.update(values)
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE employee SET name = %s, designation = %s, department = %s, email = %s, phone = %s "
                "WHERE employee_id = %s",
                (row["name"], row["designation"], row["department"], row["email"], row["phone"], row["employee_id"]),
            )
        finally:
            cursor.close()
        return row

    def delete(self, row):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM employee WHERE employee_id = %s", (row["employee_id"],))
        finally:
            cursor.close()


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


app = FastAPI(title="AcmeHR")


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/employees", response_model=list[EmployeeOut])
def list_employees(department: str | None = None):
    db = mysql.connector.connect(**DB_CONFIG)
    try:
        return EmployeeService(db).get_all(department)
    finally:
        db.close()


@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str):
    db = mysql.connector.connect(**DB_CONFIG)
    try:
        return EmployeeService(db).get(employee_id)
    finally:
        db.close()


@app.post("/employees", status_code=201, response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate):
    db = mysql.connector.connect(**DB_CONFIG)
    try:
        return EmployeeService(db).register(employee)
    finally:
        db.close()


@app.patch("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: str, changes: EmployeeUpdate):
    db = mysql.connector.connect(**DB_CONFIG)
    try:
        return EmployeeService(db).update(employee_id, changes)
    finally:
        db.close()


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: str):
    db = mysql.connector.connect(**DB_CONFIG)
    try:
        EmployeeService(db).delete(employee_id)
        return Response(status_code=204)
    finally:
        db.close()
