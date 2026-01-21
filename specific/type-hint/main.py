import random
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import (
    Annotated,
    Any,
    ClassVar,
    Dict,
    Final,
    Generic,
    List,
    Literal,
    NamedTuple,
    NewType,
    Optional,
    Protocol,
    Self,
    Set,
    Tuple,
    TypeAlias,
    TypedDict,
    TypeVar,
    Union,
)

# Data types
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# Collections
dict: Dict = {"string": "any"}
list: List = []
tuple: Tuple = ()
set: Set = {"any"}

#######################

union = Union[str, int, float, bool, bytes]
optional = Optional[str]

# untuk membuat conts yang gabisa di override
PI: Final = 3.14

# Type alias: supaya readable dan agar reusable
# ilustrasi: Budi dipanggil “Mas Budi”, tapi orangnya sama aja.
UserData: TypeAlias = Dict[str, str | int]

# NewType:
# ada KTP khusus yang bedain “Budi karyawan” vs “Budi pelanggan”,
# walau orangnya sama-sama Budi.
UserIdArief = NewType("UserIdArief", int)
UserIdBudi = NewType("UserIdBudi", int)

# Type generic
# digunakan saat argumen dan output harus sama
S = TypeVar("S")

# Limitasi value agar IDE kasih hint
limit_value = Literal["Senin", "Selasa"]


# Class variable
class Data:
    x: ClassVar[int] = 0


# Type generic: input dan output harus 1 tipe data
#               karna generic akan isolasi tipe nya
#               agar bisa pakai built-in method dari tipe tersebut
def register[T](name: List[T]) -> T:
    return random.choice(name)


def login(user_data: UserData, day: limit_value) -> str:
    for key, value in user_data.items():
        return f"Key: {key} | Value: {value} | Day: {day}"


data_regist = register(["Budi", "Jaka", "Adi"])
print(data_regist.upper())

data_login = login({"name": "Arief Minardi", "umur": 20}, "Selasa")
print(data_login)

#######################


# TypeDict: untuk validasi dictionary
class DataMahasiswa(TypedDict):
    nim: int
    name: str
    email: str


# dataclass: untuk mempersingkat class konvesional
@dataclass
class Jurusan:
    name: str


# NamedTuple: konsep nya mirip kaya @dataclass
class Point(NamedTuple):
    x: int
    y: int


p = Point(10, 20)
print(p)


# Annotated: untuk memberikan penjelasan parameter nya
def login_mahasiswa(
    mahasiswa: DataMahasiswa, user_id: Annotated[UserIdArief, "user id milik mahasiswa"]
):
    return mahasiswa, user_id


arief = UserIdArief(123)
budi = UserIdBudi(456)

print(
    login_mahasiswa(
        mahasiswa=DataMahasiswa(
            nim=23416255201040, name="Arief Minardi", email="arief@gmail.com"
        ),
        user_id=budi,  # akan error jika di check dari mypy, tetapi code tetap jalan
    )
)


# Chaining
print("Chaining method")


class Chainned:
    def __init__(self, text: str = ""):
        self.text = text

    def add_text(self, text: str) -> Self:
        self.text = text
        return self

    def upper_text(self) -> Self:
        self.text = self.text.upper()
        return self

    @property
    def get_text(self) -> str:
        return self.text


print(Chainned().add_text("Ucup Knalpot").upper_text().get_text)

# Generic class
# digunakan untuk handle class yang bisa custom tipe data
print("##############")

S = TypeVar("S")


class GenericClass(Generic[S]):
    def __init__(self):
        self._handlers: List[Callable[[str], str]] = []

    def subscribe(self, handler: Callable[[str], str]):
        self._handlers.append(handler)

    def emit(self, data: str):
        # results = []
        print("list handler: ", self._handlers)
        for h in self._handlers:
            print(h(data))  # <- jalanin fungsi yang diambil dari list
        #     results.append(result)
        # return results


generic = GenericClass[str]()  # <- inisiasi class tipe data

# masukin fungsi ke list
generic.subscribe(lambda a: f"subs({a})")

# masukin data
generic.emit("ucup")
# generic.emit("arip")


# Protocol = kontrak bentuk (bukan inheritance)
# Artinya: object dianggap SupportsClose
# kalau PUNYA method close() -> None
class SupportsClose(Protocol):
    def close(self) -> None: ...


# Class biasa, TIDAK inherit Protocol
# Tapi karena punya close(), dia cocok dengan SupportsClose
class Resource:
    def close(self) -> None:
        print("Resource.close()")


# Fungsi ini minta iterable object
# yang minimal punya method close()
def close_all(items: Iterable[SupportsClose]) -> None:
    for item in items:
        item.close()  # aman dipanggil


# Resource dianggap SupportsClose
close_all([Resource()])  # OK
