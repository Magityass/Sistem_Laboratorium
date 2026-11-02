# Sistem Peminjaman Laboratorium CLI

Aplikasi CLI (Command Line Interface) berbasis Python untuk mengelola operasional peminjaman alat di laboratorium. Proyek ini dibangun dengan menerapkan prinsip *Object-Oriented Programming*

## 📁 Struktur Proyek

```text
Sistem_Laboratorium/
├── admin.py                  # Base class / Parent class Admin
├── alat.py                   # Entitas Alat/Aset Lab
├── asisten_lab_mahasiswa.py  # Child class turunan dari Admin
├── item_peminjaman.py        # Relasi komposisi detail kondisi alat per transaksi
├── mahasiswa.py              # Entitas Mahasiswa
├── main.py                   # Entry point aplikasi & inisialisasi Dummy Data
├── manajemen_admin.py        # Layanan CRUD Admin
├── manajemen_alat.py         # Layanan CRUD Alat
├── manajemen_mahasiswa.py    # Layanan CRUD Mahasiswa
├── manajemen_transaksi.py    # Layanan pemrosesan peminjaman & pengembalian
├── menu_cli.py               # View/UI untuk interaksi pengguna di terminal
├── README.md                 # Dokumentasi
├── requirements.txt          # Daftar dependensi modul
├── sistem_peminjaman.py      # Facade pattern penggabung seluruh layanan (Core System)
├── staff.py                  # Child class turunan dari Admin (Staff Lab)
└── transaksi.py              # Entitas Transaksi utama