# Sistem Peminjaman Laboratorium CLI

Aplikasi CLI (Command Line Interface) berbasis Python untuk mengelola operasional peminjaman alat di laboratorium. Proyek ini dibangun dengan menerapkan prinsip *Object-Oriented Programming* (OOP) tingkat lanjut, termasuk *Inheritance*, *Composition*, dan *Facade/Controller Pattern*. 

## 📁 Struktur Proyek

```text
sistem-peminjaman-lab/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── admin.py
│   ├── staff.py
│   ├── asisten_lab_mahasiswa.py
│   ├── mahasiswa.py
│   ├── alat.py
│   ├── transaksi.py
│   └── item_peminjaman.py
│
├── services/
│   ├── __init__.py
│   ├── manajemen_admin.py
│   ├── manajemen_mahasiswa.py
│   ├── manajemen_alat.py
│   ├── manajemen_transaksi.py
│   └── sistem_peminjaman.py
│
└── ui/
    ├── __init__.py
    └── menu_cli.py