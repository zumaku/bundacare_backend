from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_user, get_users, create_nutrition, get_nutritions, get_nutrition_by_date
from app.schemas import UserCreate, NutritionCreate, User, Nutrition
from datetime import datetime
from typing import List

app = FastAPI()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint User
@app.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/users/", response_model=List[User])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

# Endpoint Nutrition
@app.post("/nutritions/", response_model=Nutrition)
def create_nutrition_endpoint(nutrition: NutritionCreate, db: Session = Depends(get_db)):
    return create_nutrition(db, nutrition)

@app.get("/nutritions/", response_model=List[Nutrition])
def get_nutritions_endpoint(db: Session = Depends(get_db)):
    return get_nutritions(db)

@app.get("/nutritions/date/{date}", response_model=List[Nutrition])
def get_nutrition_by_date_endpoint(date: datetime, db: Session = Depends(get_db)):
    return get_nutrition_by_date(db, date)
