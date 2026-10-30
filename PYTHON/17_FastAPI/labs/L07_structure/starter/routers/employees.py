from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from database import get_db
from schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate
from services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["employees"])


def get_employee_service(db: Session = Depends(get_db)) -> EmployeeService:
    return EmployeeService(db)


@router.get("", response_model=list[EmployeeOut])
def list_employees(
    department: str | None = None,
    service: EmployeeService = Depends(get_employee_service),
):
    return service.get_all(department)


@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str, service: EmployeeService = Depends(get_employee_service)):
    return service.get(employee_id)


# TODO: move POST, PUT, PATCH, and DELETE here from your Lesson 6 main.py.
# Each route takes service: EmployeeService = Depends(get_employee_service)
# instead of calling SessionLocal(). No try/finally is needed: get_db closes the session.
