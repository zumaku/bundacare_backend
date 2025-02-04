from fastapi import APIRouter
from app.services import get_image_path, delete_image

router = APIRouter()

@router.get("/images/{filename}")
def get_image(filename: str):
    return get_image_path(filename)

@router.delete("/predict/{filename}")
async def delete_image_endpoint(filename: str):
    return delete_image(filename)
