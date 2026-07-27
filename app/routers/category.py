from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.database.session import get_session
from app.services.category_service import CategoryService

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def list_categories(
    request: Request,
    session: Session = Depends(get_session),
):
    categories = CategoryService.get_all(session)

    return templates.TemplateResponse(
        request=request,
        name="category/list.html",
        context={
            "request": request,
            "categories": categories,
            "title": "Category Master",
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
            "category": None,
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
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get("/{category_id}/edit")
def edit_category(
    category_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    category = CategoryService.get_by_id(session, category_id)

    if not category:
        return RedirectResponse(
            url="/categories/",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    return templates.TemplateResponse(
        request=request,
        name="category/form.html",
        context={
            "request": request,
            "title": "Edit Category",
            "category": category,
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
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get("/{category_id}/delete")
def delete_category(
    category_id: int,
    session: Session = Depends(get_session),
):
    CategoryService.delete(
        session=session,
        category_id=category_id,
    )

    return RedirectResponse(
        url="/categories/",
        status_code=status.HTTP_303_SEE_OTHER,
    )