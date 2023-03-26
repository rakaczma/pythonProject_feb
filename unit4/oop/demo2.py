class MyClass:
    def __init__(self, x = 1):
        self.x = x # właściwość ustawiana na konstruktorze

    def sety(self, y):
        self.y = y # właściwość ustawiana w metodzie

obj1 = MyClass()   # ustawiamy właściwość x=1

obj2 = MyClass(4)  # ustawiamy właściwość x=4
obj2.sety(7)       #  ustawiamy właściwość y=7

obj3 = MyClass(3)
obj3.z = 99        # dodajemy nową właściwość i ustawiamy ją na z=99


print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)