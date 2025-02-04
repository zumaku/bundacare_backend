from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "BundaCare API is running!"}
