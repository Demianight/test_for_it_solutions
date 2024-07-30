from sqlalchemy.orm import Session
from database.models import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session, skip: int = 0, limit: int = 10) -> list:
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, updated_user: User):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.username = updated_user.username
    user.email = updated_user.email
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
