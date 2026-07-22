from typing import Optional

from sqlmodel import SQLModel, Field


class DocumentSequence(SQLModel, table=True):
    __tablename__ = "document_sequences"

    id: Optional[int] = Field(default=None, primary_key=True)

    document_type: str = Field(index=True, unique=True)

    prefix: str

    last_number: int = Field(default=0)

    digits: int = Field(default=6)