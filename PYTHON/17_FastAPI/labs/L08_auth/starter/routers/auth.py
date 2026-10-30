from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from models import User
from services.auth_service import AuthService

router = APIRouter(tags=["auth"])


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


# TODO: POST /login with form: OAuth2PasswordRequestForm = Depends()
# and service: AuthService = Depends(get_auth_service).
# form.username is the email. Return {"access_token": service.login(...), "token_type": "bearer"}.
# A wrong login raises InvalidCredentials, which main.py turns into 401.


# TODO: GET /me with user = Depends(get_current_user) from security.
# Return {"email": ..., "role": ...}.
