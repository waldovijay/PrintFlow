from datetime import datetime
from sqlmodel import SQLModel, Field


class AuditMixin(SQLModel):
    active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)