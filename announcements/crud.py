from typing import Any
from sqlalchemy.orm import Session
from database.models import Announcement


def get_announcement_by_id(db: Session, announcement_id: int):
    return (
        db.query(Announcement)
        .filter(Announcement.id == announcement_id)
        .first()
    )


def create_announcement(db: Session, announcement: Announcement):
    db.add(announcement)
    db.commit()
    db.refresh(announcement)
    return announcement


def get_announcements(db: Session, skip: int = 0, limit: int = 10) -> Any:
    return (
        db.query(Announcement)
        .order_by(Announcement.position)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_announcement(db: Session, announcement_id: int, data: dict):
    db.query(Announcement).filter(Announcement.id == announcement_id).update(
        data
    )
    db.commit()
    return get_announcement_by_id(db, announcement_id)


def increase_announcement_view(db: Session, announcement_id: int):
    announcement = get_announcement_by_id(db, announcement_id)
    if not announcement:
        return None
    return update_announcement(
        db, announcement_id, {"views": announcement.views + 1}
    )


def delete_announcement(db: Session, announcement_id: int):
    db.query(Announcement).filter(Announcement.id == announcement_id).delete()
    db.commit()
