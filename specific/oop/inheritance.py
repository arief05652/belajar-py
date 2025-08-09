from object import Hewan

class Kucing(Hewan): # extends class
    def __init__(self, name: str, umur: int, jenis: str):
        super().__init__(name, jenis) # isi init parent class 
        self.umur = umur
        
    # override dari class parent
    @property
    def namaHewan(self):
        return f"Nama: {self.name}\nUmur: {self.umur} tahun\nJenis: {self._jenis}" # akses property dari parent class
    


kucing = Kucing("Kucing", 2, jenis="Mamalia")
print(kucing.namaHewan)