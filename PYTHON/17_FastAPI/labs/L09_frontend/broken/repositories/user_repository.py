from sqlalchemy.orm import Session

from models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).one_or_none()

    def count(self):
        return self.db.query(User).count()

    def add(self, values):
        self.db.add(User(**values))
