class Alat:
    PILIHAN_KONDISI = ["Baik", "Rusak Ringan", "Rusak Berat", "Dalam Perbaikan"]

    def __init__(self, kode, nama, kategori, kondisi="Baik", status="Tersedia"):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.kondisi = kondisi if kondisi in self.PILIHAN_KONDISI else "Baik"
        self.status = status

    def bisa_dipinjam(self):
        return self.kondisi == "Baik" and self.status == "Tersedia"
        
    def ubah_kondisi(self, kondisi_baru):
        if kondisi_baru in self.PILIHAN_KONDISI:
            self.kondisi = kondisi_baru
            
            if self.kondisi != "Baik" and self.status == "Tersedia":
                self.status = "Tidak Tersedia"
            elif self.kondisi == "Baik" and self.status == "Tidak Tersedia":
                self.status = "Tersedia"
                
            return True
        return False