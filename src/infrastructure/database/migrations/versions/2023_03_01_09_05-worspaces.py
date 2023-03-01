"""worspaces

Revision ID: 790565b6807e
Revises: ce89dac675a7
Create Date: 2023-03-01 09:05:10.433971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "790565b6807e"
down_revision = "ce89dac675a7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_workspaces",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("workspace_name", sa.String(length=100), nullable=False),
        sa.Column("is_modified", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_users_workspaces_user_id_users"),
            ondelete="RESTRICT",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users_workspaces")),
    )
    op.create_index(
        op.f("ix_users_workspaces_user_id"),
        "users_workspaces",
        ["user_id"],
        unique=True,
    )
    op.create_index(
        op.f("ix_users_workspaces_workspace_name"),
        "users_workspaces",
        ["workspace_name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_users_workspaces_workspace_name"),
        table_name="users_workspaces",
    )
    op.drop_index(
        op.f("ix_users_workspaces_user_id"), table_name="users_workspaces"
    )
    op.drop_table("users_workspaces")
    # ### end Alembic commands ###
