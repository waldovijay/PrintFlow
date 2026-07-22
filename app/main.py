from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database.engine import create_db_and_tables
from app.routers.customer import router as customer_router

# Create FastAPI app first
app = FastAPI(title="PrintFlow ERP")

# Register routers
app.include_router(customer_router)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja templates
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup():
    create_db_and_tables()


@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard/index.html",
        context={
            "request": request,
            "title": "Dashboard",
        },
    )
