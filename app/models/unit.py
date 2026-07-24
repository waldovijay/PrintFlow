from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class Unit(SQLModel, table=True):
    __tablename__ = "units"

    id: Optional[int] = Field(default=None, primary_key=True)

    unit_code: str = Field(index=True, unique=True, max_length=20)
    unit_name: str = Field(index=True, unique=True, max_length=100)
    short_name: str = Field(max_length=20)

    description: Optional[str] = Field(default="")

    active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)