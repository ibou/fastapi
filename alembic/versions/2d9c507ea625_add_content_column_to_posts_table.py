"""add content column to posts table

Revision ID: 2d9c507ea625
Revises: 91f2620142ac
Create Date: 2024-05-11 01:55:05.132242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d9c507ea625'
down_revision: Union[str, None] = '91f2620142ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
