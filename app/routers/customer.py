from fastapi import APIRouter

router=APIRouter(prefix="/customers",tags=["Customers"])

@router.get("/")
def list_customers():
    return {"message":"Customer module ready"}
