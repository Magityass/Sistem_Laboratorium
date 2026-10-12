from models.transaksi import Transaksi
from models.item_peminjaman import ItemPeminjaman
from datetime import datetime

class ManajemenTransaksi:
    def __init__(self):
        self.data = {}
        self._id_counter = 1

    def buat_transaksi(self, mahasiswa, daftar_alat):
        id_trx = f"TRX{self._id_counter:03d}"
        transaksi = Transaksi(id_trx, mahasiswa)
        
        for alat in daftar_alat:
            if alat.bisa_dipinjam():
                alat.status = "Dipinjam"
                item = ItemPeminjaman(alat)
                transaksi.tambah_item(item)
        
        if transaksi.items:
            mahasiswa.status_peminjaman = True
            self.data[id_trx] = transaksi
            self._id_counter += 1
            return transaksi
        return None

    def proses_pengembalian(self, id_transaksi, kondisi_kembali_dict):
        trx = self.data.get(id_transaksi)
        if trx and trx.is_aktif():
            for item in trx.items:
                if item.status == "Dipinjam":
                    item.status = "Dikembalikan"
                    item.tanggal_kembali = datetime.now().strftime("%Y-%m-%d %H:%M")
                    
                    kondisi_baru = kondisi_kembali_dict.get(item.alat.kode, "Baik")
                    item.kondisi_kembali = kondisi_baru
                    item.alat.ubah_kondisi(kondisi_baru)
                        
            trx.perbarui_status()
            return True
        return False

    def cari_berdasarkan_mahasiswa(self, nim):
        return [trx for trx in self.data.values() if trx.mahasiswa.nim == nim and trx.is_aktif()]
