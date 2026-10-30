from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from security import create_token, hash_password


class InvalidCredentials(Exception):
    pass


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)

    # TODO: login(email, password). Import verify_password from security.
    # Load the user with self.repo.get_by_email. An unknown email or a wrong password
    # raises InvalidCredentials. Otherwise return create_token(user.email, user.role).

    def seed(self, users):
        if self.repo.count() > 0:
            return
        for email, password, role in users:
            self.repo.add({"email": email, "password_hash": hash_password(password), "role": role})
        self.db.commit()
