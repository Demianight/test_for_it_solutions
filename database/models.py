from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    announcements = relationship("Announcement", back_populates="author")


class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    views = Column(  # Better to write helper-model, KISS for now
        Integer,
        default=0,
    )
    position = Column(  # IMHO also should be dynamically generated
        Integer,
        index=True,
    )

    author = relationship("User", back_populates="announcements")
