import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models import User

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set. Copy .env.example to .env.")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()


# TODO: def verify_password(plain, hashed) -> bool, with bcrypt.checkpw.


def create_token(email: str, role: str) -> str:
    payload = {
        "sub": email,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=60),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# TODO: def get_current_user(token = Depends(oauth2_scheme), db = Depends(get_db)).
# Decode the token with SECRET_KEY. A PyJWTError is 401 "Invalid token".
# Load the User whose email is payload["sub"]. No such user is 401.


# TODO: def require_hr(user = Depends(get_current_user)).
# A role other than "hr" is 403 "HR only". Otherwise return the user.
