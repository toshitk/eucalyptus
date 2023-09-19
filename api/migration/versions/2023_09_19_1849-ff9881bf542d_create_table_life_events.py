"""create table(life_events)

Revision ID: ff9881bf542d
Revises: f21db4b4c97f
Create Date: 2023-09-19 18:49:37.211023

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import DATETIME, VARCHAR, Column, Integer

# revision identifiers, used by Alembic.
revision: str = "ff9881bf542d"
down_revision: Union[str, None] = "f21db4b4c97f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "life_events",
        Column("id", Integer, primary_key=True),
        Column("plan_id", Integer, nullable=False),
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
            INSERT INTO life_events (id, plan_id, name, year, month, created_at, updated_at)
            VALUES (:id, :plan_id, :name, :year, :month, :created_at, :updated_at)
        """
        ).bindparams(
            sa.bindparam("id", 1),
            sa.bindparam("plan_id", 1),
            sa.bindparam("name", "Marriage"),
            sa.bindparam("year", 2000),
            sa.bindparam("month", 1),
            sa.bindparam("created_at", "2000-01-01"),
            sa.bindparam("updated_at", "2000-01-01"),
        )
    )


def downgrade() -> None:
    op.drop_table("life_events")
