# Single Astrics Arguments...

# def add(*args):
#     # print(type(args))
#     # for n in args:
#     #     print(n)
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 5, 6, 2 ,1))

# Double Astrics Arguments...

def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

    print(kwargs["add"])

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.colour = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)