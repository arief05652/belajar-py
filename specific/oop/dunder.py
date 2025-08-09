"""dunder method yang sering dipakai"""

class Aritmatik:
    yuhu = {} # class property
    
    def __init__(self, a, b, data: list[int] = None): 
        # inisiasi class
        self.a = a # object property
        self.b = b
        self.data = data
    
    """representasi objek"""
    def __str__(self): 
        # print object
        return f"Aritmatik({self.a}, {self.b}) | data: {self.data}"
    
    def __repr__(self):
        # print class dari object
        return "Aritmatik(a={}, b={})".format(self.a, self.b)
    
    """aritmatik operator"""
    def __add__(self, other):
        # pertambahan object
        return Aritmatik(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        # pengurangan object
        return Aritmatik(self.a - other.a, self.b - other.b)
        
    def __mul__(self, other):
        # perkalian object
        return Aritmatik(self.a * other.a, self.b * other.b)
        
    def __truediv__(self, other):
        # pembagian object
        return Aritmatik(self.a / other.a, self.b / other.b)
        
    """persamaan operator"""
    # "l" mean less
    # "g" mean greater
    def __lt__(self, other):
        # "<" less than
        return self.a < other.a and self.b < other.b
    
    def __le__(self, other):
        # "<=" less than or equal
        return self.a <= other.a and self.b <= other.b
        
    def __gt__(self, other):
        # ">" greater than
        return self.a > other.a and self.b > other.b
        
    def __ge__(self, other):
        # ">=" greater than or equal
        return self.a >= other.a and self.b >= other.b
    
    def __eq__(self, other):
        # "==" equal
        return self.a == other.a and self.b == other.b
        
    def __ne__(self, other):
        # "!=" not equal
        return self.a != other.a and self.b != other.b
        
    """sequence"""
    def __len__(self):
        # mengambil panjang elemen
        return len(self.data)
    
    def __getitem__(self, index):
        # mengambil elemen berdasarkan index
        return self.data[index]

    def __setitem__(self, index, value):
        # memasukan elemen berdasarkan index
        self.data[index] = value

    def __delitem__(self, index):
        # menghapus elemen berdasarkan index
        del self.data[index]

    def __contains__(self, item):
        #  mengecek apakah elemen tertentu ada atau tidak
        return item in self.data
    
a = Aritmatik(10, 5, [1, 2, 3, 4])
b = Aritmatik(7, 5)

print(a) # __str__
print(repr(a)) # __repr__

print("="*10)

print(a + b) # __add__
print(a - b) # __sub__
print(a * b) # __mul__
print(a / b) # __truediv__

print("="*10)

print(a < b) # __lt__
print(a <= b) # __le__
print(a > b) # __gt__
print(a >= b) # __ge__
print(a == b) # __eq__
print(a != b) # __ne__

print("="*10)

print(len(a)) # __len__
print(a[2]) # __getitem__
a[2] = 7 # __setitem__
print(a[2])

del a[1] # __delitem__
print(a)

print(7 in a) # __contains__