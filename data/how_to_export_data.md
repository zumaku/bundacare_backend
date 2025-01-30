Untuk mengekstrak (export) data dari PostgreSQL, kamu bisa menggunakan beberapa metode berikut:

---

### **1. Menggunakan `pg_dump` (Untuk Backup Seluruh Database)**
Jika ingin mengekspor seluruh database, gunakan perintah berikut di terminal:

```sh
pg_dump -U your_username -d your_database -F c -f backup_file.dump
```
> **Penjelasan:**
> - `-U your_username` → Ganti `your_username` dengan nama user PostgreSQL.
> - `-d your_database` → Ganti `your_database` dengan nama database yang ingin diekspor.
> - `-F c` → Format custom yang bisa digunakan untuk backup dan restore.
> - `-f backup_file.dump` → Nama file hasil backup.

Untuk mengembalikan data dari backup, gunakan:
```sh
pg_restore -U your_username -d your_database -1 backup_file.dump
```

---

### **2. Mengekspor Data dalam Format SQL**
Jika hanya ingin mengekspor struktur dan isi database dalam format SQL, gunakan:

```sh
pg_dump -U your_username -d your_database -F p -f backup.sql
```
> **Penjelasan:**
> - `-F p` → Format SQL yang bisa langsung dijalankan di PostgreSQL.

Untuk mengimpor kembali:
```sh
psql -U your_username -d your_database -f backup.sql
```

---

### **3. Mengekspor Data dalam Format CSV**
Jika hanya ingin mengekspor data dari tabel tertentu ke format CSV:

```sh
COPY your_table TO '/path/to/output.csv' WITH CSV HEADER;
```
> **Pastikan path yang digunakan bisa diakses PostgreSQL.**

Untuk mengimpor kembali CSV ke tabel:
```sh
COPY your_table FROM '/path/to/input.csv' WITH CSV HEADER;
```

---

### **4. Menggunakan `SELECT` dengan Output ke File**
Jika hanya ingin menyimpan hasil query ke file:
```sh
\o output.txt
SELECT * FROM your_table;
\o
```
> **Penjelasan:**
> - `\o output.txt` → Menyimpan output ke file `output.txt`
> - `SELECT * FROM your_table;` → Query yang ingin dieksekusi
> - `\o` → Mengembalikan output ke layar terminal

---

Jika kamu ingin mengekstrak data dengan cara tertentu, beri tahu aku lebih detail agar aku bisa memberikan solusi yang lebih sesuai! 😊