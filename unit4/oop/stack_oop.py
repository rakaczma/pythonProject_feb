class Stack: # definiujemy klasę stosu
    def __init__(self): # definiujemy konstruktor
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del  self.__stack_list[-1]
        return val

    def show(self):
        print(self.__stack_list)

#---------------------------------------

obj = Stack()
obj2 = Stack()
obj3 = Stack()

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

obj3.push("Ania")
obj3.push("Zosia")
obj3.push("Tomek")

# obj.__stack_list = [4, 4, 4]

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())
print()
# print(len(obj.__stack_list))

print(obj.pop())
print(obj.pop())
print(obj.pop())

print(obj.pop())
print(obj.pop())
print(obj.pop())