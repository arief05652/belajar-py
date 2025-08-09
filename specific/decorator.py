print("""BARE DECORATOR""")
def your_decorator(func):
    def wrapper():
        # Do stuff before func...
        print("Before func!")
        func()
        # Do stuff after func...
        print("After func!")
    return wrapper

@your_decorator
def foo():
    print("Hello World!")

foo()

print("""DECORATOR WITH ARGUMENTS""")
def your_decorator(func):
    def wrapper(*args,**kwargs):
        # Do stuff before func...
        print("Before func!") 
        func(*args,**kwargs)
        # Do stuff after func...
        print("After func!")
    return wrapper

@your_decorator
def foo(bar):
    print("My name is " + bar)

foo("Jack")


print("""DECORATOR WITH WRAPS""")
import functools

def decorator_with_wraps(func):
    @functools.wraps(func) # For preserving the metadata of func.
    def wrapper(*args,**kwargs):
        # Do stuff before func...
        result = func(*args,**kwargs)
        # Do stuff after func..
        return result
    return wrapper

@decorator_with_wraps
def foo(bar):
    print("My name is " + bar)

foo("Jack")


print("""DECORATOR WITH PARAMETER""")
def decorator_with_parameter(arg):
    def decorator(func):
        @functools.wraps(func) # For preserving the metadata of func.
        def wrapper(*args,**kwargs):
            # Do stuff before func possibly using arg...
            result = func(*args,**kwargs)
            # Do stuff after func possibly using arg...
            return result
        return wrapper
    return decorator

@decorator_with_parameter(arg="x")
def foo(bar):
    print("My name is " + bar)

foo("Jack")


print("""CREATE DECORATOR IN CLASS BASE""")
class CountCallNumber:

    def __init__(self, func):
        self.func = func
        self.call_number = 0

    def __call__(self, *args, **kwargs):
        self.call_number += 1
        print("This is execution number " + str(self.call_number))
        return self.func(*args, **kwargs)

@CountCallNumber
def say_hi(name):
    print("Hi! My name is " + name)

say_hi("Jack")
# This is execution number 1
# Hi! My name is Jack

say_hi("James")
# This is execution number 2
# Hi! My name is James
