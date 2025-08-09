""" if, elif, else """
a: str = 15

# percabangan general
if a > 5:
    print("{} lebih dari 5".format(a))
elif a < 10:
    print("{} kurang dari 10".format(a))
else:
    print("{} tidak semuanya".format(a))
    
""" nested if """
if a > 10:
    print("a lebih dari 10")
    if a == 15:
        print("nested if a sama dengan 15")
else:
    print("a kurang dari 10")
    
""" percabangan dengan walrus """
# - cara kerja: variable langsung di tugaskan 
#   di operasi nya ngga di inisiasi dulu
if (b := 15) > 5:
    print("{} lebih dari 5".format(b))
    
""" match """
def checkDay(day, hola: list[str] = None):
    match day:
        case 'senin':
            return "Sekarang hari senin"
        case 'selasa':
            return "Sekarang hari selasa"
        case _: # default case dengan wildcard
            return "Gatau hari"
        
    match hola:
        case [time, name, umur] if umur < 17: # match parsing list dengan if 
            return f"Good {time} {name} {umur} age`s \nkamu belum cukup umur!" 
        case [time, name, umur]: # match parsing list
            return f"Good {time} {name} {umur} age`s !" 
        
print(checkDay('senin', ["Morning", "Arief", 17]))
