from models.alat import Alat
from models.mahasiswa import Mahasiswa
from models.staff import Staff


class MenuCLI:
    def __init__(self, sistem):
        self.sistem = sistem

    def tampilkan_login(self):
        while True:
            print("\n=== SISTEM PEMINJAMAN LABORATORIUM KOMPUTER ===")
            print("1. Login Admin")
            print("2. Login Mahasiswa")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                username = input("Username: ")
                password = input("Password: ")
                if self.sistem.login_admin(username, password):
                    print(
                        f"\n[+] Login berhasil! Selamat datang Admin {self.sistem.user_aktif.username}."
                    )
                    self.tampilkan_menu_admin()
                else:
                    print("[-] Login gagal! Username atau password salah.")

            elif pilihan == "2":
                nim = input("NIM: ")
                nama = input("Nama: ")
                if self.sistem.login_mahasiswa(nim, nama):
                    print(
                        f"\n[+] Login berhasil! Selamat datang {self.sistem.user_aktif.nama}."
                    )
                    self.tampilkan_menu_mahasiswa()
                else:
                    print(
                        "[-] Login gagal! NIM atau Nama tidak terdaftar (Hubungi Admin)."
                    )

            elif pilihan == "0":
                print("Terima kasih telah menggunakan sistem ini.")
                break
            else:
                print("[-] Pilihan tidak valid.")

    def tampilkan_menu_admin(self):
        while self.sistem.user_aktif:
            print("\n--- MENU UTAMA ADMIN ---")
            print("1. Kelola Data Admin/Staff (Tambah/Edit/Hapus)")
            print("2. Kelola Data Mahasiswa (Tambah/Edit/Hapus)")
            print("3. Kelola Data Alat/Aset (Tambah/Edit/Hapus)")
            print("4. Lihat Semua Transaksi")
            print("5. Proses Pengembalian Alat")
            print("0. Logout")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                self.sub_menu_kelola_admin()
            elif pilihan == "2":
                self.sub_menu_kelola_mahasiswa()
            elif pilihan == "3":
                self.sub_menu_kelola_alat()
            elif pilihan == "4":
                self.tampilkan_semua_transaksi()
            elif pilihan == "5":
                self.proses_pengembalian_ui()
            elif pilihan == "0":
                self.sistem.logout()
                print("[+] Logout berhasil.")
            else:
                print("[-] Pilihan tidak valid.")

    def sub_menu_kelola_admin(self):
        while True:
            print("\n-- KELOLA ADMIN/STAFF --")
            print("1. Tambah Admin Baru")
            print("2. Lihat Semua Admin")
            print("3. Edit Password Admin")
            print("4. Hapus Admin")
            print("0. Kembali")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                username = input("Masukkan Username baru: ")
                if self.sistem.manajemen_admin.cari(username):
                    print("[-] Gagal! Username sudah terdaftar.")
                else:
                    nip = input("Masukkan NIP: ")
                    password = input("Masukkan Password: ")
                    self.sistem.manajemen_admin.tambah(
                        Staff(nip=nip, username=username, password=password)
                    )
                    print(f"[+] Admin {username} berhasil didaftarkan!")

            elif pilihan == "2":
                self.tampilkan_semua_admin()

            elif pilihan == "3":
                if self.tampilkan_semua_admin():
                    username = input("\nMasukkan Username admin yang ingin diedit: ")
                    if self.sistem.manajemen_admin.cari(username):
                        password_baru = input("Masukkan Password baru: ")
                        if self.sistem.manajemen_admin.edit(username, password_baru):
                            print("[+] Password berhasil diubah!")
                    else:
                        print("[-] Admin tidak ditemukan.")

            elif pilihan == "4":
                if self.tampilkan_semua_admin():
                    username = input("\nMasukkan Username admin yang ingin dihapus: ")
                    if username == self.sistem.user_aktif.username:
                        print(
                            "[-] Gagal! Anda tidak bisa menghapus akun Anda sendiri saat sedang login."
                        )
                    else:
                        if self.sistem.manajemen_admin.hapus(username):
                            print("[+] Akun admin berhasil dihapus!")
                        else:
                            print("[-] Admin tidak ditemukan.")
            elif pilihan == "0":
                break
            else:
                print("[-] Pilihan tidak valid.")

    def sub_menu_kelola_mahasiswa(self):
        while True:
            print("\n-- KELOLA MAHASISWA --")
            print("1. Tambah Mahasiswa Baru")
            print("2. Lihat Semua Mahasiswa")
            print("3. Edit Data Mahasiswa")
            print("4. Hapus Mahasiswa")
            print("0. Kembali")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                nim = input("Masukkan NIM: ")
                if self.sistem.manajemen_mahasiswa.cari(nim):
                    print("[-] Gagal! NIM sudah terdaftar.")
                else:
                    nama = input("Masukkan Nama: ")
                    self.sistem.manajemen_mahasiswa.tambah(Mahasiswa(nim, nama))
                    print(f"[+] Mahasiswa {nama} berhasil didaftarkan!")

            elif pilihan == "2":
                self.tampilkan_semua_mahasiswa()

            elif pilihan == "3":
                if self.tampilkan_semua_mahasiswa():
                    nim = input("\nMasukkan NIM mahasiswa yang ingin diedit: ")
                    nama_baru = input("Masukkan Nama baru: ")
                    if self.sistem.manajemen_mahasiswa.edit(nim, nama_baru):
                        print("[+] Data berhasil diubah!")
                    else:
                        print("[-] Mahasiswa tidak ditemukan.")

            elif pilihan == "4":
                if self.tampilkan_semua_mahasiswa():
                    nim = input("\nMasukkan NIM mahasiswa yang ingin dihapus: ")
                    hasil = self.sistem.manajemen_mahasiswa.hapus(nim)
                    if hasil == "GAGAL_MASIH_MEMINJAM":
                        print(
                            "[-] Gagal! Mahasiswa masih memiliki transaksi peminjaman aktif."
                        )
                    elif hasil:
                        print("[+] Data mahasiswa berhasil dihapus!")
                    else:
                        print("[-] Mahasiswa tidak ditemukan.")
            elif pilihan == "0":
                break
            else:
                print("[-] Pilihan tidak valid.")

    def sub_menu_kelola_alat(self):
        while True:
            print("\n-- KELOLA ALAT/ASET LAB --")
            print("1. Tambah Alat Baru")
            print("2. Lihat Semua Alat")
            print("3. Edit Alat (Nama/Kondisi/Status)")
            print("4. Hapus Alat")
            print("0. Kembali")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                kode = input("Masukkan Kode Alat (Misal: PC-05): ")
                if self.sistem.manajemen_alat.cari(kode):
                    print("[-] Gagal! Kode alat sudah ada.")
                else:
                    nama = input("Masukkan Nama Alat: ")
                    print(f"Kategori: {self.sistem.manajemen_alat.daftar_kategori}")
                    kategori = input("Masukkan Kategori: ")
                    self.sistem.manajemen_alat.tambah(Alat(kode, nama, kategori))
                    print("[+] Alat baru berhasil ditambahkan!")

            elif pilihan == "2":
                self.tampilkan_semua_alat()

            elif pilihan == "3":
                self.tampilkan_semua_alat()
                kode = input("\nMasukkan kode alat yang ingin diedit: ")
                alat = self.sistem.manajemen_alat.cari(kode)
                if alat:
                    nama_baru = input(
                        f"Nama baru (Enter jika skip, saat ini: {alat.nama}): "
                    )
                    print(f"Pilihan Kondisi: {Alat.PILIHAN_KONDISI}")
                    kondisi_baru = input("Kondisi baru (Enter jika skip): ")
                    status_baru = input(
                        "Status baru (Tersedia/Tidak Tersedia/Dipinjam, Enter jika skip): "
                    )

                    self.sistem.manajemen_alat.edit(
                        kode,
                        nama=nama_baru if nama_baru else None,
                        kondisi=kondisi_baru if kondisi_baru else None,
                        status=status_baru if status_baru else None,
                    )
                    print("[+] Data alat berhasil diperbarui!")
                else:
                    print("[-] Alat tidak ditemukan.")

            elif pilihan == "4":
                self.tampilkan_semua_alat()
                kode = input("\nMasukkan kode alat yang ingin dihapus: ")
                alat = self.sistem.manajemen_alat.cari(kode)
                if alat and alat.status == "Dipinjam":
                    print("[-] Gagal! Alat sedang dipinjam.")
                elif self.sistem.manajemen_alat.hapus(kode):
                    print("[+] Alat berhasil dihapus!")
                else:
                    print("[-] Alat tidak ditemukan.")
            elif pilihan == "0":
                break
            else:
                print("[-] Pilihan tidak valid.")

    def tampilkan_semua_admin(self):
        data_admin = self.sistem.manajemen_admin.data
        if not data_admin:
            print("[-] Belum ada data admin/staff.")
            return False

        print("\n=== DAFTAR ADMIN & STAFF ===")
        print("-" * 65)
        print(f"| {'ID / NIP / NIM':<18} | {'Username':<15} | {'Jabatan':<20} |")
        print("-" * 65)

        for admin in data_admin.values():
            print(
                f"| {admin.id_admin:<18} | {admin.username:<15} | {admin.jabatan:<20} |"
            )

        print("-" * 65)
        return True

    def tampilkan_semua_mahasiswa(self):
        data_mhs = self.sistem.manajemen_mahasiswa.data
        if not data_mhs:
            print("[-] Belum ada data mahasiswa.")
            return False

        print("\n=== DAFTAR MAHASISWA ===")
        print("-" * 56)
        print(f"| {'NIM':<10} | {'Nama Mahasiswa':<20} | {'Status':<15} |")
        print("-" * 56)

        for mhs in data_mhs.values():
            status = "Sedang Meminjam" if mhs.status_peminjaman else "Tidak Meminjam"
            print(f"| {mhs.nim:<10} | {mhs.nama:<20} | {status:<15} |")

        print("-" * 56)
        return True

    def tampilkan_semua_transaksi(self):
        data_trx = self.sistem.manajemen_transaksi.data
        if not data_trx:
            print("[-] Belum ada data transaksi.")
            return

        print("\n=== DAFTAR SEMUA TRANSAKSI ===")
        print("-" * 135)
        print(
            f"| {'ID Transaksi':<12} | {'Nama Peminjam':<14} | {'Tanggal Pinjam':<19} | {'Batas Kembali':<19} | {'Alat (Kode)':<28} | {'Status TRX':<15} | {'Status Item':<12} |"
        )
        print("-" * 135)

        for id_trx, trx in data_trx.items():
            first_item = True
            for item in trx.items:
                nama_alat = item.alat.nama
                if len(nama_alat) > 17:
                    nama_alat = nama_alat[:14] + "..."
                alat_info = f"{nama_alat} ({item.alat.kode})"

                status_trx = trx.status.title()
                if len(status_trx) > 15:
                    status_trx = status_trx[:12] + "..."

                status_item = item.status.title()

                if first_item:
                    nama_peminjam = trx.mahasiswa.nama
                    if len(nama_peminjam) > 14:
                        nama_peminjam = nama_peminjam[:11] + "..."

                    print(
                        f"| {id_trx:<12} | {nama_peminjam:<14} | {trx.tanggal_pinjam:<19} | {trx.batas_kembali:<19} | {alat_info:<28} | {status_trx:<15} | {status_item:<12} |"
                    )
                    first_item = False
                else:
                    print(
                        f"| {'':<12} | {'':<14} | {'':<19} | {'':<19} | {alat_info:<28} | {'':<15} | {status_item:<12} |"
                    )

        print("-" * 135)

    def proses_pengembalian_ui(self):
        self.tampilkan_semua_transaksi()
        id_trx = input("\nMasukkan ID Transaksi yang ingin dikembalikan: ")
        trx = self.sistem.manajemen_transaksi.data.get(id_trx)

        if trx and trx.is_aktif():
            kondisi_dict = {}
            print("\n-- Pengecekan Kondisi Alat --")
            for item in trx.items:
                print(f"\nAlat: {item.alat.nama} ({item.alat.kode})")
                print(f"Pilihan Kondisi: {Alat.PILIHAN_KONDISI}")
                kondisi_kembali = input(f"Kondisi saat kembali (default Baik): ")
                kondisi_dict[item.alat.kode] = (
                    kondisi_kembali if kondisi_kembali else "Baik"
                )

            self.sistem.manajemen_transaksi.proses_pengembalian(id_trx, kondisi_dict)
            print(
                "[+] Pengembalian berhasil diproses. Status alat dan mahasiswa telah diperbarui."
            )
        else:
            print("[-] Transaksi tidak ditemukan atau sudah Selesai/Dikembalikan.")

    def tampilkan_menu_mahasiswa(self):
        while self.sistem.user_aktif:
            print("\n--- MENU MAHASISWA ---")
            print("1. Lihat Daftar Alat (Read-Only)")
            print("2. Pinjam Alat")
            print("3. Lihat Status Peminjaman Saya")
            print("0. Logout")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                self.tampilkan_semua_alat()

            elif pilihan == "2":
                if self.sistem.user_aktif.status_peminjaman:
                    print(
                        "[-] Kamu masih memiliki peminjaman aktif. Kembalikan alat sebelumnya dulu!"
                    )
                    continue

                self.tampilkan_semua_alat()
                kode_input = input(
                    "\nMasukkan kode alat yang ingin dipinjam (pisahkan koma jika lebih dari 1, misal: PC-01,KBL-01): "
                )
                kode_list = [k.strip() for k in kode_input.split(",")]

                alat_dipinjam = []
                for kode in kode_list:
                    alat = self.sistem.manajemen_alat.cari(kode)
                    if alat and alat.bisa_dipinjam():
                        alat_dipinjam.append(alat)
                    else:
                        print(
                            f"[-] Alat {kode} tidak valid, sedang dipinjam, atau rusak."
                        )

                if alat_dipinjam:
                    trx = self.sistem.manajemen_transaksi.buat_transaksi(
                        self.sistem.user_aktif, alat_dipinjam
                    )
                    if trx:
                        print(
                            f"[+] Berhasil meminjam! ID Transaksi: {trx.id_transaksi}"
                        )
                else:
                    print(
                        "[-] Peminjaman dibatalkan, tidak ada alat valid yang dipilih."
                    )

            elif pilihan == "3":
                trx_list = self.sistem.manajemen_transaksi.cari_berdasarkan_mahasiswa(
                    self.sistem.user_aktif.nim
                )
                if not trx_list:
                    print("[-] Kamu tidak memiliki peminjaman aktif.")
                else:
                    print("\n=== STATUS PEMINJAMAN SAYA ===")
                    print("-" * 112)
                    print(
                        f"| {'ID Transaksi':<12} | {'Tanggal Pinjam':<19} | {'Batas Kembali':<19} | {'Alat (Kode)':<32} | {'Status Item':<13} |"
                    )
                    print("-" * 112)

                    for trx in trx_list:
                        first_item = True
                        for item in trx.items:
                            nama_alat = item.alat.nama
                            if len(nama_alat) > 18:
                                nama_alat = nama_alat[:15] + "..."
                            alat_info = f"{nama_alat} ({item.alat.kode})"
                            status_item = item.status.title()

                            if first_item:
                                print(
                                    f"| {trx.id_transaksi:<12} | {trx.tanggal_pinjam:<19} | {trx.batas_kembali:<19} | {alat_info:<32} | {status_item:<13} |"
                                )
                                first_item = False
                            else:
                                print(
                                    f"| {'':<12} | {'':<19} | {'':<19} | {alat_info:<32} | {status_item:<13} |"
                                )
                    print("-" * 112)

            elif pilihan == "0":
                self.sistem.logout()
                print("[+] Logout berhasil.")
            else:
                print("[-] Pilihan tidak valid.")

    def tampilkan_semua_alat(self):
        data_alat = self.sistem.manajemen_alat.data
        if not data_alat:
            print("[-] Belum ada data alat.")
            return
        print("\n=== DAFTAR ASET LAB KOMPUTER ===")
        print("-" * 102)
        print(
            f"| {'Kode':<8} | {'Nama Alat':<30} | {'Kategori':<18} | {'Status':<15} | {'Kondisi':<15} |"
        )
        print("-" * 102)

        for alat in data_alat.values():
            print(
                f"| {alat.kode:<8} | {alat.nama:<30} | {alat.kategori:<18} | {alat.status:<15} | {alat.kondisi:<15} |"
            )

        print("-" * 102)
