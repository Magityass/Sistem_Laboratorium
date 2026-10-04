from __future__ import annotations
from datetime import datetime
from typing import Optional
from .alat import Alat

class ItemPeminjaman:
    STATUS_DIPINJAM = "Dipinjam"
    STATUS_DIKEMBALIKAN = "Dikembalikan"
    KONDISI_PENGEMBALIAN_VALID = ("Baik", "Rusak Ringan", "Rusak Berat")

    def __init__(self, alat: Alat) -> None:
        self.alat: Alat = alat
        self.transaksi = transaksi
        self.status: str = self.STATUS_DIPINJAM
        self.kondisi_kembali: Optional[str] = None
        self.tanggal_kembali: Optional[datetime] = None

    def proses_kembali(self, kondisi_baru: str) -> None:
        if self.is_dikembalikan():
            raise ValueError(
                f"Alat {self.alat.kode} pada item ini sudah "
                "dikembalikan sebelumnya."
            )
        if kondisi_baru not in self.KONDISI_PENGEMBALIAN_VALID:
            raise ValueError(
                f"Kondisi '{kondisi_baru}' tidak valid untuk pengembalian. "
                f"Pilihan: {self.KONDISI_PENGEMBALIAN_VALID}"
            )

        self.status = self.STATUS_DIKEMBALIKAN
        self.kondisi_kembali = kondisi_baru
        self.tanggal_kembali = datetime.now()
        self.alat.ubah_kondisi(kondisi_baru)

    def is_dikembalikan(self) -> bool:
        return self.status == self.STATUS_DIKEMBALIKAN

    def is_aktif(self) -> bool:
        return self.status == self.STATUS_DIPINJAM

    def __str__(self) -> str:
        baris = f"{self.alat.nama} ({self.alat.kode}) - {self.status}"
        if self.is_dikembalikan():
            tanggal = (
                self.tanggal_kembali.strftime("%d-%m-%Y")
                if self.tanggal_kembali
                else "-"
            )
            baris += f" | Kondisi: {self.kondisi_kembali} | Tgl kembali: {tanggal}"
        return baris

    def __repr__(self) -> str:
        return f"ItemPeminjaman(alat={self.alat.kode!r}, status={self.status!r})"
