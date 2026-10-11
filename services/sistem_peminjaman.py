class SistemPeminjaman:
    def __init__(self) -> None:
        self.__manajemen_admin = ManajemenAdmin()
        self.__manajemen_mahasiswa = ManajemenMahasiswa()
        self.__manajemen_alat = ManajemenAlat()
        self.__manajemen_transaksi = ManajemenTransaksi()
        self.__user_aktif: Optional[Union[Admin, Mahasiswa]] = None
        self.__berjalan: bool = False


    def manajemen_admin(self) -> ManajemenAdmin:
        return self.__manajemen_admin

   def manajemen_mahasiswa(self) -> ManajemenMahasiswa:
        return self.__manajemen_mahasiswa

    def manajemen_alat(self) -> ManajemenAlat:
        return self.__manajemen_alat

    def manajemen_transaksi(self) -> ManajemenTransaksi:
        return self.__manajemen_transaksi

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
        from UI.menu_cli import MenuCLI

        menu = MenuCLI(self)
        self.__berjalan = True

        while self.__berjalan:
            if self.__user_aktif is None:
                menu.tampilkan_login()
            elif isinstance(self.__user_aktif, Admin):
                menu.tampilkan_menu_admin()
            else:
                menu.tampilkan_menu_mahasiswa()
            menu.proses_input()

    def logout(self) -> None:
        self.__user_aktif = None

    def keluar(self) -> None:
        """Menghentikan loop run()."""
        self.__user_aktif = None
        self.__berjalan = False
