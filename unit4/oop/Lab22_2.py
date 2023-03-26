class C:
    counter = 0

    def __init__(self):
        C.counter += 1

    def getcounter(self):
        return C.counter

for i in range(100):
    obj = C()

print("Utworzono obiektów: ", obj.counter)