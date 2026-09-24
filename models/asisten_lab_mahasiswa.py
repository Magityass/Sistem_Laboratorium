from admin import Admin

class AsistenLabMahasiwa(Admin):
    def __init__(self, nim, username,password, jabatan="Asisten Lab"):
        super().__init__(
            id_admin=nim,
            username=username,
            password=password,
            jabatan=jabatan
        )
        self.nim = nim