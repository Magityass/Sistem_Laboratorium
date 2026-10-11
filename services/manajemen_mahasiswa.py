class ManajemenMahasiswa:
    def __init__(self) -> None:
        self.__data: Dict[str, Mahasiswa] = {}

    def verifikasi_login(self, username: str, password: str) -> bool:
        mahasiswa = self.__data.get(username)
        if mahasiswa is None:
            return False
        return mahasiswa.login(username, password)

    def tambah(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.nim in self.__data:
            return False
        self.__data[mahasiswa.nim] = mahasiswa
        return True

    def cari(self, nim: str) -> Optional[Mahasiswa]:
        return self.__data.get(nim)
