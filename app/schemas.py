from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema untuk User
class UserBase(BaseModel):
    username: str
    nik: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Schema untuk Nutrition
class NutritionBase(BaseModel):
    nama_makanan: str
    gambar: Optional[str]
    kalori: Optional[int]
    protein: Optional[int]
    karbo: Optional[int]
    lemak: Optional[int]
    judul_deskripsi: Optional[str]
    isi_deskripsi: Optional[str]

class NutritionCreate(NutritionBase):
    user_id: int

class Nutrition(NutritionBase):
    id: int
    created_at: datetime
    user: User

    class Config:
        orm_mode = True