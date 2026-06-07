import dataclasses
import weakref


def ref_callback(call):
    print(f"Objeck has removed: {call()}")


@dataclasses.dataclass(slots=True, weakref_slot=True)
class BioData:
    nama: str
    umur: int
    tinggi: float


bio = BioData("ucup", 15, 180)  # strong reference

weak_bio = weakref.ref(
    bio, ref_callback
)  # weak reference, dengan callback yang auto trigger ketika object di del
prox_weak_bio = weakref.proxy(
    bio
)  # jika ref nya di hapus mengembalikan 'ReferenceError'

print("ambil data dari weakref: ", weak_bio().umur)  # ambil data lewat weakref
print("weak count: ", weakref.getweakrefcount(bio))  # cek weakref total
print("cek weak name: ", weakref.getweakrefs(bio))  # get list nama weakref

del bio  # hapus reference & trigger callback jika ada
print("weak obj dihapus: ", weak_bio)

try:
    print("val proxy: ", prox_weak_bio.nama)
except ReferenceError as e:
    print("ref error: ", e)


print("# ==== WEAK COLLECTION ====")
"""
- WeakValueDictionary: weak value, key akan terhapus jika value nya dihapus
- WeakKeyDictionary: sebalik nya dari yang atas
- WeakSet: semua isi nya lemah dan bisa dihapus kapan aja
"""


@dataclasses.dataclass(slots=True, weakref_slot=True, frozen=True)
class Alamat:
    jalan: str
    bangunan: str

    def get_detail(self):
        return f"Jalan: {self.jalan} | Bangunan: {self.bangunan}"


# ===== WeakValueDictionary
a = Alamat("bogor", "rumah")
b = Alamat("jakarta", "kantor")

ref_dictval = weakref.WeakValueDictionary()

# menyimpan value lemah di key yang kuat
ref_dictval["data_a"] = a
ref_dictval["data_b"] = b

# transfer value lemah
key_baru = ref_dictval["data_b"]


print("list key: ", list(ref_dictval.keys()))
del b  # hapus referensi lemah
key, val = next(ref_dictval.items())  # ambil data dari generator weak dict
print(key, val)
# print(list(ref_dictval.items())[1])
# print(ref_dictval["data_a"])


# ===== WeakKeyDictionary
a = Alamat("zaenal", "rumah")

ref_key = weakref.WeakKeyDictionary()

ref_key[a] = {"name": "zaenal", "umur": 12}

print("weak key: ", ref_key[a])  # ambil data pakai key obj nya
del a
# print("weak key: ", ref_key[a]) # error karna dihapus


# ===== WeakSet
a = Alamat("burhan", "kantor")
b = Alamat("zaki", "kantor")

ref_set = weakref.WeakSet()

ref_set.add(a)
ref_set.add(b)

print(len(ref_set))  # cek panjang set
del a  # hapus object
for weak in list(ref_set):  # iterate pake list untuk thread safety
    print("iterate weak set: ", weak.get_detail())
