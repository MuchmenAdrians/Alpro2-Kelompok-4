import os

# ==========================================
# SIRUANG
# Sistem Informasi Peminjaman Ruang Kampus
# ==========================================

# =========================
# FUNGSI CLEAR TERMINAL
# =========================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def kembali_ke_menu():
    input("\nTekan Enter untuk kembali ke menu utama...")
    clear_screen()

# =========================
# DATA RUANG KAMPUS
# =========================
jadwal_ruang = {
    "Ruang 101": {},
    "Ruang 102": {},
    "Ruang 103": {},
    "LabKom A": {},
    "LabKom B": {},
    "Lab Jaringan": {},
    "Lab Multimedia": {},
    "Ruang Rapat": {},
    "Aula Seminar": {}
}

# =========================
# DAFTAR HARI
# =========================
hari_kampus = ["senin", "selasa", "rabu", "kamis", "jumat"]

# =========================
# JAM PERKULIAHAN
# =========================
jam_kuliah = {
    1: "07:30",
    2: "08:20",
    3: "09:10",
    4: "10:00",
    5: "10:50",
    6: "11:40",
    7: "13:00",
    8: "13:50",
    9: "14:40",
    10: "15:30",
    11: "16:20",
    12: "17:10"
}

# =========================
# FUNGSI CEK KETERSEDIAAN RUANG
# =========================
def cek_ruang(nama_ruang, hari, jam_mulai, jam_selesai):
    if nama_ruang not in jadwal_ruang:
        return False
    if hari not in jadwal_ruang[nama_ruang]:
        return True
    for jam in range(jam_mulai, jam_selesai + 1):
        if jam in jadwal_ruang[nama_ruang][hari]:
            return False
    return True

# =========================
# FUNGSI SIMPAN DATA PEMINJAMAN
# =========================
def simpan_peminjaman(nama_ruang, hari, jam_mulai, jam_selesai, nama_peminjam):
    if cek_ruang(nama_ruang, hari, jam_mulai, jam_selesai):
        if hari not in jadwal_ruang[nama_ruang]:
            jadwal_ruang[nama_ruang][hari] = {}
        for jam in range(jam_mulai, jam_selesai + 1):
            jadwal_ruang[nama_ruang][hari][jam] = nama_peminjam
        print("\nPeminjaman berhasil disimpan.")
    else:
        print("\nRuang sedang digunakan pada waktu tersebut.")
        

# =========================
# FITUR PINJAM RUANG
# =========================
def pinjam_ruang():
    print("===== PINJAM RUANG =====")

    # Tampilkan daftar ruang
    daftar_ruang = list(jadwal_ruang.keys())

    print("\nDaftar Ruang:")
    for i, ruang in enumerate(daftar_ruang, start=1):
        print(f"{i}. {ruang}")

    # =========================
    # INPUT PILIH RUANG
    # =========================
    while True:
        try:
            pilih_ruang = int(input("\nPilih nomor ruang: "))

            if 1 <= pilih_ruang <= len(daftar_ruang):
                nama_ruang = daftar_ruang[pilih_ruang - 1]
                break
            else:
                print("Pilihan ruang tidak tersedia.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT HARI
    # =========================
    print("\nDaftar Hari:")
    for i, hari in enumerate(hari_kampus, start=1):
        print(f"{i}. {hari.capitalize()}")

    while True:
        try:
            pilih_hari = int(input("\nPilih nomor hari: "))

            if 1 <= pilih_hari <= len(hari_kampus):
                hari = hari_kampus[pilih_hari - 1]
                break
            else:
                print("Pilihan hari tidak tersedia.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # TAMPILKAN JAM
    # =========================
    print("\nJam Perkuliahan:")
    for kode, jam in jam_kuliah.items():
        print(f"{kode}. {jam}")

    # =========================
    # INPUT JAM MULAI
    # =========================
    while True:
        try:
            jam_mulai = int(input("\nMasukkan jam mulai: "))

            if jam_mulai in jam_kuliah:
                break
            else:
                print("Jam mulai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT JAM SELESAI
    # =========================
    while True:
        try:
            jam_selesai = int(input("Masukkan jam selesai: "))

            if jam_selesai in jam_kuliah:
                if jam_selesai >= jam_mulai:
                    break
                else:
                    print("Jam selesai tidak boleh sebelum jam mulai.")
            else:
                print("Jam selesai tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # INPUT NAMA PEMINJAM
    # =========================
    while True:
        nama_peminjam = input("Masukkan nama peminjam: ").strip()

        if nama_peminjam != "":
            break
        else:
            print("Nama peminjam tidak boleh kosong.")

    # =========================
    # SIMPAN PEMINJAMAN
    # =========================
    simpan_peminjaman(
        nama_ruang,
        hari,
        jam_mulai,
        jam_selesai,
        nama_peminjam
    )