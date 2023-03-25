alphabet = ""
polish = "ą, ć, ę, ł, ń, ó, ś, ż, ź"

for i in range(ord("a"), ord("z") + 1):
    alphabet += chr(i)
    print(chr(i), "->", ord(chr(i)))

for i in polish:
    print(chr(i), "->", ord(chr(i)))


alphabet += polish
print(alphabet)