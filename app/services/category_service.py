from sqlmodel import Session, select

from app.models.category import Category
from app.services.sequence_service import SequenceService


class CategoryService:
   
    @staticmethod
    def create(
        session: Session,
        category_name: str,
        description: str = "",
    ):
        category = Category(
            category_code=SequenceService.get_next_number(
                session,
                "CATEGORY",
                "CAT",
            ),
            category_name=category_name,
            description=description,
        )

        session.add(category)
        session.commit()
        session.refresh(category)

        return category

    @staticmethod
    def get_all(session: Session):
        statement = (
            select(Category)
            .where(Category.is_active == True)
            .order_by(Category.category_name)
        )

        return session.exec(statement).all()

    @staticmethod
    def get_dropdown(session: Session):
        statement = (
            select(Category)
            .where(Category.is_active == True)
            .order_by(Category.category_name)
        )

        return session.exec(statement).all()

    @staticmethod
    def get_by_id(
        session: Session,
        category_id: int,
    ):
        return session.get(Category, category_id)

    @staticmethod
    def update(
        session: Session,
        category_id: int,
        category_name: str,
        description: str,
    ):
        category = session.get(Category, category_id)
  
        if not category:
            return None
        
        category.category_name = category_name
        category.description = description

        session.commit()
        session.refresh(category)

        return category
    @staticmethod
    def delete(
        session: Session,
        category_id: int,
    ):
        category = session.get(Category, category_id)

        if not category:
            return False

        session.delete(category)
        session.commit()

        return True