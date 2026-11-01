from admin import Admin

class Staff(Admin):
    def __init__(self, nip, username, password, jabatan="Staff"):
        super().__init__(
            id_admin=nip,
            username=username,
            password=password,
            jabatan=jabatan
        )
        self.nip = nip