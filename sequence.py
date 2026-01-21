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
print(sort)  # [41, 32, 23, 15]


from typing import Iterable, Sequence

"""
Iterable: dipake kalo butuh data list dan ingin dipakai untuk iterasi
Sequence: dipakai saat butuh data list tetapi yang dibutuhkan indeks dari datanya
"""


def iterable(x: Iterable[int]) -> None:
    for i in x:
        print("iterasi: ", i)


def sequence(x: Sequence[int]) -> None:
    print("indeks: ", x[2])


iterable([1, 2, 4])
sequence([1, 2, 4])
