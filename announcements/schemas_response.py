from pydantic import BaseModel

from users.schemas_response import UserSchema


class AnnouncementSchema(BaseModel):
    id: int
    title: str
    author: UserSchema
    position: int
    views: int
