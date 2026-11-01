class ItemPeminjaman:
    def __init__(self, alat):
        self.alat = alat
        self.status = "Dipinjam"
        self.kondisi_kembali = None
        self.tanggal_kembali = None
