list_angka = [1, 2, 3, 4]
list_huruf = ["a", "b", "c", "d"]
positif, negatif, desimal =  3, -5, 7.3


print("""Numerik Functions""")


# untuk menghitung total angka di list
print("Total angka:", sum(list_angka))

# mencari angka terbesar
print("Angka terbesar:", max(list_angka))

# mencari angka terkecil
print("Angka terkecil:", min(list_angka))

# untuk menghitung jumlah angka
print("Jumlah angka:", len(list_angka))

# nilai absolut aka selalu positif
print("Nilai absolut:", abs(negatif))

# untuk membulatkan angka
print("Membulatkan angka:", round(desimal))

# pangkat
print("Pangkat:", pow(3, 2))


print("""Collection Functions""")


# untuk perulangan rentang angka
for i in range(1, 4):
    print("Range: ", i)

# loop dengan indeks
for i, v in enumerate(list_angka):
    print(f"Index: {i} | Value: {v}")

# zip untuk menggabungkan list
for a, b in zip(list_angka, list_huruf):
    print(f"Angka: {a} | Huruf: {b}")

# mengubah tipe data tapi dari dalem list
print("Mengubah tipe data:", list(map(str, list_angka)))

# untuk mem filter data dari list
print("Mengubah tipe data:", list(filter(lambda x: x > 2, list_angka)))

# mengurutkan list
print("Mengurutkan:", sorted(list_angka, reverse=True))


print("""Logika Functions""")


# any: kalau ada yg true maka true
print("Any:", any([True, False, False]))

# all: true kalau semua element true dan sebaliknya
print("All:", all([True, True, False]))

# isinstance: untuk mengecek tipe data
print("Isinstance:", isinstance(positif, int))

# issubclass: untuk mengecek class apakah turunan dari class lain
print("Issubclass:", issubclass(int, complex))


print("""Utilities Functions""")


print("ASCII -> Huruf: ", chr(65))
print("Huruf -> ASCII: ", ord("A"))

# ubah ke biner, heksadesimal, dan octal
print("Biner: ", bin(10))
print("Heksadesimal: ", hex(10))
print("Octal: ", oct(10))