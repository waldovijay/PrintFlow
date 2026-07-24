from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)

    category_code: str = Field(index=True, unique=True)
    category_name: str = Field(index=True)

    description: Optional[str] = None

    active: bool = True

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)