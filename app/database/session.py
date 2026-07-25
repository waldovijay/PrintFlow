from sqlmodel import Session
from app.database.engine import engine
from app.models.unit import Unit
from app.models.brand import Brand

def get_session():
    with Session(engine) as session:
        yield session