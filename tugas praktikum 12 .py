# Buatlah program dengan input dan fungsi untuk menghitung:
# a. Luas persegi panjang
# b. Volume balok
# c. Luas lingkaran
# d. Volume bola

# a. Luas persegi panjang
def luas_persegi_panjang():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("Panjang\t= "))
    l = int(input("Lebar\t= "))
    luas = p * l
    return luas
hasil_lpp = luas_persegi_panjang()
print("Luas persegi panjang =", hasil_lpp)

# b. Volume balok
def volume_balok():
    print("\nMenghitung Volume Balok")
    p = int(input("Panjang\t= "))
    l = int(input("Lebar\t= "))
    t = int(input("Tinggi\t= "))
    volume = p * l * t
    return volume
hasil_vb = volume_balok()
print("Volume balok =", hasil_vb)

# c. Luas lingkaran
def luas_lingkaran():
    print("\nMenghitung Luas Lingkaran")
    r = int(input("Jari-jari\t= "))
    phi = 3.14
    luas_o = phi * r * r
    return luas_o
hasil_ll = luas_lingkaran()
print("Luas lingkaran =", hasil_ll)

# d. Volume bola
def volume_bola():
    print("\nMenghitung Volume Bola")
    r = int(input("Jari-jari\t= "))
    phi = 3.14
    v_bola = (4/3) * phi * r ** 3
    return v_bola
hasil_vbola = volume_bola()
print("Volume bola =", hasil_vbola)
