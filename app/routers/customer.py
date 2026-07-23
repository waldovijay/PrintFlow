from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from fastapi import Form
from fastapi.responses import RedirectResponse

from app.database.session import get_session
from app.services.customer_service import CustomerService

router = APIRouter(prefix="/customers", tags=["Customers"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/{customer_id}/edit")
def edit_customer(
    customer_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    customer = CustomerService.get_by_id(
        session,
        customer_id,
    )

    return templates.TemplateResponse(
        request=request,
        name="customer/form.html",
        context={
            "request": request,
            "title": "Edit Customer",
            "customer": customer,
            "is_edit": True,
        },
    )
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
@router.post("/{customer_id}/update")
def update_customer(
    customer_id: int,
    company_name: str = Form(...),
    contact_person: str = Form(""),
    mobile: str = Form(""),
    gst_number: str = Form(""),
    session: Session = Depends(get_session),
):
    CustomerService.update(
        session=session,
        customer_id=customer_id,
        company_name=company_name,
        contact_person=contact_person,
        mobile=mobile,
        gst_number=gst_number,
    )

    return RedirectResponse(
        url="/customers/",
        status_code=303,
    )
