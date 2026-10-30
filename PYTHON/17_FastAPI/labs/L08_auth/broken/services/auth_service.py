from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from security import create_token, hash_password, verify_password


class InvalidCredentials(Exception):
    pass


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)

    def login(self, email, password):
        user = self.repo.get_by_email(email)
        if user is None:
            raise InvalidCredentials()
        return create_token(user.email, user.role)

    def seed(self, users):
        if self.repo.count() > 0:
            return
        for email, password, role in users:
            self.repo.add({"email": email, "password_hash": hash_password(password), "role": role})
        self.db.commit()
