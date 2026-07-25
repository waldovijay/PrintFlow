from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class Brand(SQLModel, table=True):
    __tablename__ = "brands"

    id: Optional[int] = Field(default=None, primary_key=True)

    brand_code: str = Field(index=True, unique=True, max_length=20)
    brand_name: str = Field(index=True, max_length=100)
    description: Optional[str] = None

    active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)