from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import Nutrition, NutritionCreate
from app.crud import create_nutrition, get_nutritions, get_nutrition_by_date

router = APIRouter()

@router.post("/nutritions/", response_model=Nutrition)
def create_nutrition_endpoint(nutrition: NutritionCreate, db: Session = Depends(get_db)):
    return create_nutrition(db, nutrition)

@router.get("/nutritions/", response_model=List[Nutrition])
def get_nutritions_endpoint(db: Session = Depends(get_db)):
    return get_nutritions(db)

@router.get("/nutritions/date/{date}", response_model=List[Nutrition])
def get_nutrition_by_date_endpoint(date: datetime, db: Session = Depends(get_db)):
    return get_nutrition_by_date(db, date)
