import datetime
import random
import string

# Template data buku
buku_template = {
    "judul": "judul",
    "penulis": "penulis",
    "tahun_terbit": 1111,
    "tgl_terakhir_pinjaman": datetime.datetime(2010, 10, 10),
    "status": "TERSEDIA"
}

# Dictionary utama untuk menyimpan semua data buku
data_perpustakaan = {}

while True:
    print(f"{"Selamat Datang":^50}")
    print(f"{"Sistem Manajemen Perpustakaan":^50}")
    print("-" * 50)

    buku = dict.fromkeys(buku_template.keys())

    # Input data buku
    buku["judul"] = input("Judul Buku : ")
    buku["penulis"] = input("Penulis : ")
    buku["tahun_terbit"] = int(input("Tahun Terbit : "))

    print("\nMasukkan Tanggal Terakhir Pinjam:")
    tahun = int(input("Tahun (YYYY): "))
    bulan = int(input("Bulan (MM): "))
    tanggal = int(input("Tanggal (DD): "))
    buku["tgl_terakhir_pinjaman"] = datetime.datetime(tahun, bulan, tanggal)

    buku["status"] = input("Status (TERSEDIA/TIDAK): ").upper()

    # Membuat KEY unik dengan kombinasi huruf acak (multi-keys bisa dikembangkan)
    KEY = "".join(random.choice(string.ascii_uppercase) for i in range(6))

    # Menambahkan data buku ke dictionary utama (nesting dictionary)
    data_perpustakaan.update({KEY: buku})

    # Tampilkan semua data buku
    print("\n" + "-" * 80)
    print(f"{'KEYS':<8} {'JUDUL BUKU':<25} {'PENULIS':<20} {'THN':<5} {'TGL PINJAM':<15} {'STATUS':<10}")
    print("-" * 80)

    for key in data_perpustakaan:
        JUDUL = data_perpustakaan[key]["judul"]
        PENULIS = data_perpustakaan[key]["penulis"]
        THN = data_perpustakaan[key]["tahun_terbit"]
        TGL = data_perpustakaan[key]["tgl_terakhir_pinjaman"].strftime("%x")
        STATUS = data_perpustakaan[key]["status"]

        print(f"{key:<8} {JUDUL:<25} {PENULIS:<20} {THN:<5} {TGL:<15} {STATUS:<10}")

    print("\n")

    is_done = input("Tambah buku lagi? (y/n): ")
    if is_done.lower() == "n":
        break
