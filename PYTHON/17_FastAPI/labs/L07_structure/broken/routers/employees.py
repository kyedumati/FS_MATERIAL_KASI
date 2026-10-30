from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from database import get_db
from schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate
from services.employee_service import EmployeeService

router = APIRouter(prefix="/employee", tags=["employees"])


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


@router.post("", status_code=201, response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate, service: EmployeeService = Depends(get_employee_service)):
    return service.register(employee)


@router.put("/{employee_id}", response_model=EmployeeOut)
def replace_employee(
    employee_id: str,
    employee: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service),
):
    return service.replace(employee_id, employee)


@router.patch("/{employee_id}", response_model=EmployeeOut)
def update_employee(
    employee_id: str,
    changes: EmployeeUpdate,
    service: EmployeeService = Depends(get_employee_service),
):
    return service.update(employee_id, changes)


@router.delete("/{employee_id}", status_code=204)
def delete_employee(employee_id: str, service: EmployeeService = Depends(get_employee_service)):
    service.delete(employee_id)
    return Response(status_code=204)
