from sqlmodel import Session, select

from app.models.unit import Unit
from app.services.sequence_service import SequenceService


class UnitService:

    @staticmethod
    def create(
        session: Session,
        unit_name: str,
        short_name: str,
        description: str = "",
    ):
        unit = Unit(
            unit_code=SequenceService.get_next_number(
                session,
                "UNIT",
                "UNT",
            ),
            unit_name=unit_name,
            short_name=short_name,
            description=description,
        )

        session.add(unit)
        session.commit()
        session.refresh(unit)

        return unit

    @staticmethod
    def get_all(session: Session):
        statement = (
            select(Unit)
            .where(Unit.active == True)
            .order_by(Unit.unit_name)
        )

        return session.exec(statement).all()

    @staticmethod
    def get_dropdown(session: Session):
        return UnitService.get_all(session)

    @staticmethod
    def get_by_id(
        session: Session,
        unit_id: int,
    ):
        return session.get(Unit, unit_id)

    @staticmethod
    def update(
        session: Session,
        unit_id: int,
        unit_name: str,
        short_name: str,
        description: str,
    ):
        unit = session.get(Unit, unit_id)

        unit.unit_name = unit_name
        unit.short_name = short_name
        unit.description = description

        session.add(unit)
        session.commit()
        session.refresh(unit)

        return unit