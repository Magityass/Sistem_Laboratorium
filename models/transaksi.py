from datetime import datetime
from typing import List, Optional


class DetailTransaksi:
    """Class untuk mencatat rincian tiap alat yang dipinjam dalam satu transaksi."""

    def __init__(self, alat):
        self.alat = alat  
        self.is_dikembalikan: bool = False
        self.tgl_kembali: Optional[datetime] = None
        self.kondisi_kembali: Optional[str] = None

    def proses_kembali(self, kondisi_baru: str) -> None:
        """Memproses pengembalian alat dan memperbarui kondisinya."""
        self.is_dikembalikan = True
        self.tgl_kembali = datetime.now()
        self.kondisi_kembali = kondisi_baru
        if hasattr(self.alat, "update_kondisi"):
            self.alat.update_kondisi(kondisi_baru)


class Transaksi:
    """Class induk untuk mencatat header transaksi peminjaman."""

    def __init__(self, id_transaksi: str, mahasiswa, admin):
        self.id_transaksi: str = id_transaksi
        self.mahasiswa = mahasiswa  
        self.admin = admin  
        self.daftar_detail: List[DetailTransaksi] = []
        self.tgl_pinjam: datetime = datetime.now()
        self.status: str = "dipinjam"  

    def tambah_detail_alat(self, alat) -> None:
        """Menambahkan item alat ke dalam transaksi ini."""
        detail = DetailTransaksi(alat)
        self.daftar_detail.append(detail)

    def update_status_transaksi(self) -> None:
        """Memeriksa dan memperbarui status transaksi secara otomatis."""
        if not self.daftar_detail:
            return

        total_item = len(self.daftar_detail)
        item_dikembalikan = sum(1 for detail in self.daftar_detail if detail.is_dikembalikan)

        status_lama = self.status

        if item_dikembalikan == 0:
            self.status = "dipinjam"
        elif item_dikembalikan < total_item:
            self.status = "sebagian_dikembalikan"
        else:
            self.status = "selesai"
    
            if status_lama != "selesai" and getattr(self.mahasiswa, "jumlah_transaksi_aktif", 0) > 0:
                self.mahasiswa.jumlah_transaksi_aktif -= 1