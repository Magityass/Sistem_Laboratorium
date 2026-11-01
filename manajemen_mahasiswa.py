from typing import Dict, Optional, Union
from models.mahasiswa import Mahasiswa

class ManajemenMahasiswa:
    def __init__(self) -> None:
        self.__data: Dict[str, Mahasiswa] = {}

    @property
    def data(self) -> Dict[str, Mahasiswa]:
        return self.__data

    def verifikasi_login(self, nim: str, nama: str) -> bool:
        mahasiswa = self.__data.get(nim)
        if mahasiswa is None:
            return False
        return mahasiswa.login(nim, nama)

    def tambah(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.nim in self.__data:
            return False
        self.__data[mahasiswa.nim] = mahasiswa
        return True

    def cari(self, nim: str) -> Optional[Mahasiswa]:
        return self.__data.get(nim)

    def edit(self, nim: str, nama_baru: str) -> bool:
        if nim in self.__data:
            self.__data[nim].nama = nama_baru
            return True
        return False

    def hapus(self, nim: str) -> Union[bool, str]:
        if nim in self.__data:
            if self.__data[nim].status_peminjaman:
                return "GAGAL_MASIH_MEMINJAM"
            del self.__data[nim]
            return True
        return False