from sqlmodel import Session, select

from app.models.brand import Brand


class BrandService:

    @staticmethod
    def get_all(session: Session):
        return session.exec(
            select(Brand)
            .where(Brand.active == True)
            .order_by(Brand.brand_name)
        ).all()

    @staticmethod
    def get_by_id(session: Session, brand_id: int):
        return session.get(Brand, brand_id)

    @staticmethod
    def create(
        session: Session,
        brand_code: str,
        brand_name: str,
        description: str,
    ):

        brand = Brand(
            brand_code=brand_code,
            brand_name=brand_name,
            description=description,
        )

        session.add(brand)
        session.commit()

        return brand

    @staticmethod
    def update(
        session: Session,
        brand_id: int,
        brand_code: str,
        brand_name: str,
        description: str,
    ):

        brand = session.get(Brand, brand_id)

        brand.brand_code = brand_code
        brand.brand_name = brand_name
        brand.description = description

        session.add(brand)
        session.commit()

        return brand