"""add user table

Revision ID: 9446f7efa385
Revises: 2d9c507ea625
Create Date: 2024-05-11 02:13:11.447599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9446f7efa385'
down_revision: Union[str, None] = '2d9c507ea625'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.CURRENT_TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
