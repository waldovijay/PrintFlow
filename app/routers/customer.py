from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/customers", tags=["Customers"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def customer_list(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="customer/list.html",
        context={
            "request": request,
            "title": "Customers",
            "customers": [],
        },
    )