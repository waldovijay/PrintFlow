from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.session import get_session
from app.services.brand_service import BrandService

router = APIRouter(prefix="/brands", tags=["Brands"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def brand_list(
    request: Request,
    search: str = "",
    session: Session = Depends(get_session),
):
    brands = BrandService.get_all(session)

    if search:
        search_text = search.lower()

        brands = [
            b for b in brands
            if search_text in b.brand_code.lower()
            or search_text in b.brand_name.lower()
            or search_text in (b.description or "").lower()
        ]

    return templates.TemplateResponse(
        request=request,
        name="brand/list.html",
        context={
            "request": request,
            "brands": brands,
            "page_title": "Brand Master",
            "page_subtitle": "Manage Brands",
            "add_url": "/brands/new",
            "add_button_text": "+ Add Brand",
        },
    )


@router.get("/new")
def new_brand(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="brand/form.html",
        context={
            "request": request,
            "title": "Add Brand",
            "brand": None,
            "cancel_url": "/brands/",
            "is_edit": False,
        },
    )

@router.post("/create")
def create_brand(
    brand_code: str = Form(...),
    brand_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    BrandService.create(
        session=session,
        brand_code=brand_code,
        brand_name=brand_name,
        description=description,
    )

    return RedirectResponse(
        url="/brands/",
        status_code=303,
    )


@router.get("/{brand_id}/edit")
def edit_brand(
    brand_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    brand = BrandService.get_by_id(session, brand_id)

    return templates.TemplateResponse(
        request=request,
        name="brand/form.html",
        context={
            "request": request,
            "title": "Edit Brand",
            "brand": brand,
            "is_edit": True,
        },
    )


@router.post("/{brand_id}/update")
def update_brand(
    brand_id: int,
    brand_code: str = Form(...),
    brand_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    BrandService.update(
        session=session,
        brand_id=brand_id,
        brand_code=brand_code,
        brand_name=brand_name,
        description=description,
    )

    return RedirectResponse(
        url="/brands/",
        status_code=303,
    )