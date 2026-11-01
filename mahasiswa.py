class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.status_peminjaman = False

    def login(self, nim, nama):
        return self.nim == nim and self.nama == nama