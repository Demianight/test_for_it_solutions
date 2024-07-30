from pydantic import BaseModel


class AnnouncementCreateSchema(BaseModel):
    title: str
    position: int
