from datetime import datetime, timedelta
class Transaksi:

    def __init__(self, id_transaksi: str, mahasiswa, daftar_item: list):
        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.daftar_item = daftar_item
        self.tanggal_pinjam = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.batas_kembali = (datetime.now() + timedelta(days=7)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.status = "dipinjam"

    def perbarui_status(self) -> None:
        status_item = [item.status for item in self.daftar_item]

        if all(s == "dikembalikan" for s in status_item):
            self.status = "selesai"
        elif any(s == "dikembalikan" for s in status_item):
            self.status = "sebagian dikembalikan"
        else:
            self.status = "dipinjam"

    def is_aktif(self) -> bool:
        return self.status != "selesai"