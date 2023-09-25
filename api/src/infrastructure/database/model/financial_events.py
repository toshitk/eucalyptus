from datetime import datetime

from sqlalchemy import DATETIME, VARCHAR, Column, Integer

from .base import Base


class FinancialEvent(Base):
    __tablename__ = "financial_events"

    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)  # 1: income, 2:saving, 3: expense
    category = Column(VARCHAR(255))
    name = Column(VARCHAR(255), nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    amount = Column(Integer)
    deleted_at = Column(DATETIME, default=None)
    created_at = Column(DATETIME, default=datetime.now, nullable=False)
    updated_at = Column(
        DATETIME, default=datetime.now, nullable=False, onupdate=datetime.now
    )

    def __init__(
        self,
        plan_id: int,
        type: int,
        name: str,
        year: int,
        month: int,
        amount: int | None = None,
        category: str | None = None,
        deleted_at: datetime | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        id: int | None = None,
    ):
        self.id = id
        self.type = type
        self.category = category
        self.plan_id = plan_id
        self.name = name
        self.year = year
        self.month = month
        self.amount = amount
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def __str__(self):
        return f"id: {self.id}, \
plan_id: {self.plan_id}, \
type: {self.type}, \
category: {self.category}, \
name: {self.name}, \
year: {self.year}, \
month: {self.month}, \
amount: {self.amount}, \
deleted_at: {self.deleted_at}, \
created_at: {self.created_at}, \
updated_at: {self.updated_at}"
