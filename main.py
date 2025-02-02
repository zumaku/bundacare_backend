from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_user, get_users, create_nutrition, get_nutritions, get_nutrition_by_date
from app.schemas import UserCreate, NutritionCreate, User, Nutrition
from datetime import datetime
from typing import List
from pathlib import Path
import shutil
import uuid

# Direktori penyimpanan gambar
IMAGE_DIR = Path("data/images")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)    # Buat folder jika belum ada


app = FastAPI()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def welcome():
    return {"message": "BundaCare API is running!"}

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


'''
# Predict endpoint
riq => image & res => nutritions & descriptions

1. Menerima request image
2. Menjalankan model prediksi nutrisi
3. Mendapatkan hasil prediksi nutrisi
4. Menyimpan image di server
5. Mengirim image dan hasil prediksi ke llm
6. Memperoleh judul deskripsi dari llm
7. Memperoleh isi deskripsii dari llm
8. Mengembalikan data nutrisi, deskripsi, dan nama image.

# Try curl -X 'POST' 'http://127.0.0.1:8000/predict' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@./bojobaru.png'
'''
@app.post("/predict")
async def upload_image(file: UploadFile = File(...)):
    # Pastikan hanya menerima file gambar
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="File harus berupa gambar (JPEG/PNG)")

    # Buat nama file acak menggunakan UUID
    file_extension = file.filename.split(".")[-1]
    random_filename = f"{uuid.uuid4()}.{file_extension}"

    # Path penyimpanan
    file_path = IMAGE_DIR / random_filename

    # Simpan gambar
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    '''
    # Jalankan fungsi prediksi
    Fungsi tersebut untuk mendapatkan nilai kalori, protein, karbo, dan lemak
    '''
    kalori = 40
    protein = 4
    karbo = 15
    lemak = 5
    
    '''
    # Jalankan fungsi get prediksi
    Fungsi ini akan melempar data nutrisi yang didapat ke Gemini
    untuk mendapatkan nilai judul deskripsi dan isi deskripsinya.
    '''
    judul_deskripsi = 'Tumis Brokoli dan Wortel'
    isi_deskripsi = 'Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A. Makanan ini rendah kalori dan lemak.'
    
    # Mempersiapkan data yang didapat
    data = {
        "kalori": kalori,
        "protein": protein,
        "karbo": karbo,
        'lemak': lemak,
        'judul_deskripsi': judul_deskripsi,
        'isi_deskripsi': isi_deskripsi
    }
    
    # Mengembalikan data ke client
    return {"nama_gambar": random_filename, "data": data}

'''
# Delete image prediction endpoint
req => image

1. Mengklik hapus
2. Menerima nama image yang akan dihapus
3. Menghapus image di server
4. Mengembalikan status ok
'''