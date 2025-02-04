from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import User, UserCreate
from app.crud import create_user, get_users

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/", response_model=List[User])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)
