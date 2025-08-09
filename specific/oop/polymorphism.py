"""DUCK TYPING"""
# fungsi nya untuk mengurangi ketergantungan antara class tertentu
# asalkan class tersebut memiliki method dan atribut yang sama

class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(duck):
   print(duck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)   
makeSound(anotherBird) 

"""ABSTRACT METHOD"""
# digunakan saat ingin membuat blueprint yang kelas turunanan nya 
# harus mengimplementasikan method tersebut

from abc import ABC, abstractmethod

class shape(ABC):
   @abstractmethod
   def draw(self):
      "Abstract method"
      return

class circle(shape):
   def draw(self):
      super().draw()
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      super().draw()
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()
   
   
"""REFLECTION"""
# digunakan untuk mengecek tipe data / objek

def tambah(a, b):
    # untuk mengecek tipe data apakah sesuai
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Harus angka")
    return a + b


class Hewan: pass
class Kucing(Hewan): pass
class Persia(Kucing): pass
# untuk mengecek apakah class adalah turunan dari class lain
print(issubclass(Kucing, Hewan))   # True
print(issubclass(Persia, Hewan))   # True (turunan tak langsung)
print(issubclass(Hewan, Hewan))    # True
print(issubclass(Hewan, Kucing))   # False

