from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from models import User
from security import create_token

router = APIRouter(tags=["auth"])


# TODO: POST /login with form: OAuth2PasswordRequestForm = Depends().
# form.username is the email. Unknown email or wrong password is 401 "Wrong email or password".
# Return {"access_token": create_token(...), "token_type": "bearer"}.


# TODO: GET /me with user = Depends(get_current_user).
# Return {"email": ..., "role": ...}.
