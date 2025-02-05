

# **API Documentation: BundaCare**

> ## **📌 List Konten**
> - [**📄 Deskripsi Proyek**](#📄-deskripsi-proyek)
> - [**📂 Struktur Folder**](#📂-struktur-folder)
> - [**▶️ Cara Menggunakan**](#▶️-cara-menggunakan)
> - [**🎯 Endpoints**](#🎯-endpoints)
> 

## **📄 Deskripsi Proyek**
BundaCare adalah aplikasi backend berbasis FastAPI untuk manajemen nutrisi harian ibu hamil yang memiliki fitur prediksi nutrisi makanan harian, chatbot intteraktif, dan monitoring tenaga kesehatan secara real time.

Pengembang:
- Zul Fadli Ahmad
- Nursyamsu Rijal Usman
- Isla Inayah Bahar

## **📂 Struktur Folder**
Berikut adalah struktur direktori dalam proyek ini:

```
.
├── .venv/                  # Virtual environment (opsional)
├── app/
│   ├── routers/           # Folder untuk endpoint (API routes)
│   |   ├── home.py        # Endpoint untuk root API
│   |   ├── nutrition.py   # Endpoint untuk nutrisi
│   |   ├── predict.py     # Endpoint untuk prediksi gambar
│   |   └── user.py        # Endpoint untuk user
|   |
│   ├── crud.py            # Operasi CRUD untuk database
│   ├── database.py        # Konfigurasi database (SQLAlchemy)
│   ├── gcs.py             # Interaksi dengan Google Cloud Storage (jika ada)
│   ├── models.py          # Model database dengan SQLAlchemy
│   └── schemas.py         # Skema Pydantic untuk validasi data
│
├── config/
│   └── gsc-key.json       # Berisi konfigurasi Google Cloud Storage
|
├── data/
│   ├── images/            # Folder untuk menyimpan gambar
│   ├── backup_file.dump   # File backup database
│   ├── backup.sql         # SQL dump untuk restore database
│   └── how_to_export_data.md  # Panduan ekspor data
│
├── docs/
│   └── api/               # Dokumentasi API
│       ├── thunder-collection_bundacare.json # Koleksi Thunder Client/Postman
│       └── thunder-collection_postman_bundacare.json
│
├── .env                   # File konfigurasi environment
├── .env.example           # Template konfigurasi environment
├── .gitignore             # File untuk mengabaikan file tertentu dalam Git
├── main.py                # Entry point aplikasi FastAPI
├── README.md              # Dokumentasi utama proyek
└── requirements.txt       # Daftar dependensi Python
```

### **1. `app/`**
Berisi kode utama backend:
- `crud.py`: Berisi fungsi CRUD untuk database.
- `database.py`: Mengatur koneksi database menggunakan SQLAlchemy.
- `models.py`: Definisi model database.
- `schemas.py`: Validasi data menggunakan Pydantic.

### **2. `config/`**
Folder untuk penyimpanan file konfigurasi:
- `gcs-key.json`: File konfigurasi Google Cloud Storage.

### **3. `data/`**
Folder untuk penyimpanan data tambahan:
- `images/`: Direktori penyimpanan gambar.
- `backup.sql`: File untuk backup dan restore database.
- `how_to_export_data.md`: Panduan ekspor data.

### **4. `docs/`**
Folder yang berisi dokumentasi API:
- `api/`: Koleksi API untuk Postman dan Thunderclient dalam format JSON.

### **5. `main.py`**
File utama untuk menjalankan aplikasi FastAPI.

### **6. `requirements.txt`**
File yang berisi daftar dependensi yang perlu diinstal dengan `pip install -r requirements.txt`.

### **7. `.env & .env.example`**
File untuk menyimpan konfigurasi environment seperti database URL, secret key, dll.

## **▶️ Cara Menggunakan**
1. Sebelum menjalankan FastAPI, pastikan Anda telah menginstal:
    - Python (>= 3.8)
    - pip (Python package manager)
    - Virtual environment (opsional, tetapi disarankan)
2. Buat virtual environment dan aktifkan:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   venv\Scripts\activate     # Untuk Windows
   ```
3. Instal dependensi:
   ```sh
   pip install -r requirements.txt
   ```
4. Buat file `.env`:
   ```sh
   cp .env.example .env
   # Isikan dipendensi environment yang dibutuhkan di file `.env`
   ```
5. Jalankan aplikasi FastAPI:
   ```sh
   python3 uvicorn main:app --reload    # Untuk macOS/Linux
   python uvicorn main:app --reload     # Untuk Windows
   ```
6. Akses API di browser:
   - Base URL: `http://127.0.0.1:8000`
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - Redoc: `http://127.0.0.1:8000/redoc`


## **🎯 Endpoints**

**Base URL** `http://127.0.0.1:8000`

### **0. Welcome**
- **URL** `/`
- **Method:** `GET`
- **Description:** Mengecek status layanan.

##### **Response**  
```json
{
  "message": "BundaCare API is running!"
}
```

---

### **1. Users**

#### **1.1. Get All Users**  
- **URL:** `/users`  
- **Method:** `GET`  
- **Description:** Mendapatkan semua data pengguna.

##### **Response**  
```json
[
  {
    "username": "zuma",
    "nik": "1234",
    "id": 1,
    "created_at": "2025-01-25T10:32:11"
  },
  {
    "username": "ijal",
    "nik": "4321",
    "id": 2,
    "created_at": "2025-01-25T10:37:52"
  },
  {
    "username": "isla",
    "nik": "1212",
    "id": 3,
    "created_at": "2025-01-25T10:37:54"
  }
]
```

---

#### **1.2. Create User**  
- **URL:** `/users`  
- **Method:** `POST`  
- **Description:** Membuat pengguna baru.
- **Headers:**  
  - `Content-Type: application/json`
- **Body:**  
```json
{
    "username": "hua",
    "nik": "1234",
    "password": "admin"
}
```

---

### **2. Nutritions**

#### **2.1. Get All Nutritions**  
- **URL:** `/nutritions`  
- **Method:** `GET`  
- **Description:** Mendapatkan semua data nutrisi.

##### **Response**  
```json
[
  {
    "nama_makanan": "Nasi Goreng",
    "gambar": "nasi_goreng.jpg",
    "kalori": 400,
    "protein": 10,
    "karbo": 50,
    "lemak": 15,
    "judul_deskripsi": "Makanan favorit",
    "isi_deskripsi": "Nasi goreng adalah makanan khas Indonesia.",
    "id": 1,
    "created_at": "2025-01-25T10:33:07",
    "user": {
      "username": "zuma",
      "nik": "1234",
      "id": 1,
      "created_at": "2025-01-25T10:32:11"
    }
  },
  ...
]
```

---

#### **2.2. Get Nutrition by Date**  
- **URL:** `/nutritions/date/{date}`  
- **Method:** `GET`  
- **Description:** Mendapatkan data nutrisi berdasarkan tanggal tertentu.
- **Example:**  
  - `/nutritions/date/2025-01-30`

##### **Response**  
```json
[
  {
    "nama_makanan": "Nasi Goreng",
    "gambar": "nasi_goreng.jpg",
    "kalori": 400,
    "protein": 10,
    "karbo": 50,
    "lemak": 15,
    "judul_deskripsi": "Makanan favorit",
    "isi_deskripsi": "Nasi goreng adalah makanan khas Indonesia.",
    "id": 1,
    "created_at": "2025-01-25T10:33:07",
    "user": {
      "username": "zuma",
      "nik": "1234",
      "id": 1,
      "created_at": "2025-01-30T10:32:11"
    }
  },
  ...
]
```

---

#### **2.3. Create Nutrition**  
- **URL:** `/nutritions`  
- **Method:** `POST`  
- **Description:** Menambahkan data nutrisi baru.
- **Headers:**  
  - `Content-Type: application/json`
- **Body:**  
```json
{
  "nama_makanan": "Nasi Kuning",
  "gambar": "nasi_kuning.jpg",
  "kalori": 350,
  "protein": 16,
  "karbo": 40,
  "lemak": 13,
  "judul_deskripsi": "Makanan favorit",
  "isi_deskripsi": "Nasi kuning adalah makanan enak.",
  "user_id": 1
}
```

##### **Response**  
```json
{
  "nama_makanan": "Nasi Kuning",
  "gambar": "nasi_kuning.jpg",
  "kalori": 350,
  "protein": 16,
  "karbo": 40,
  "lemak": 13,
  "judul_deskripsi": "Makanan favorit",
  "isi_deskripsi": "Nasi kuning adalah makanan enak.",
  "id": 22,
  "created_at": "2025-02-02T09:43:59.325375",
  "user": {
    "username": "zuma",
    "nik": "1234",
    "id": 1,
    "created_at": "2025-01-25T10:32:11"
  }
}
```

---

### **3. Predictions**

#### **3.1. Predict Image**  
- **URL:** `/predict`  
- **Method:** `POST`  
- **Description:** Mengunggah gambar untuk prediksi.
- **Headers:**  
  - `Content-Type: multipart/form-data`
- **Body:**  
  - File gambar yang akan diprediksi.

##### **cURL Example**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/predict' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@data/image/img_example.png'
```

##### **Response**  
```json
{
  "gambar_url":"https://storage.googleapis.com/bundacare_docs/e1e8721b-7bcb-4411-950b-4a4aac2803cb.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=bundacare-storage-service%40sparkdatathon-2025-student-7.iam.gserviceaccount.com%2F20250205%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250205T144740Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=a9d6d8c5bd8a9810abe7d4742ae548c586570e226a620e6f843ce6c32c99d67bb8fbb302cca31374e0b7899eb5f92e20e94300fc15bb706d74c170c7b401068dc60d3e2427e2bef849c62fc35e9b1d7d0f470b5ee33e7fd39d1b7ada5e2e1d4e1cdae7d9c80e5fee028849470a752dc34fd3bb7c48a1a3a906a6e00699f7cc29886979e371c8c2129eba8c9c493c816bc4b462b832ff85641ec13e66d0e8be52d8add0809d02a39c176ca77cecc4836c6362ac8353ad5cd9efc2f5b68b694c570888fe407fff93fd0d5872413d6f2ee92b4badabd99354a64e108764352fc0dff9427a44d88e9ba093faad3aaaf4bc4fad7dfe3a3672ad05886fa9a507db493a",
  "data":{
    "kalori":40,
    "protein":4,
    "karbo":15,
    "lemak":5,
    "judul_deskripsi":"Tumis Brokoli dan Wortel","isi_deskripsi":"Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A."
  }
}
```

---

#### **3.2. Delete Prediction Image**  
- **URL:** `/predict/{filename}`  
- **Method:** `DELETE`  
- **Description:** Menghapus gambar hasil prediksi.
- **Example:**  
  - Jika `gambar_url` yang didapat dari response server: `https://storage.googleapis.com/bundacare_docs/e1e8721b-7bcb-4411-950b-4a4aac2803cb.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=...&X-Goog-Date=...&X-Goog-Expires=...&X-Goog-SignedHeaders=host&X-Goog-Signature=...`
  - Maka gunakan nama filenya untuk menghapus: `/predict/e1e8721b-7bcb-4411-950b-4a4aac2803cb.png`

##### **cURL Example**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/predict/e1e8721b-7bcb-4411-950b-4a4aac2803cb.png'
```

##### **Response**  
```json
{
  "message": "File '36f95155-f404-4434-b2e7-87fee090dbbc.png' deleted successfully"
}
```