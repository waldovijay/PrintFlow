from sqlmodel import Session
from app.database.engine import engine
from app.models.unit import Unit

def get_session():
    with Session(engine) as session:
        yield session