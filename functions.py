from typing import Callable


# fungsi biasa (bisa pake keyword arg bisa juga kaga)
def fungsi1(arg):
    pass


# fungsi default arg (jadi jika gapake arg pun bisa)
def fungsi2(arg="hello"):
    pass


# fungsi dengan positional arg or named arg
# ("/," bisa posisi atau named arg)
def fungsi3(arg1, arg2, /, arg3):
    print(arg1)
    print(arg2)
    print(arg3)


fungsi3(12, 12, arg3="sam")


# keyword only arg
def fungsi4(arg1, /, arg2, *, arg3):
    pass


fungsi4(1, 2, arg3="sakd")


# nested fungsi dengan nonlocal keyword
def nested():
    a = 10
    print("id glocal nested: {}".format(id(a)))

    def func():
        # untuk memisahkan
        nonlocal a
        a = 20
        print("id local nested: {}".format(id(a)))

    return func()


nested()


# callback
def to_lower(text: str, callback: Callable[[str], str]) -> str:
    return callback(text.lower())


# Definisikan callback dulu
def my_callback(hasil_lower):
    return f"Hasilnya: {hasil_lower}"


# Panggil dengan callback
print(to_lower("AKSD", lambda r: f"hasil: {r}"))
# Output: Hasilnya: aksd
