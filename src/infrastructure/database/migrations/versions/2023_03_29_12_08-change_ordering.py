"""change ordering

Revision ID: 8595f5e743f4
Revises: 5ea08a20c2d3
Create Date: 2023-03-29 12:08:25.549087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8595f5e743f4"
down_revision = "5ea08a20c2d3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("activities", "ordering", new_column_name="order")
    op.alter_column("activity_histories", "ordering", new_column_name="order")
    op.alter_column("activity_item_histories", "ordering", new_column_name="order")
    op.alter_column("activity_items", "ordering", new_column_name="order")
    op.alter_column("flow_histories", "ordering", new_column_name="order")
    op.alter_column("flow_item_histories", "ordering", new_column_name="order")
    op.alter_column("flow_items", "ordering", new_column_name="order")
    op.alter_column("flows", "ordering", new_column_name="order")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("activities", "order", new_column_name="ordering")
    op.alter_column("activity_histories", "order", new_column_name="ordering")
    op.alter_column("activity_item_histories", "order",new_column_name="ordering")
    op.alter_column("activity_items", "order", new_column_name="ordering")
    op.alter_column("flow_histories", "order", new_column_name="ordering")
    op.alter_column("flow_item_histories", "order", new_column_name="ordering")
    op.alter_column("flow_items", "order", new_column_name="ordering")
    op.alter_column("flows", "order", new_column_name="ordering")
    # ### end Alembic commands ###
