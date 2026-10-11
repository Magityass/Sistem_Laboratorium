from typing import Dict, Optional
from models.admin import Admin
class ManajemenAdmin:
    def __init__(self) -> None:
        self.__data: Dict[str, Admin] = {}
      
    def verifikasi_login(self, username: str, password: str):
        admin = self.__data.get(username)
        if admin is None:
            return False
        return admin.login(username, password)
      
    def tambah(self, admin: Admin):
        if admin.username in self.__data:
            return False
        self.__data[admin.username] = admin
        return True
      
    def cari(self, username: str):
        return self.__data.get(username)
