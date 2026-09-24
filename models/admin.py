class Admin:
    def __init__(self, id_admin, username, password, jabatan):
        self.id_admin = id_admin
        self.username = username
        self.password = password
        self.jabatan = jabatan

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False