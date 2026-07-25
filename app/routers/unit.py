from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.session import get_session
from app.services.unit_service import UnitService

router = APIRouter(prefix="/units", tags=["Units"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def unit_list(
    request: Request,
    search: str = "",
    session: Session = Depends(get_session),
):
    units = UnitService.get_all(session)

    if search:
        search_text = search.lower()

        units = [
            u for u in units
            if search_text in u.unit_name.lower()
            or search_text in u.short_name.lower()
            or search_text in (u.description or "").lower()
        ]

    return templates.TemplateResponse(
        request=request,
        name="unit/list.html",
        context={
            "request": request,
            "title": "Unit Master",
            "units": units,
            "search": search,
        },
    )

@router.get("/new")
def new_unit(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="unit/form.html",
        context={
            "request": request,
            "title": "Add Unit",
        },
    )


@router.post("/create")
def create_unit(
    unit_name: str = Form(...),
    short_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    UnitService.create(
        session=session,
        unit_name=unit_name,
        short_name=short_name,
        description=description,
    )

    return RedirectResponse(
        url="/units/",
        status_code=303,
    )


@router.get("/{unit_id}/edit")
def edit_unit(
    unit_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    unit = UnitService.get_by_id(session, unit_id)

    return templates.TemplateResponse(
        request=request,
        name="unit/form.html",
        context={
            "request": request,
            "title": "Edit Unit",
            "unit": unit,
            "is_edit": True,
        },
    )


@router.post("/{unit_id}/update")
def update_unit(
    unit_id: int,
    unit_name: str = Form(...),
    short_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):

    UnitService.update(
        session=session,
        unit_id=unit_id,
        unit_name=unit_name,
        short_name=short_name,
        description=description,
    )

    return RedirectResponse(
        url="/units/",
        status_code=303,
    )