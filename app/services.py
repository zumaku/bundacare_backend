import os
import uuid
import shutil
from pathlib import Path
from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse

IMAGE_DIR = Path("data/images/")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)  # Pastikan folder ada

'''
===================================
|         IMAGE SERVICES          |
===================================
'''

async def save_image(file: UploadFile) -> str:
    """Menyimpan gambar dengan nama acak dan mengembalikan nama file."""
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="File harus berupa gambar (JPEG/PNG)")

    file_extension = file.filename.split(".")[-1]
    random_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = IMAGE_DIR / random_filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return random_filename

def get_image_path(filename: str):
    """Mengembalikan response file jika tersedia."""
    file_path = IMAGE_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

def delete_image(filename: str):
    """Menghapus gambar berdasarkan nama file."""
    file_path = IMAGE_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        file_path.unlink()
        return {"message": f"File '{filename}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")
