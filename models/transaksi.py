from datetime import datetime, timedelta

class Transaksi:
    def __init__(self, id_transaksi: str, mahasiswa):
        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.items = []
        self.tanggal_pinjam = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.batas_kembali = (datetime.now() + timedelta(days=7)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.status = "Dipinjam"

    def tambah_item(self, item):
        self.items.append(item)

    def perbarui_status(self) -> None:
        if not self.items:
            return
            
        status_item = [item.status.lower() for item in self.items]

        if all(s == "dikembalikan" for s in status_item):
            self.status = "Selesai"
        elif any(s == "dikembalikan" for s in status_item):
            self.status = "Sebagian Dikembalikan"
        else:
            self.status = "Dipinjam"

    def is_aktif(self) -> bool:
        return self.status.lower() != "selesai"