Exception # error yang umum
ValueError # nilai argumen tidak sesuai dengan tipe data yang diharapkan
ZeroDivisionError # pembagian dengan angka nol
TypeError # tipe data tidak sesuai
IndexError # indeks diluar batas
KeyError # kunci tidak ditemukan
AttributeError # atribut tidak ditemukan
ImportError # gagal import modul
ModuleNotFoundError # modul tidak ditemukan
FileNotFoundError # file tidak ditemukan
PermissionError # akses file tidak diizinkan
OSError # error operasi sistem
RuntimeError # error runtime
NotImplementedError # method belum diimplementasikan
OverflowError # angka terlalu besar
MemoryError # memori tidak cukup
StopIteration # iterasi sudah selesai
StopAsyncIteration # iterasi async sudah selesai
NameError # variabel tidak ditemukan
UnboundLocalError # variabel lokal tidak ditemukan
IndentationError # indentasi tidak sesuai
SyntaxError # syntax tidak sesuai
EOFError # akhir file tidak ditemukan
AssertionError # assert tidak terpenuhi
KeyboardInterrupt # pengguna membatalkan eksekusi

try:
    # kode yang mungkin bisa error
    ...
except:
    # exception penyebab code error
    ...
else:
    # jika kode tidak error jalankan ini
    ...
finally:
    # selalu dijalankan jika ada error atau tidak
    # biasanya dipakai untuk close db atau file
    ...