""" ARITMATIK OPERATOR
- '+' : tambah
- '-' : kurang
- '*' : kali
- '/' : bagi
- '%' : sisa bagi
- '**' : pangkat
- '//' : total bagi
"""
# CONTOH
a = 10 + 10
b = 10 - 10
c = 10 * 10
d = 10 / 10
e = 10 % 10
f = 10 ** 10
g = 10 // 10

""" PERSAMAAN OPERATOR
- '==' : sama dengan
- '!=' : tidak sama dengan
- '>=' : lebih besar / sama dengan
- '<=' : lebih kecil / sama dengan
- '>' : lebih besar dari
- '<' : lebih kecil dari
"""
# CONTOH
num1, num2 = 10, 5

h = num1 == num2
i = num1 != num2
j = num1 >= num2
k = num1 <= num2
l = num1 > num2
m = num1 < num2

""" LOGICAL OPERATOR
- and : true and true = true | false and true = false 
- or : true or false = true | false or false = false
- not : not false = true | not true = false
"""
var = 10
# print(var >= 10 and var == 4)
# print(var < 100 or var == 10)
# print(not(var == 5)) # kebalikan

""" MEMBERSHIP OPERATOR
- in : cek isi sequence
- not in : cek isi di sequence tetapi ga ada
"""
data: list[any] = ['arief', 'minardi', 20]
# print("arief" in data) # True
# print("arief" not in data) # False

""" IDENTITY OPERATOR
- is : compare memory object
- is not : reserve compare memory object
"""
# CONTOH
a = "1"
b = a
print(f"a: {id(a)} | b: {id(b)}")
print(a is not b)