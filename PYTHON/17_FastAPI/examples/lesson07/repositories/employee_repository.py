from sqlalchemy.orm import Session

from models import Employee


class EmployeeRepository:
    def __init__(self, db: Session):
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
