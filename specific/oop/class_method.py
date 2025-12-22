class Karyawan:
    count = 0
    
    def __init__(self, name: str):
        self.name = name
        
        Karyawan.count += 1

    @classmethod
    def addCount(cls, name: str):
        """
        bisa dipanggil langsung dari class
        """
        return cls(name)
    
    @property
    def getEmployeCount(self):
        """
        harus dipakai dari instance gabisa langsung dari class
        """
        print (f"Total Employe: {self.count}")
    
    @staticmethod
    def getEmploye():
        """
        bisa dipanggil langsung dari class
        """
        print(f"Total Employe: {Karyawan.count}")


a = Karyawan("Andi")
b = Karyawan.addCount("Asep")
b.getEmployeCount # property
Karyawan.addCount("Budi") # classmethod
Karyawan.getEmploye() # staticmethod

print("="*10)

print(hasattr(a, 'name')) # untuk mengecek apakah ada attribute
print(getattr(a, 'name')) # untuk mengambil attribute
setattr(a, 'name', 'Ucup') # untuk mengubah attribute
print(getattr(a, 'name'))

delattr(a, 'name') # untuk menghapus attribute
print(getattr(a, 'name'))
