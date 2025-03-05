"""create products table

Revision ID: 9c63e69744ca
Revises: 
Create Date: 2025-03-05 12:49:01.698922

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c63e69744ca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.UUID(as_uuid=True), default=uuid.uuid4, nullable=False, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('stock', sa.Integer, nullable=False),
    )

def downgrade() -> None:
    op.drop_table('products')
