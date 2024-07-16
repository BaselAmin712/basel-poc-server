from fastapi import APIRouter

router = APIRouter()

@router.get("/checkConnection")
def check_connection():
    return {"connection": "You are successfully connected to the poc-server"}