from sqlalchemy import Boolean, Column, ForeignKey, String, Text

from infrastructure.database.base import Base


class ThemeSchema(Base):
    __tablename__ = "themes"

    name = Column(String(length=100), nullable=False)
    logo = Column(Text())
    background_image = Column(Text())
    primary_color = Column(String(length=100))
    secondary_color = Column(String(length=100))
    tertiary_color = Column(String(length=100))
    public = Column(Boolean(), default=False)
    allow_rename = Column(Boolean(), default=False)
    creator_id = Column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
