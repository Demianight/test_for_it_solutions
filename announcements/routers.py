from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from announcements.schemas_request import AnnouncementCreateSchema
from announcements.schemas_response import AnnouncementSchema
from database.models import Announcement, User
from dependencies import get_db, get_user
from . import crud


router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.get("/")
def get_announcements(
    db: Session = Depends(get_db),
) -> list[AnnouncementSchema]:
    return crud.get_announcements(db)


@router.get("/{announcement_id}")
def get_announcement_by_id(
    announcement_id: int, db: Session = Depends(get_db)
) -> AnnouncementSchema:
    if not crud.get_announcement_by_id(db, announcement_id):
        raise HTTPException(status_code=404, detail="Announcement not found")

    return crud.increase_announcement_view(db, announcement_id)


@router.post("/")
def create_announcement(
    announcement_data: AnnouncementCreateSchema,
    user: User = Depends(get_user),
    db: Session = Depends(get_db),
) -> AnnouncementSchema:
    announcement = Announcement(
        title=announcement_data.title,
        author=user,
        position=announcement_data.position,
    )

    return crud.create_announcement(db, announcement)


@router.delete("/{announcement_id}")
def delete_announcement(
    announcement_id: int,
    user: User = Depends(get_user),
    db: Session = Depends(get_db),
) -> None:
    announcement = crud.get_announcement_by_id(db, announcement_id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")
    if not user.id == announcement.author.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    return crud.delete_announcement(db, announcement_id)
