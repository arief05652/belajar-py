class Vector:
    def __init__(self, a, b):  # Constructor: inisialisasi atribut saat objek dibuat
        self.a = a
        self.b = b

    def __str__(self):  # Magic method: mengatur representasi string saat objek di-print
        return "Vector ({}, {})".format(self.a, self.b)
    
    def __add__(self, other):  # Magic method: mendefinisikan perilaku operator +
        # cara kerja: self itu representasi dari v1 dan other v2
        return Vector(self.a + other.a, self.b + other.b)
    
    # def __del__(self): # destructor: delete object jarang digunakan lagi
    #     pass

    def __repr__(self): # representasi class 
        return "Vector(a={}, b={})".format(self.a, self.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)  # Output: Vector (7, 8)
print(repr(v1)) # contoh memakai "__repr__" method
