from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String

from infrastructure.database.base import Base


class UserSchema(Base):
    __tablename__ = "users"

    email = Column(String(length=100), unique=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    hashed_password = Column(String(length=100))
    last_seen_at = Column(DateTime(), default=datetime.now)
    is_super_admin = Column(Boolean(), default=False, server_default="false")

    def __repr__(self):
        return f"UserSchema(id='{self.id}', email='{self.email}')"


class UserDeviceSchema(Base):
    __tablename__ = "user_devices"

    user_id = Column(ForeignKey("users.id"))
    device_id = Column(String(255))
