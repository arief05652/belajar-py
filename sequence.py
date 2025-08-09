list = ["b", "c", "d", "a"]

# print(*list) # unpack data di list "**var" untuk kwargs
# print(*[data.upper() for data in list])


"""
- .sort() : mengubah list sendiri (digunakan saat runtime)
- sorted() : mengembalikan list baru (digunakan di instance baru)
"""
def ambil_angka_terakhir(x):
    return x % 10

data = [23, 41, 15, 32]
sort = sorted(data, key=ambil_angka_terakhir)
# 23 → 3
# 41 → 1
# 15 → 5
# 32 → 2
data.sort(key=ambil_angka_terakhir)
print(data)
print(sort) # [41, 32, 23, 15]