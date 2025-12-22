class Body:
    def __init__(self, name, age):
        self.name = name
        self.age = age


data = {"name": "arief", "age": 20}

body = Body(**data)

print(body.__dict__)


from typing import Annotated, get_args

UserId = Annotated[int, "ID user", "harus positif", "blebleble"]

# Ambil type asli dan metadata
origin_type, *metadata = get_args(UserId)
print(origin_type)  # <class 'int'>
print(metadata)  # ('ID user', 'harus positif')
