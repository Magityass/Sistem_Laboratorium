from typing import Optional, Union
from services.manajemen_admin import ManajemenAdmin
from services.manajemen_mahasiswa import ManajemenMahasiswa
from services.manajemen_alat import ManajemenAlat
from services.manajemen_transaksi import ManajemenTransaksi
from models.admin import Admin
from models.mahasiswa import Mahasiswa

class SistemPeminjaman:
    def __init__(self) -> None:
        self.__manajemen_admin = ManajemenAdmin()
        self.__manajemen_mahasiswa = ManajemenMahasiswa()
        self.__manajemen_alat = ManajemenAlat()
        self.__manajemen_transaksi = ManajemenTransaksi()
        self.__user_aktif: Optional[Union[Admin, Mahasiswa]] = None
        self.__berjalan: bool = False

    @property
    def manajemen_admin(self) -> ManajemenAdmin:
        return self.__manajemen_admin

    @property
    def manajemen_mahasiswa(self) -> ManajemenMahasiswa:
        return self.__manajemen_mahasiswa

    @property
    def manajemen_alat(self) -> ManajemenAlat:
        return self.__manajemen_alat

    @property
    def manajemen_transaksi(self) -> ManajemenTransaksi:
        return self.__manajemen_transaksi

    @property
    def user_aktif(self) -> Optional[Union[Admin, Mahasiswa]]:
        return self.__user_aktif

    def login_admin(self, username: str, password: str) -> bool:
        if not self.__manajemen_admin.verifikasi_login(username, password):
            return False
        self.__user_aktif = self.__manajemen_admin.cari(username)
        return self.__user_aktif is not None

    def login_mahasiswa(self, nim: str, nama: str) -> bool:
        if not self.__manajemen_mahasiswa.verifikasi_login(nim, nama):
            return False
        self.__user_aktif = self.__manajemen_mahasiswa.cari(nim)
        return self.__user_aktif is not None

    def run(self) -> None:
        from ui.menu_cli import MenuCLI

        menu = MenuCLI(self)
        self.__berjalan = True

        while self.__berjalan:
            if self.__user_aktif is None:
                menu.tampilkan_login()
            elif isinstance(self.__user_aktif, Admin):
                menu.tampilkan_menu_admin()
            else:
                menu.tampilkan_menu_mahasiswa()

    def logout(self) -> None:
        self.__user_aktif = None

    def keluar(self) -> None:
        """Menghentikan loop run()."""
        self.__user_aktif = None
        self.__berjalan = False
