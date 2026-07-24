from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.session import get_session
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def category_list(
    request: Request,
    session: Session = Depends(get_session),
):
    categories = CategoryService.get_all(session)

    return templates.TemplateResponse(
        request=request,
        name="category/list.html",
        context={
            "request": request,
            "title": "Category Master",
            "categories": categories,
        },
    )


@router.get("/new")
def new_category(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="category/form.html",
        context={
            "request": request,
            "title": "Add Category",
        },
    )


@router.post("/create")
def create_category(
    category_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):
    CategoryService.create(
        session=session,
        category_name=category_name,
        description=description,
    )

    return RedirectResponse(
        url="/categories/",
        status_code=303,
    )


@router.get("/{category_id}/edit")
def edit_category(
    category_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    category = CategoryService.get_by_id(
        session,
        category_id,
    )

    return templates.TemplateResponse(
        request=request,
        name="category/form.html",
        context={
            "request": request,
            "title": "Edit Category",
            "category": category,
            "is_edit": True,
        },
    )


@router.post("/{category_id}/update")
def update_category(
    category_id: int,
    category_name: str = Form(...),
    description: str = Form(""),
    session: Session = Depends(get_session),
):
    CategoryService.update(
        session=session,
        category_id=category_id,
        category_name=category_name,
        description=description,
    )

    return RedirectResponse(
        url="/categories/",
        status_code=303,
    )