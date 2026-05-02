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
