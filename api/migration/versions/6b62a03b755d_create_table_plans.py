"""create table(plans)

Revision ID: 6b62a03b755d
Revises: 71ae9af4bed2
Create Date: 2023-09-19 11:37:59.940088

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import DATETIME, VARCHAR, Column, Integer

# revision identifiers, used by Alembic.
revision: str = "6b62a03b755d"
down_revision: Union[str, None] = "71ae9af4bed2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "plans",
        Column("id", Integer, primary_key=True),
        Column("user_id", Integer, nullable=False),
        Column("name", VARCHAR(255), nullable=False),
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
            INSERT INTO plans (id, user_id, name, created_at, updated_at)
            VALUES (:id, :user_id, :name, :created_at, :updated_at)
        """
        ).bindparams(
            sa.bindparam("id", 1),
            sa.bindparam("user_id", 1),
            sa.bindparam("name", "Sample Plan"),
            sa.bindparam("created_at", "2000-01-01"),
            sa.bindparam("updated_at", "2000-01-01"),
        )
    )


def downgrade() -> None:
    op.drop_table("plans")
