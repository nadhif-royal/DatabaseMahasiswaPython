# 🎓 Database Mahasiswa

## 📌 Deskripsi
**Database Mahasiswa** adalah proyek Python untuk mengelola data mahasiswa berbasis file teks.  
Proyek ini dibuat dalam rangka **Day 19-20 dari bootcamp Code Marathon - 30 Days of Code with Python** by KelasBagus.  

Sistem ini memungkinkan pengguna untuk **menyimpan, menampilkan, memperbarui, dan menghapus** data mahasiswa menggunakan file sebagai penyimpanan.

## ⚙️ Fitur
✅ Menambahkan mahasiswa baru  
✅ Menampilkan semua mahasiswa  
✅ Menghapus mahasiswa berdasarkan NIM  
✅ Mencari mahasiswa berdasarkan NIM  
✅ Memperbarui data mahasiswa (Nama/NIM)  

---

## 🛠️ Cara Menggunakan

### 1️⃣ Clone Repository
```sh
git clone https://github.com/nadhif-royal/DatabaseMahasiswaPython.git
cd DatabaseMahasiswaPython
```

### 2️⃣ Jalankan Program
Pastikan sudah menginstal Python 3 lalu jalankan:
```sh
python Database_Mahasiswa.py
```
### 🔄 Hapus file nama.txt dan nim.txt
Kedua file ini dapat anda hapus untuk merestart ulang program dan akan di generate kembali secara otomatis oleh program saat user menambahkan data mahasiswa baru.

### 📂 Struktur Proyek
```sh
/DatabaseMahasiswaPython
│── Day19-20_Project3/
│   ├── Database_Mahasiswa.py
│   ├── nama.txt
│   ├── nim.txt
│── README.md
│── LICENSE
```

## 🏁 Alur Program Utama (Database_Mahasiswa.py)
Program akan memeriksa apakah file nama.txt dan nim.txt ada.
- Jika tidak, akan dibuat otomatis.
- kedua file ini (nama.txt dan nim.txt) berfungsi untuk menyimpan data mahasiswa berupa nama dan nim.
- Keduanya disusun sejajar, sehingga baris ke-1 dalam nama.txt cocok dengan baris ke-1 dalam nim.txt.
  
Terdapat menu utama yaitu:
- Tambah Mahasiswa
- Tampilkan Data Mahasiswa
- Hapus Mahasiswa
- Update Mahasiswa

User dapat mengubah kode sesuai kebutuhan dengan pilihan menu utama diatas. Hasil dari perubahan akan langsung disimpan dalam file nama.txt dan nim.txt.
