import os
from google.cloud import storage
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta, datetime

# Load environment variables from .env
load_dotenv()

# Ambil konfigurasi dari .env
GCS_KEY_PATH = os.getenv("GCS_KEY_PATH")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")

# Pastikan kredensial tersedia
if not GCS_KEY_PATH or not GCS_BUCKET_NAME:
    raise ValueError("Variabel lingkungan GCS belum dikonfigurasi dengan benar!")

# Inisialisasi klien GCS dengan kredensial dari file JSON
storage_client = storage.Client.from_service_account_json(GCS_KEY_PATH)
bucket = storage_client.bucket(GCS_BUCKET_NAME)

def upload_to_gcs(file, filename: str, content_type: str):
    """Mengunggah file ke Google Cloud Storage dan menghasilkan URL yang ditandatangani."""
    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=content_type)

    # Generate signed URL with 1 hour expiry
    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(hours=1),
        method="GET",  # Allow GET requests (for reading)
        # content_type=content_type # Set content type for proper handling
    )

    return url  # Mengembalikan URL yang ditandatangani

def delete_from_gcs(filename):
    """Menghapus file dari Google Cloud Storage."""
    blob = bucket.blob(filename)
    blob.delete()
    return {"message": f"File '{filename}' dihapus dari GCS"}