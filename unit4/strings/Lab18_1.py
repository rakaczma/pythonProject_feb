# 1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.

alphabet = ""
polish = "ąćęłńóśżź"

for i in range(ord("a"), ord("z") + 1):
    alphabet += chr(i)
    print(chr(i), "->", ord(chr(i)))

for c in polish:
    print(c, "->", ord(c))