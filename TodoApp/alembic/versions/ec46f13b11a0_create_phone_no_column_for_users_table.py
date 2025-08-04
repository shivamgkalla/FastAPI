"""Create phone_no column for users table

Revision ID: ec46f13b11a0
Revises: 
Create Date: 2025-07-28 12:23:01.414613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec46f13b11a0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'phone_no', new_column_name='phone_number')


def downgrade() -> None:
    op.alter_column('users', 'phone_number', new_column_name='phone_no')

