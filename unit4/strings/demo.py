# txt = "Ala ma kota."
#
# print(len(txt))
# print(txt[-1])
# print(len("\t\n\\"))
#
# txt = """To jest tekst. \
#         To dalsy ciąg."""
#
# txt = """a
# b
# c"""
#
# print(len(txt))

# str1 = "a"
# str2 = "b"
#
# print(str1 + str2)
# print(str2 + str1)
# print()
#
# print(str1 * 3)
# print(5 * str2)
# print()
#
# str1 += str2
# print(str1)

# char1 = "a"
# char2 = " "
#
# print(ord(char1))
# print(ord(char2))
# print()
#
# print(ord("ł"))
# print(hex(ord("ę")))
#
# print("\u0119")

# c = "a"
# print(c, ord(c), hex(ord(c)), c.encode())
#
# print()
#
# c = "\u20ac"
# print(c, ord(c), hex(ord(c)), c.encode())

# print(chr(97))
# print(chr(945))
#
# print("a" == chr(ord("a")))

#      0123456789itd
# txt = "Ala ma kota."
#
# print(txt[2])
# print(txt[-3])
#
# for i in range(len(txt)):
#     print(txt[i], end="-")
#
# for c in txt:
#     print(c)
#
#      0123456789itd
# txt = "Ala ma kota."
#
# print(txt[4:6])
# print(txt[7:])
# print(txt[-1:])
# print(txt[2::3])

# print(ord("a"))
# print(ord("z"))

alphabet = ""

# for i in range(ord("a"), ord("z") + 1):
#     print(chr(i), end="\n")

for i in range(ord("a"), ord("z") + 1):
    alphabet += chr(i)

# print(alphabet)
# print()
#
# print("a" in alphabet)
# print("abce" in alphabet)
#
# # del alphabet
# # print(alphabet)
#
# # alphabet += "AAAA"
# # print(alphabet)
#
# print(min("abcABC"))
# print(max("abcABC"))
#
# print(max("Ala ma kota."))
#
# print(alphabet.index("w"))
# print("aAbByYzZAa".index("A"))
# print([1, 2, 3].index(1))

print(list(alphabet))
print(alphabet.count("a"))
print([1, 2, 3, 2, 2, 4].count(2))