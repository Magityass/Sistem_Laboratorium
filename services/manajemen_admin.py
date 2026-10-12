from typing import Dict, Optional
from models.admin import Admin

class ManajemenAdmin:
    def __init__(self) -> None:
        self.__data: Dict[str, Admin] = {}

    @property
    def data(self) -> Dict[str, Admin]:
        return self.__data

    def verifikasi_login(self, username: str, password: str) -> bool:
        admin = self.__data.get(username)
        if admin is None:
            return False
        return admin.login(username, password)

    def tambah(self, admin: Admin) -> bool:
        if admin.username in self.__data:
            return False
        self.__data[admin.username] = admin
        return True

    def cari(self, username: str) -> Optional[Admin]:
        return self.__data.get(username)

    def edit(self, username: str, password_baru: str) -> bool:
        if username in self.__data:
            self.__data[username].password = password_baru
            return True
        return False

    def hapus(self, username: str) -> bool:
        if username in self.__data:
            del self.__data[username]
            return True
        return False
