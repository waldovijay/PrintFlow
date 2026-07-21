from typing import Optional
from sqlmodel import SQLModel, Field

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    name: str
    contact_person: Optional[str]=None
    mobile: str
    email: Optional[str]=None
    city: Optional[str]=None
    is_active: bool=True
