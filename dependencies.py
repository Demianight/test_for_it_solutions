from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import database
from logs import logger
from users import crud


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_logger():
    return logger


def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """
    It's fairly simple to use request headers
    But i dont think that it's required for this task
    So just take user_id from query params

    You can see full implementation here:
    https://github.com/Demianight/fast_api_social_net/blob/main/dependencies/auth.py
    """
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
