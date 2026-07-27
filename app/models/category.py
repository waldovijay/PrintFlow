from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)

    category_code: str = Field(
        max_length=20,
        unique=True,
        index=True,
    )

    category_name: str = Field(
        max_length=100,
        index=True,
    )

    description: Optional[str] = Field(
        default=None,
        max_length=500,
    )

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.now)

    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )