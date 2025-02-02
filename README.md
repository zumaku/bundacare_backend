# **API Documentation: BundaCare**

## **Base URL**  
`http://127.0.0.1:8000`

## **Endpoints**

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

##### **Response**  
```json
{
  "nama_gambar":"1c2d0a6a-f753-42ca-beb0-5a49c5a6cca6.png",
  "data":{
    "kalori":40,
    "protein":4,
    "karbo":15,
    "lemak":5,
    "judul_deskripsi":"Tumis Brokoli dan Wortel",
    "isi_deskripsi":"Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A. Makanan ini rendah kalori dan lemak."
  }
}
```

---

#### **3.2. Delete Prediction Image**  
- **URL:** `/predict/{image_id}`  
- **Method:** `DELETE`  
- **Description:** Menghapus gambar hasil prediksi.
- **Example:**  
  - `/predict/36f95155-f404-4434-b2e7-87fee090dbbc.png`

##### **Response**  
```json
{
  "message": "File '36f95155-f404-4434-b2e7-87fee090dbbc.png' deleted successfully"
}
```