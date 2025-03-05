"""create_order_table

Revision ID: 1e00315510b8
Revises: 9c63e69744ca
Create Date: 2025-03-05 14:15:08.457791

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision: str = '1e00315510b8'
down_revision: Union[str, None] = '9c63e69744ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # Create the 'orders' table
    op.create_table(
        'orders',
        sa.Column('id', sa.UUID(), default=uuid.uuid4, nullable=False, primary_key=True),
        sa.Column('product_id', sa.UUID(), sa.ForeignKey('products.id', ondelete="CASCADE"), nullable=False),  # ForeignKey to products
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('total_amount', sa.Float(), nullable=False)
    )

def downgrade() -> None:
    """Downgrade schema."""
    # Drop the 'orders' table
    op.drop_table('orders')
