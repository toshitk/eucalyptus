"""create table(financial_events)

Revision ID: 76eae9971e09
Revises: bc8b12fcd7ab
Create Date: 2023-09-25 15:35:41.238385

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import DATETIME, VARCHAR, Column, Integer

# revision identifiers, used by Alembic.
revision: str = "76eae9971e09"
down_revision: Union[str, None] = "bc8b12fcd7ab"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "financial_events",
        Column("id", Integer, primary_key=True),
        Column("plan_id", Integer, nullable=False),
        Column("type", Integer, nullable=False),  # 1: income, 2:saving, 3: expense
        Column("category", VARCHAR(255)),
        Column("name", VARCHAR(255), nullable=False),
        Column("year", Integer, nullable=False),
        Column("month", Integer, nullable=False),
        Column("deleted_at", DATETIME, default=None),
        Column("created_at", DATETIME, default=datetime.now, nullable=False),
        Column(
            "updated_at",
            DATETIME,
            default=datetime.now,
            nullable=False,
            onupdate=datetime.now,
        ),
    )

    op.execute(
        sa.text(
            """
            INSERT INTO financial_events (id, plan_id, type, category, name, year, month, created_at, updated_at)
            VALUES (:id, :plan_id, :type, :category, :name, :year, :month, :created_at, :updated_at)
        """
        ).bindparams(
            sa.bindparam("id", 1),
            sa.bindparam("plan_id", 1),
            sa.bindparam("type", 1),
            sa.bindparam("category", "salary"),
            sa.bindparam("name", "monthly salary"),
            sa.bindparam("year", 2000),
            sa.bindparam("month", 1),
            sa.bindparam("created_at", "2000-01-01"),
            sa.bindparam("updated_at", "2000-01-01"),
        )
    )


def downgrade() -> None:
    op.drop_table("financial_events")
