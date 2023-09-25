"""alter table(users)

Revision ID: bc8b12fcd7ab
Revises: ff9881bf542d
Create Date: 2023-09-20 14:47:43.793638

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import DATETIME, VARCHAR, Column, Integer

# revision identifiers, used by Alembic.
revision: str = "bc8b12fcd7ab"
down_revision: Union[str, None] = "ff9881bf542d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("auth0_id", sa.VARCHAR(255)))
    op.execute(
        sa.text(
            """
            UPDATE users SET auth0_id = 'auth0|650b9c9a9414f9ea13f7d9aa'
            WHERE id = 1
        """
        )
    )
    op.alter_column(
        "users",
        "auth0_id",
        existing_type=sa.Integer,
        type_=sa.VARCHAR(255),
        nullable=False,
    )


def downgrade() -> None:
    op.drop_column("users", "auth0_id")
