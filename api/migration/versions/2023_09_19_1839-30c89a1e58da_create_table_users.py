"""create table(users)

Revision ID: 30c89a1e58da
Revises:
Create Date: 2023-09-19 18:39:09.305364

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import DATETIME, VARCHAR, Column, Integer

# revision identifiers, used by Alembic.
revision: str = "30c89a1e58da"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        Column("id", Integer, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
        Column("email", VARCHAR(255), nullable=False),
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
            INSERT INTO users (id, name, email, created_at, updated_at)
            VALUES (:id, :name, :email, :created_at, :updated_at)
        """
        ).bindparams(
            sa.bindparam("id", 1),
            sa.bindparam("name", "John Smith"),
            sa.bindparam("email", "john@example.com"),
            sa.bindparam("created_at", "2000-01-01"),
            sa.bindparam("updated_at", "2000-01-01"),
        )
    )


def downgrade() -> None:
    op.drop_table("users")
