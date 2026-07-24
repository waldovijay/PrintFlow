from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.session import get_session
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def item_list(
    request: Request,
    session: Session = Depends(get_session),
):
    items = ItemService.get_all(session)

    return templates.TemplateResponse(
        request=request,
        name="item/list.html",
        context={
            "request": request,
            "title": "Item Master",
            "items": items,
        },
    )


@router.get("/new")
def new_item(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="item/form.html",
        context={
            "request": request,
            "title": "Add Item",
        },
    )


@router.post("/create")
def create_item(
    item_name: str = Form(...),
    item_type: str = Form("Product"),
    inventory_managed: bool = Form(True),
    category: str = Form(""),
    unit: str = Form(""),
    hsn_sac: str = Form(""),
    gst_percent: float = Form(0),
    cost_price: float = Form(0),
    selling_price: float = Form(0),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    ItemService.create(
        session=session,
        item_name=item_name,
        item_type=item_type,
        inventory_managed=inventory_managed,
        category=category,
        unit=unit,
        hsn_sac=hsn_sac,
        gst_percent=gst_percent,
        cost_price=cost_price,
        selling_price=selling_price,
        description=description,
    )

    return RedirectResponse(
        url="/items/",
        status_code=303,
    )


@router.get("/{item_id}/edit")
def edit_item(
    item_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    item = ItemService.get_by_id(session, item_id)

    return templates.TemplateResponse(
        request=request,
        name="item/form.html",
        context={
            "request": request,
            "title": "Edit Item",
            "item": item,
            "is_edit": True,
        },
    )


@router.post("/{item_id}/update")
def update_item(
    item_id: int,
    item_name: str = Form(...),
    item_type: str = Form(...),
    inventory_managed: bool = Form(True),
    category: str = Form(""),
    unit: str = Form(""),
    hsn_sac: str = Form(""),
    gst_percent: float = Form(0),
    cost_price: float = Form(0),
    selling_price: float = Form(0),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    ItemService.update(
        session=session,
        item_id=item_id,
        item_name=item_name,
        item_type=item_type,
        inventory_managed=inventory_managed,
        category=category,
        unit=unit,
        hsn_sac=hsn_sac,
        gst_percent=gst_percent,
        cost_price=cost_price,
        selling_price=selling_price,
        description=description,
    )

    return RedirectResponse(
        url="/items/",
        status_code=303,
    )