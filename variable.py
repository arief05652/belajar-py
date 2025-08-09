""" TIPE DATA DASAR """
a: str = "String"
b: int = 12
c: float = 10.4
d: bool = True | False
e: complex = 1012j

""" TIPE DATA SEQUENCE """
f: list[str | int | float | bool | complex] = ["a", "b", "c"]
g: tuple = (1 ,"a", 10.2)
h: dict[str, int | str] = {"a", "b", "1", 2}
i: set = {"a", "b", "c", 12}

""" TIPE DATA BINARY  """
j: bytes = bytes([65, 66, 67, 68, 69])
k: bytes = b"hello"

l: bytearray = bytearray([72, 101, 108, 108, 111]) # ascii
m = memoryview(k) # showing memory addr in bytes var

""" TIPE DATA NONE """
n = None

print(type(n)) # <- for check data type

"""
type casting 
-----------
int(value)
str(value)
float(value)
"""