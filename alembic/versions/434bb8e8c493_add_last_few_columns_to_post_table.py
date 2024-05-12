"""add last few columns to post table

Revision ID: 434bb8e8c493
Revises: d92470b0dd88
Create Date: 2024-05-11 03:20:20.493682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '434bb8e8c493'
down_revision: Union[str, None] = 'd92470b0dd88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts",sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.CURRENT_TIMESTAMP(), nullable=False), 
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published") 
    pass
