from sqlmodel import Session, select

from app.models.customer import Customer
from app.services.sequence_service import SequenceService


class CustomerService:

    @staticmethod
    def update(
        session: Session,
        customer_id: int,
        company_name: str,
        contact_person: str,
        mobile: str,
        gst_number: str,
    ):
        customer = CustomerService.get_by_id(session, customer_id)

        if not customer:
            return None

        customer.company_name = company_name
        customer.contact_person = contact_person
        customer.mobile = mobile
        customer.gst_number = gst_number

        session.add(customer)
        session.commit()
        session.refresh(customer)

        return customer

    @staticmethod
    def get_by_id(session: Session, customer_id: int):
        return session.get(Customer, customer_id)

    @staticmethod
    def get_all(session: Session):
        statement = (
            select(Customer)
            .where(Customer.active == True)
            .order_by(Customer.company_name)
        )
        return session.exec(statement).all()

    @staticmethod
    def create(
        session: Session,
        company_name: str,
        contact_person: str = "",
        mobile: str = "",
        gst_number: str = "",
    ):

        customer_code = SequenceService.get_next_number(
            session,
            "CUSTOMER",
            "CUS",
        )

        customer = Customer(
            customer_code=customer_code,
            company_name=company_name,
            contact_person=contact_person or None,
            mobile=mobile or None,
            gst_number=gst_number or None,
        )

        session.add(customer)
        session.commit()
        session.refresh(customer)

        return customer