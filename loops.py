"""
mutable: tipe data yang bisa diubah nilainya
immutable: tipe yang tidak bisa diubah atau
        kalau mau diubah harus buat objek baru
"""

"""for loop"""
for i in range(1, 5):
    print(i)

""" while loop """
i = 0
while i < 10:
    print(i)
    i += 1

data = [i for i in range(1, 5)]
print("List comprehension: ", data)

""" break, pass, continue """
def loop(data: list[str]):
    for i in data:
        if i == "r":
            pass  # lewati dan lanjut loop
        elif i == "i":
            continue  # lewati dan lanjut loop tapi huruf 'i' di lewat
        else:
            break  # stop iter
