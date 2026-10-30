import uuid

from sqlalchemy import Column, String, Text, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String)
    email = Column(String, unique=True)
    password = Column(Text)
    role = Column(String, default="member")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())