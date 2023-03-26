class MyClass:
    def __init__(self, x = 1):
        self.__x = x # prywatna zmienna instancji

    def sety(self, y):
        self.__y = y

obj1 = MyClass()   # ustawiamy właściwość x=1

obj2 = MyClass(4)  # ustawiamy właściwość x=4
obj2.sety(7)       #  ustawiamy właściwość y=7

obj3 = MyClass(3)
obj3.z = 99        # dodajemy nową właściwość i ustawiamy ją na z=99


print("obj1", obj1.__dict__)
print("obj2", obj2.__dict__)
print("obj3", obj3.__dict__)

print(obj1._MyClass__x)
print(obj3.z)