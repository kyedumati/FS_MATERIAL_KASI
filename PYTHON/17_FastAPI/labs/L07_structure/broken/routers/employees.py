from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db
from models import Employee
from schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate

router = APIRouter(prefix="/employee", tags=["employees"])


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


@router.post("", status_code=201, response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    row = Employee(**employee.model_dump())
    db.add(row)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Employee id already exists")
    db.refresh(row)
    return row


@router.put("/{employee_id}", response_model=EmployeeOut)
def replace_employee(employee_id: str, employee: EmployeeCreate, db: Session = Depends(get_db)):
    row = db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()
    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.model_dump().items():
        setattr(row, key, value)
    row.employee_id = employee_id
    db.commit()
    db.refresh(row)
    return row


@router.patch("/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: str, changes: EmployeeUpdate, db: Session = Depends(get_db)):
    row = db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()
    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in changes.model_dump(exclude_unset=True).items():
        setattr(row, key, value)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{employee_id}", status_code=204)
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    row = db.query(Employee).filter(Employee.employee_id == employee_id).one_or_none()
    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(row)
    db.commit()
    return Response(status_code=204)
