"""add categories column to reviews

Revision ID: 8f3a1c2d9b4e
Revises: 42cfd550f26d
Create Date: 2026-06-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '8f3a1c2d9b4e'
down_revision: Union[str, Sequence[str], None] = '42cfd550f26d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "newzealandairlinereviews",
        sa.Column("categories", sa.Text, nullable=True)
    )


def downgrade() -> None:
    with op.batch_alter_table("newzealandairlinereviews", recreate="always") as batch_op:
        batch_op.drop_column("categories")
