from fastapi import APIRouter, Depends
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session

from database.models import User
from dependencies import get_db
from users.schemas_request import UserCreateSchema

from users.schemas_response import UserSchema
from . import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users(db: Session = Depends(get_db)) -> list[UserSchema]:
    return crud.get_users(db)


@router.post("/")
def create_user(
    user_data: UserCreateSchema, db: Session = Depends(get_db)
) -> UserSchema:
    if crud.get_user_by_username(db, user_data.username):
        raise RequestValidationError("username already exists")

    user = User(username=user_data.username, email=user_data.email)
    return crud.create_user(db, user)
