from models.staff import Staff
from models.mahasiswa import Mahasiswa
from models.alat import Alat
from services.sistem_peminjaman import SistemPeminjaman
from ui.menu_cli import MenuCLI

def inisialisasi_data_dummy(sistem):
    staff_lab = Staff(nip="192837", username="admin", password="123")
    sistem.manajemen_admin.tambah(staff_lab)
    
    mhs1 = Mahasiswa(nim="12345", nama="Andi")
    mhs2 = Mahasiswa(nim="67890", nama="Budi")
    sistem.manajemen_mahasiswa.tambah(mhs1)
    sistem.manajemen_mahasiswa.tambah(mhs2)
    
    alat1 = Alat(kode="PC-01", nama="PC Desktop Dell Optiplex", kategori="PC Desktop")
    alat2 = Alat(kode="LP-01", nama="Laptop Asus ROG", kategori="Laptop")
    alat3 = Alat(kode="PRJ-01", nama="Proyektor Epson", kategori="Proyektor")
    alat4 = Alat(kode="KBL-01", nama="Kabel LAN CAT6 10m", kategori="Jaringan")
    alat5 = Alat(kode="ACC-01", nama="Keyboard Mechanical", kategori="Aksesoris")
    alat6 = Alat(kode="PC-02", nama="PC Desktop HP", kategori="PC Desktop", kondisi="Rusak Ringan", status="Tidak Tersedia")
    
    sistem.manajemen_alat.tambah(alat1)
    sistem.manajemen_alat.tambah(alat2)
    sistem.manajemen_alat.tambah(alat3)
    sistem.manajemen_alat.tambah(alat4)
    sistem.manajemen_alat.tambah(alat5)
    sistem.manajemen_alat.tambah(alat6)

def main():
    sistem = SistemPeminjaman()
    inisialisasi_data_dummy(sistem)
    
    cli = MenuCLI(sistem)
    cli.tampilkan_login()

if __name__ == "__main__":
    main()
