from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from fastapi import Form
from fastapi.responses import RedirectResponse

from app.database.session import get_session
from app.services.customer_service import CustomerService

router = APIRouter(prefix="/customers", tags=["Customers"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def customer_list(
    request: Request,
    session: Session = Depends(get_session)
):
    customers = CustomerService.get_all(session)

    return templates.TemplateResponse(
        request=request,
        name="customer/list.html",
        context={
            "request": request,
            "title": "Customer Master",
            "customers": customers,
        },
    )
@router.get("/new")
def new_customer(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="customer/form.html",
        context={
            "request": request,
            "title": "Add Customer",
        },
    )
@router.post("/create")
def create_customer(
    company_name: str = Form(...),
    contact_person: str = Form(""),
    mobile: str = Form(""),
    gst_number: str = Form(""),
    session: Session = Depends(get_session),
):

    CustomerService.create(
        session=session,
        company_name=company_name,
        contact_person=contact_person,
        mobile=mobile,
        gst_number=gst_number,
    )

    return RedirectResponse(
        url="/customers/",
        status_code=303,
    )