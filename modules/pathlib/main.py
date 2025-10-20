from pathlib import Path

# ======================
# 🔹 Path dasar
# ======================
path = Path("modules/../built_in/main.py")

print("=== PATH INFO ===")
print("Path: ", path)                          # path mentah (belum dibersihkan)
print("Path Resolve: ", path.resolve())        # path absolut & bersih
print("Current Path: ", path.cwd())            # direktori kerja saat ini
print("Home Path: ", path.home())              # path home user

# ======================
# 🔹 Navigasi antar path
# ======================
print("\n=== NAVIGASI PATH ===")
print("Parent Path: ", path.parent.resolve())  # folder induk
print("Parent Name: ", path.parent.name)       # nama folder induk
print("Path Stem: ", path.stem)                # nama file tanpa ekstensi
print("Path Suffix: ", path.suffix)            # ekstensi file (contoh: .py)
print("Path Suffixes: ", path.suffixes)        # jika multi ekstensi (contoh: .tar.gz)

# ======================
# 🔹 Folder manipulation
# ======================
print("\n=== FOLDER MANIPULATION ===")

# Buat folder baru
folder = Path("output/logs")
folder.mkdir(parents=True, exist_ok=True)  # parents=True agar folder di atasnya ikut dibuat

print("Folder dibuat:", folder.resolve())

# Cek apakah folder ada
print("Folder exists:", folder.exists())
print("Apakah folder?:", folder.is_dir())

# ======================
# 🔹 File manipulation
# ======================
print("\n=== FILE MANIPULATION ===")

# Buat file baru di dalam folder
file = folder / "example.txt"
file.touch(exist_ok=True)  # buat file kosong (jika belum ada)
print("File dibuat:", file.resolve())

# Tulis isi file
file.write_text("Halo dari pathlib!\nBaris kedua juga ada nih.")
print("Isi file berhasil ditulis.")

# Baca isi file
content = file.read_text()
print("Isi file:\n", content)

# Rename file
new_file = file.with_name("renamed_example.txt")
file.rename(new_file)
print("File diubah nama jadi:", new_file.name)

# Ubah ekstensi
bak_file = new_file.with_suffix(".bak")
new_file.rename(bak_file)
print("File diubah ekstensi jadi:", bak_file.name)

# ======================
# 🔹 Iterasi isi folder
# ======================
print("\n=== ITERASI ISI FOLDER ===")
for item in folder.iterdir():
    print(" -", item.name)

# ======================
# 🔹 Hapus file dan folder
# ======================
print("\n=== HAPUS FILE & FOLDER ===")
if bak_file.exists():
    bak_file.unlink()  # hapus file
    print("File dihapus:", bak_file.name)

# Hapus folder (jika kosong)
try:
    folder.rmdir()
    print("Folder dihapus:", folder)
except OSError:
    print("Folder tidak kosong, tidak bisa dihapus langsung.")
