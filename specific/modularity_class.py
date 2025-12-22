# BASE CLASS
class Animal():
    speak: str = None
    
    def animal_speak(self, speak: str):
        self.speak = speak


# INHERITANCE
"""Pewarisan class"""
class Cat(Animal):
    def __init__(self, speak: str):
        self.speak = speak
    
    def cat_speak(self):
        print(self.speak)

kucing = Cat("Miaw")
kucing.cat_speak()


# COMPOSITION
"""Alternative dari inherit"""
class Tiger:
    def __init__(self):
        self.animal = Animal()

    def tiger_speak(self, suara: str):
        self.animal.animal_speak(suara)
        print(self.animal.speak)
        
tiger = Tiger()
tiger.tiger_speak("Roar...")


# AGGREGATION
"""Mirip tapi object nya dibikin di luar"""
class Logger:
    def log(self, msg):
        print(msg)

class Service:
    def __init__(self, logger: Logger):
        self.logger = logger

    def out_logger(self):
        self.logger.log("ini dari logger class")

log = Logger()
service = Service(log)
service.out_logger()


# MIXIN
"""Mirip inherit tapi cuman ngerjain fitur kecil"""
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class User(JSONMixin):
    def __init__(self, name):
        self.name = name

    def print_json(self):
        return self.to_json()

user_mixin = User("arief")
print(user_mixin.print_json())


# PROTOCOLS / DUCK TYPING
"""Seperti di alias jadi pake object dan method di parameter dalam fungsi"""
def run(obj):
    obj.start()

class Job:
    def start(self):
        print("job start")

run(Job()) 