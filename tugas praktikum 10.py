# Nama    : Muhammad Banyu Legowo
# NIM     : 2505060071
# Rombel  : 04

# 1. Tuples
print ("No.1\n")

# a. Buat sebuah tuple bernama mahasiswa yang berisi data diri anda dengan 3 nilai: (“Nama”, “NIM”,”Prodi”) 
data_tuples = ("Muhammabd Banyu Legowo", "2505060071", "S1 Teknologi Informasi")
# c. Tampilkan data NIM dan Prodi 
print (f"NIM    = {data_tuples[1]}")
print (f"Prodi  = {data_tuples[2]}\n")

# 2. Dictionary
print ("No.2\n")

# a. Buat dictionary keranjang dengan data: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}
# b dan c Tambilan barang dan harga dan perulangan untuk menghitung total harga semua barang
total = 0
for buah, harga in keranjang.items():
  print (f"Harga {buah} : Rp {harga}")
  total += harga
# d. Tampilkan harga total belanja 
print ("=========================")  
print (f"Total harga : Rp {total}")
