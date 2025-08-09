# contoh class versi biasa
class Kendaraan:
    
    # constructor
    def __init__(self, nameKendaraan: str, tahunKendaraan: str, warnaKendaraan: str):
        self.name = nameKendaraan # public 
        self._warna = warnaKendaraan # protect
        self.__tahun = tahunKendaraan # private
    
    # getter dengan fungsi
    def getkendaraan(self):
        return f"name: {self.name}\nwarna: {self._warna}\ntahun: {self.__tahun}"
    
    # setter dengan fungsi
    def setKendaraan(self, tahun: int):
        if tahun > 2000:
            self.__tahun = tahun
    
kendaraan = Kendaraan("Avanza", 2000, "Hitam")
kendaraan.setKendaraan(2005)
print(kendaraan.getkendaraan())
    

# contoh class versi pythonic
class Hewan:
    # constructor
    def __init__(self, name: str, jenis: str):
        self.name = name
        self._jenis = jenis
    
    # getter tapi diubah jadi property
    @property
    def namaHewan(self):
        return f"Hewan: {self.name}"
    
    # setter
    @namaHewan.setter
    def namaHewan(self, name: str):
        self.name = name
        
hewan = Hewan("Kucing")
hewan.namaHewan = "Ikan"
print(hewan.namaHewan)