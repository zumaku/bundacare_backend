from fastapi import APIRouter, UploadFile, File, HTTPException
from app.gcs import upload_to_gcs, delete_from_gcs
import uuid

router = APIRouter()

@router.post("/predict")
async def upload_image(file: UploadFile = File(...)):
    '''
    Example cURL:
    curl -X 'POST' 'http://127.0.0.1:8000/predict' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@spark.jpg'
    '''
    # Pastikan hanya menerima file gambar (JPEG/PNG)
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="File harus berupa gambar (JPEG/PNG)")

    # Upload gambar ke Google Cloud Storage
    file_extension = file.filename.split(".")[-1]
    random_filename = f"{uuid.uuid4()}.{file_extension}"
    image_url = upload_to_gcs(file.file, random_filename, file.content_type)

    # Simulasi hasil prediksi
    data = {
        "kalori": 40,
        "protein": 4,
        "karbo": 15,
        "lemak": 5,
        "judul_deskripsi": "Tumis Brokoli dan Wortel",
        "isi_deskripsi": "Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A."
    }

    return {"gambar_url": image_url, "data": data}

@router.delete("/predict/{filename}")
async def delete_image(filename: str):
    return delete_from_gcs(filename)