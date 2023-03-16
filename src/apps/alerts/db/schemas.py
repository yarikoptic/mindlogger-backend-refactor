from sqlalchemy import Boolean, Column, ForeignKey, String

from infrastructure.database.base import Base


class AlertConfigSchema(Base):
    """This table is used as an alert configuration for a
    specific applet and specific activity item answer
    """

    __tablename__ = "alerts_configs"

    applet_id = Column(
        ForeignKey("applets.id", ondelete="RESTRICT"),
        nullable=False,
    )
    activity_item_id = Column(
        ForeignKey("activity_items.id", ondelete="RESTRICT"),
        nullable=False,
    )
    alert_message = Column(String(), nullable=False)
    specific_answer = Column(String(), nullable=False)
    viewed = Column(Boolean(), nullable=False, default=True)


class AlertSchema(Base):
    """This table is used as responses to specific flow activity items"""

    __tablename__ = "alerts"

    alert_config_id = Column(
        ForeignKey("alerts_configs.id", ondelete="RESTRICT"),
        nullable=False,
    )
    respondent_id = Column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )
    is_watched = Column(Boolean(), nullable=False, default=False)
    applet_id = Column(
        ForeignKey("applets.id", ondelete="RESTRICT"),
        nullable=False,
    )
    activity_item_id = Column(
        ForeignKey("activity_items.id", ondelete="RESTRICT"),
        nullable=False,
    )
