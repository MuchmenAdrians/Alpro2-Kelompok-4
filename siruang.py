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
# FUNGSI KONVERSI JAM KE RANGE
# =========================
def jam_to_range(jam_mulai, jam_selesai):
    if jam_mulai in jam_kuliah and jam_selesai in jam_kuliah:
        return f"{jam_kuliah[jam_mulai]} - {jam_kuliah[jam_selesai]}"
    return f"Jam {jam_mulai} - {jam_selesai}"

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
def simpan_peminjaman(nama_ruang, hari, jam_mulai, jam_selesai, nama_peminjam, keperluan):
    if cek_ruang(nama_ruang, hari, jam_mulai, jam_selesai):
        if hari not in jadwal_ruang[nama_ruang]:
            jadwal_ruang[nama_ruang][hari] = {}
        for jam in range(jam_mulai, jam_selesai + 1):
            jadwal_ruang[nama_ruang][hari][jam] = {"nama": nama_peminjam, "keperluan": keperluan}
        print("\nPeminjaman berhasil disimpan.")
    else:
        print("\nRuang sedang digunakan pada waktu tersebut.")
        

# =========================
# FITUR PINJAM RUANG
# =========================
def pinjam_ruang():
    print("===== PINJAM RUANG =====")
    # Tampilkan daftar ruang dengan nomor
    daftar_ruang = list(jadwal_ruang.keys())
    print("\nDaftar Ruang:")
    for i, ruang in enumerate(daftar_ruang, start=1):
        print(f"{i}. {ruang}")

    # =========================
    # INPUT NAMA RUANG (DENGAN NOMOR)
    # =========================
    while True:
        try:
            pilih_ruang = int(input("\nPilih nomor ruang: "))           
            if 1 <= pilih_ruang <= len(daftar_ruang):
                nama_ruang = daftar_ruang[pilih_ruang - 1]
                break
            else:
                print(f"Nomor ruang tidak tersedia. Silakan pilih 1-{len(daftar_ruang)}.")
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
    # INPUT KEPERLUAN
    # =========================
    while True:
        keperluan = input("Masukkan keperluan (mata kuliah/acara): ").strip()
        if keperluan != "":
            break
        else:
            print("Keperluan tidak boleh kosong.")

    # =========================
    # SIMPAN PEMINJAMAN
    # =========================
    simpan_peminjaman(
        nama_ruang,
        hari,
        jam_mulai,
        jam_selesai,
        nama_peminjam,
        keperluan
    )

# =========================
# FUNGSI UNTUK MERINGKAS JADWAL
# =========================
def ringkas_jadwal(jadwal_per_hari):
    if not jadwal_per_hari:
        return []    
    ringkasan = []
    jam_list = sorted(jadwal_per_hari.keys())   
    i = 0
    while i < len(jam_list):
        start = jam_list[i]
        end = start
        
        # Cari jam yang berurutan dengan peminjam dan keperluan yang sama
        while i + 1 < len(jam_list) and jam_list[i + 1] == end + 1:
            current = jadwal_per_hari[jam_list[i]]
            next_jam = jadwal_per_hari[jam_list[i + 1]]
            
            # Cek apakah peminjam dan keperluan sama
            if (current["nama"] == next_jam["nama"] and 
                current["keperluan"] == next_jam["keperluan"]):
                end = jam_list[i + 1]
                i += 1
            else:
                break
        
        ringkasan.append({
            "jam_mulai": start,
            "jam_selesai": end,
            "nama": jadwal_per_hari[start]["nama"],
            "keperluan": jadwal_per_hari[start]["keperluan"]
        })
        i += 1    
    return ringkasan

# =========================
# FITUR LIHAT JADWAL
# =========================
def lihat_semua_jadwal():
    print("===== DAFTAR PEMINJAMAN =====")    
    ada_peminjaman = False
    for ruang, data in jadwal_ruang.items():
        if data:
            ada_peminjaman = True
            print(f"\nRuang: {ruang}")
            for hari, jam_data in data.items():
                ringkasan = ringkas_jadwal(jam_data)
                for item in ringkasan:
                    range_waktu = jam_to_range(item["jam_mulai"], item["jam_selesai"])
                    print(f"  - {hari.capitalize()} ({range_waktu}): {item['nama']} - {item['keperluan']}")
    
    if not ada_peminjaman:
        print("\nBelum ada peminjaman ruang.")

def lihat_jadwal_per_ruang():
    while True:
        clear_screen()
        print("===== CEK JADWAL PER RUANG =====")       
        # Tampilkan daftar ruang yang tersedia dengan nomor
        daftar_ruang = list(jadwal_ruang.keys())
        print("\nDaftar Ruang yang Tersedia:")
        for i, ruang in enumerate(daftar_ruang, start=1):
            print(f"{i}. {ruang}")

        print("\nKetik 'menu' untuk kembali ke utama")
        pilihan = input("\nPilih nomor ruang: ").strip()        
        if pilihan.lower() == "menu":
            break       
        if pilihan == "":
            print("\nPilihan tidak boleh kosong!")
            input("\nTekan Enter untuk mencoba lagi...")
            continue
        
        # Cek apakah input berupa angka
        try:
            index = int(pilihan)
            if 1 <= index <= len(daftar_ruang):
                nama_ruang = daftar_ruang[index - 1]
                data = jadwal_ruang[nama_ruang]
                if data:
                    print(f"\nJadwal {nama_ruang}:")
                    for hari, jam_data in data.items():
                        ringkasan = ringkas_jadwal(jam_data)
                        for item in ringkasan:
                            range_waktu = jam_to_range(item["jam_mulai"], item["jam_selesai"])
                            print(f"  - {hari.capitalize()} ({range_waktu}): {item['nama']} - {item['keperluan']}")
                else:
                    print(f"\n{nama_ruang} masih kosong, belum ada peminjaman!")
            else:
                print(f"\nNomor ruang tidak valid. Silakan pilih 1-{len(daftar_ruang)}.")
        except ValueError:
            print("\nInput harus berupa angka!")
        
        input("\nTekan Enter untuk cek ruang lain...")

# =========================
# FITUR HAPUS PEMINJAMAN
# =========================
def hapus_peminjaman():
    print("===== HAPUS PEMINJAMAN =====")
    # Tampilkan daftar ruang dengan nomor
    daftar_ruang = list(jadwal_ruang.keys())
    print("\nDaftar Ruang:")
    for i, ruang in enumerate(daftar_ruang, start=1):
        print(f"{i}. {ruang}")

    # =========================
    # INPUT NAMA RUANG (DENGAN NOMOR)
    # =========================
    while True:
        try:
            pilih_ruang = int(input("\nPilih nomor ruang: "))
            
            if 1 <= pilih_ruang <= len(daftar_ruang):
                nama_ruang = daftar_ruang[pilih_ruang - 1]
                break
            else:
                print(f"Nomor ruang tidak tersedia. Silakan pilih 1-{len(daftar_ruang)}.")
        except ValueError:
            print("Input harus berupa angka.")

    # =========================
    # TAMPILKAN DATA PEMINJAMAN
    # =========================
    data_ruang = jadwal_ruang[nama_ruang]
    if data_ruang:
        print(f"\nData peminjaman di {nama_ruang}:")
        for hari, jam_data in data_ruang.items():
            ringkasan = ringkas_jadwal(jam_data)
            for item in ringkasan:
                range_waktu = jam_to_range(item["jam_mulai"], item["jam_selesai"])
                print(f"- {hari.capitalize()} ({range_waktu}): {item['nama']} - {item['keperluan']}")
    else:
        print("\nBelum ada peminjaman pada ruang ini.")
        return

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
            jam_mulai = int(input("\nMasukkan jam mulai yang ingin dihapus: "))
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
            jam_selesai = int(input("Masukkan jam selesai yang ingin dihapus: "))
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
    # PROSES HAPUS
    # =========================
    data_ditemukan = False

    if hari in jadwal_ruang[nama_ruang]:
        for jam in range(jam_mulai, jam_selesai + 1):
            if jam in jadwal_ruang[nama_ruang][hari]:
                del jadwal_ruang[nama_ruang][hari][jam]
                data_ditemukan = True

        # Hapus hari jika kosong
        if not jadwal_ruang[nama_ruang][hari]:
            del jadwal_ruang[nama_ruang][hari]
    if data_ditemukan:
        print("\nPeminjaman berhasil dihapus.")
    else:
        print("\nData peminjaman tidak ditemukan.")

# =========================
# MENU UTAMA
# =========================
def menu_utama():
    while True:
        print("\n===== SISTEM INFORMASI PEMINJAMAN RUANG KAMPUS =====")
        print("1. Pinjam Ruang")
        print("2. Lihat Semua Jadwal")
        print("3. Lihat Jadwal Per Ruang")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        pilihan = input("\nPilih menu (1-5): ").strip()
        
        if pilihan == "1":
            clear_screen()
            pinjam_ruang()
            kembali_ke_menu()
        elif pilihan == "2":
            clear_screen()
            lihat_semua_jadwal()
            kembali_ke_menu()
        elif pilihan == "3":
            clear_screen()
            lihat_jadwal_per_ruang()
            clear_screen()
        elif pilihan == "4":
            clear_screen()
            hapus_peminjaman()
            kembali_ke_menu()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan SIRUANG!")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-5.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

# =========================
# MENJALANKAN PROGRAM
# =========================
clear_screen()
menu_utama() 