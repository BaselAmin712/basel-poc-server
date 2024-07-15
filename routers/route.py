from fastapi import APIRouter

router = APIRouter()

@router.get("/firstRoute")
def read_item():
    return {"this is first route"}