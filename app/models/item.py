from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: Optional[int] = Field(default=None, primary_key=True)

    item_code: str = Field(index=True, unique=True)

    item_name: str = Field(index=True)

    item_type: str = Field(default="Product")
    inventory_managed: bool = Field(default=True)

    category: Optional[str] = None
    unit: Optional[str] = None

    hsn_sac: Optional[str] = None
    gst_percent: float = Field(default=0)

    cost_price: float = Field(default=0)
    selling_price: float = Field(default=0)

    description: Optional[str] = None

    active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)