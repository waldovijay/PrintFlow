from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    __tablename__ = "customers"

    id: Optional[int] = Field(default=None, primary_key=True)

    customer_code: str = Field(index=True, unique=True)
    company_name: str = Field(index=True)

    customer_type: str = Field(default="Corporate")

    contact_person: Optional[str] = None

    mobile: Optional[str] = None
    alternate_mobile: Optional[str] = None

    email: Optional[str] = None

    gst_number: Optional[str] = None
    pan_number: Optional[str] = None

    address: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None

    price_category: str = Field(default="Retail")

    credit_limit: float = Field(default=0)

    payment_terms: int = Field(default=0)

    assigned_salesperson: Optional[str] = None

    gst_type: str = Field(default="Regular")

    remarks: Optional[str] = None

    active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)