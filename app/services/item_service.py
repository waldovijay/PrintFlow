from sqlmodel import Session, select

from app.models.item import Item
from app.services.sequence_service import SequenceService


class ItemService:

    @staticmethod
    def get_by_id(session: Session, item_id: int):
        return session.get(Item, item_id)

    @staticmethod
    def get_all(session: Session):
        statement = (
            select(Item)
            .where(Item.active == True)
            .order_by(Item.item_name)
        )
        return session.exec(statement).all()

    @staticmethod
    def create(
        session: Session,
        item_name: str,
        item_type: str = "Product",
        inventory_managed: bool = True,
        category: str = "",
        unit: str = "",
        hsn_sac: str = "",
        gst_percent: float = 0,
        cost_price: float = 0,
        selling_price: float = 0,
        description: str = "",
    ):

        item_code = SequenceService.get_next_number(
            session,
            "ITEM",
            "ITM",
        )

        item = Item(
            item_code=item_code,
            item_name=item_name,
            item_type=item_type,
            inventory_managed=inventory_managed,
            category=category or None,
            unit=unit or None,
            hsn_sac=hsn_sac or None,
            gst_percent=gst_percent,
            cost_price=cost_price,
            selling_price=selling_price,
            description=description or None,
        )

        session.add(item)
        session.commit()
        session.refresh(item)

        return item

    @staticmethod
    def update(
        session: Session,
        item_id: int,
        item_name: str,
        item_type: str,
        inventory_managed: bool,
        category: str,
        unit: str,
        hsn_sac: str,
        gst_percent: float,
        cost_price: float,
        selling_price: float,
        description: str,
    ):

        item = ItemService.get_by_id(session, item_id)

        if not item:
            return None

        item.item_name = item_name
        item.item_type = item_type
        item.inventory_managed = inventory_managed
        item.category = category or None
        item.unit = unit or None
        item.hsn_sac = hsn_sac or None
        item.gst_percent = gst_percent
        item.cost_price = cost_price
        item.selling_price = selling_price
        item.description = description or None

        session.add(item)
        session.commit()
        session.refresh(item)

        return item