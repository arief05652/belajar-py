# from typing import Callable


# class DataUser:
#     user_dict: dict[str, Callable[..., ]] = {}

# class Biodata(DataUser):
    
#     def add_user(self, name: str, age: int) -> None:
#         self.user_dict[name] = age
    
#     def get_user(self, name: str) -> int | None:
#         return self.user_dict.get(name)
    
#     def all_users(self) -> dict[str, int]:
#         return self.user_dict


# ucup = Biodata()
# ucup.add_user("ucup", 20)
# ucup.add_user("otong", 25)

# print("Ucup:", ucup.get_user("ucup"))
# print("Semua data:", ucup.all_users())

# # Loop semua user
# for name, age in ucup.all_users().items():
#     print(f"{name} berumur {age}")


class Hero:
    def __init__(self, name):
        self.name = name
        
    def info_hero(self):
        print(f"Nama: {self.name}")

class Mage(Hero):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana
        
    def info_mage(self):
        super().info_hero()
        print(f"Mana: {self.mana}")

mage = Mage("ucup", 100)
mage.info_mage()


class UserHero:
    def __init__(self):
        self.hero = None     

    def create_hero(self, name: str):
        self.hero = Hero(name)
        print(f"Berhasil bikin user: {name}")
        self.hero.info_hero()

user = UserHero()
user.create_hero("Zilong")