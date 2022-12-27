import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from infrastructure.database.base import Base


class ActivityItemSchema(Base):
    __tablename__ = "activity_items"

    activity_id = sa.Column(
        sa.ForeignKey("activities.id", ondelete="CASCADE"), nullable=False
    )

    question = sa.Column(JSONB())
    response_type = sa.Column(sa.Text())
    answers = sa.Column(JSONB())
    color_palette = sa.Column(sa.Text())
    timer = sa.Column(sa.Integer())
    has_token_value = sa.Column(sa.Boolean(), default=False)
    is_skippable = sa.Column(sa.Boolean(), default=False)
    has_alert = sa.Column(sa.Boolean(), default=False)
    has_score = sa.Column(sa.Boolean(), default=False)
    is_random = sa.Column(sa.Boolean(), default=False)
    is_able_to_move_to_previous = sa.Column(sa.Boolean(), default=False)
    has_text_response = sa.Column(sa.Boolean(), default=False)
    ordering = sa.Column(sa.REAL())
