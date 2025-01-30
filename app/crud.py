from sqlalchemy.orm import Session
from app.models import User, Nutrition
from app.schemas import UserCreate, NutritionCreate
from datetime import datetime
from sqlalchemy import func

# CRUD untuk User
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

# CRUD untuk Nutrition
def create_nutrition(db: Session, nutrition: NutritionCreate):
    db_nutrition = Nutrition(**nutrition.dict())
    db.add(db_nutrition)
    db.commit()
    db.refresh(db_nutrition)
    return db_nutrition

def get_nutritions(db: Session):
    return db.query(Nutrition).all()

def get_nutrition_by_date(db: Session, date: datetime):
    return db.query(Nutrition).filter(func.date(Nutrition.created_at) == date).all()
