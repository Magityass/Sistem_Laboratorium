class ManajemenAdmin:
    def __init__(self):
        self.data = {}

    def verifikasi_login(self, username, password):
        admin = self.cari(username)
        if admin and admin.login(username, password):
            return admin
        return None

    def tambah(self, admin):
        if admin.username in self.data:
            return False
        self.data[admin.username] = admin
        return True

    def cari(self, username):
        return self.data.get(username)

    def edit(self, username, password_baru):
        admin = self.cari(username)
        if admin:
            admin.password = password_baru
            return True
        return False

    def hapus(self, username):
        if username in self.data:
            del self.data[username]
            return True
        return False

    def tampilkan_semua(self):
        if not self.data:
            print("[-] Belum ada data admin.")
            return False

        print("\n=== DAFTAR ADMIN / STAFF ===")
        print("-" * 52)
        print(f"| {'NIP':<10} | {'Username':<15} | {'Jabatan':<15} |")
        print("-" * 52)

        for admin in self.data.values():
            print(
                f"| {admin.id_admin:<10} | {admin.username:<15} | {admin.jabatan:<15} |"
            )

        print("-" * 52)
        return True
