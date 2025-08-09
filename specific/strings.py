""" slicing """
# slicing dimulai dari indeks 0 dan spasi pun masuk ke dalam indeks
# - variable[start:end:step]
# - start: dimulai dari indeks berapa
# - end: diakhiri di indeks berapa
# - step: loncat elemen
a: str = "hello, world" # len: 11
a = "abcdefghijklmn"

# akses dengan indeks
print(a[0]) # Output: a

# jika akses dengan negative dimulai 
# dari urutan belakang dan dari indeks ke: -1
# source: https://www.tutorialspoint.com/python/images/positive_negative_index.jpg
print(a[-2]) # Output: m

# contoh dengan step
print(a[::2]) # Output: acegikm

""" string style """
b = b"hello" # byte
# raw string akan mencetak seluruh escaping word
c = r"wor\nld"
print(c)
