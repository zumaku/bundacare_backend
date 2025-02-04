from fastapi import APIRouter, UploadFile, File
from app.services import save_image

router = APIRouter()

@router.post("/predict")
async def upload_image(file: UploadFile = File(...)):
    random_filename = await save_image(file)

    # Simulasi hasil prediksi
    data = {
        "kalori": 40,
        "protein": 4,
        "karbo": 15,
        'lemak': 5,
        'judul_deskripsi': 'Tumis Brokoli dan Wortel',
        'isi_deskripsi': 'Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A.'
    }
    
    return {"nama_gambar": random_filename, "data": data}
