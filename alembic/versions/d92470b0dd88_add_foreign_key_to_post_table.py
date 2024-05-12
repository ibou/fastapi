"""add foreign-key to post table

Revision ID: d92470b0dd88
Revises: 9446f7efa385
Create Date: 2024-05-11 02:22:19.213106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd92470b0dd88'
down_revision: Union[str, None] = '9446f7efa385'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', 
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
