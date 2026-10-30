from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from repositories.employee_repository import EmployeeRepository


class EmployeeNotFound(Exception):
    pass


class DuplicateEmployeeId(Exception):
    pass


class EmployeeService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = EmployeeRepository(db)

    def get_all(self, department=None):
        return self.repo.get_all(department)

    def get(self, employee_id):
        row = self.repo.get(employee_id)
        if row is None:
            raise EmployeeNotFound(employee_id)
        return row

    def register(self, data):
        self.repo.add(data.model_dump())
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise DuplicateEmployeeId(data.employee_id)
        return self.get(data.employee_id)

    def replace(self, employee_id, data):
        row = self.get(employee_id)
        values = data.model_dump()
        values["employee_id"] = employee_id
        self.repo.update(row, values)
        self.db.commit()
        return self.get(employee_id)

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
