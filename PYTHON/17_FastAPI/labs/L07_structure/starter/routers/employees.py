from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db
from models import Employee
from schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("", response_model=list[EmployeeOut])
def list_employees(department: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Employee)
    if department is not None:
        query = query.filter(Employee.department == department)
    return query.all()


@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    row = db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()
    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return row


# TODO: move POST, PUT, PATCH, and DELETE here from your Lesson 6 main.py.
# Each route takes db: Session = Depends(get_db) instead of calling SessionLocal().
# No try/finally is needed: get_db closes the session.
