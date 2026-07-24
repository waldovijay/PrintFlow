from sqlmodel import SQLModel, create_engine

# Import all models here
from app.models.customer import Customer
from app.models.item import Item
from app.models.category import Category

DATABASE_URL = "sqlite:///data/printflow.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
