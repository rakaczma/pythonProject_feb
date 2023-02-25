def print_char(character="*", rep=10, vert=False):
    for i in range(rep):
        if vert:
            print(character)
        else:
            print(character + " ", end="")
    if not vert:
        print()
    print()

print_char()
print_char("+", 5, True)
print_char("^", 7, False)