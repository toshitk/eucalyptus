from datetime import datetime

from sqlalchemy import DATETIME, VARCHAR, Column, Integer

from .base import Base


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    deleted_at = Column(DATETIME, default=None)
    created_at = Column(DATETIME, default=datetime.now, nullable=False)
    updated_at = Column(
        DATETIME, default=datetime.now, nullable=False, onupdate=datetime.now
    )

    def __init__(
        self,
        user_id: int,
        name: str,
        deleted_at: datetime | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        id: int | None = None,
    ):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def __str__(self):
        return f"id: {self.id}, \
user_id: {self.user_id}, \
name: {self.name}, \
deleted_at: {self.deleted_at}, \
created_at: {self.created_at}, \
updated_at: {self.updated_at}"
