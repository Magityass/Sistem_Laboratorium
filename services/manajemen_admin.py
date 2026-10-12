from typing import Dict, Optional
from models.admin import Admin

class ManajemenAdmin:
    def __init__(self) -> None:
        self.__data: Dict[str, Admin] = {}

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

    def tampilkan_semua(self) -> bool:
        if not self.__data:
            print("[-] Belum ada data admin/staff.")
            return False

        print("\n=== DAFTAR ADMIN & STAFF ===")
        print("-" * 65)
        print(f"| {'ID / NIP / NIM':<18} | {'Username':<15} | {'Jabatan':<20} |")
        print("-" * 65)

        for admin in self.__data.values():
            print(f"| {admin.id_admin:<18} | {admin.username:<15} | {admin.jabatan:<20} |")

        print("-" * 65)
        return True