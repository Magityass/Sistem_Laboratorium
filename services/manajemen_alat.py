class ManajemenAlat:
    def __init__(self):
        self.data = {}
        self.daftar_kategori = ["PC Desktop", "Laptop", "Monitor", "Aksesoris (Keyboard/Mouse)", "Jaringan & Kabel", "Proyektor/Presentasi"]

    def tambah(self, alat):
        self.data[alat.kode] = alat

    def edit(self, kode, nama=None, kategori=None, kondisi=None, status=None):
        alat = self.cari(kode)
        if alat:
            if nama: alat.nama = nama
            if kategori: alat.kategori = kategori
            if kondisi: alat.ubah_kondisi(kondisi)
            if status: alat.status = status
            return True
        return False

    def hapus(self, kode):
        if kode in self.data:
            del self.data[kode]
            return True
        return False

    def cari(self, kode):
        return self.data.get(kode)
