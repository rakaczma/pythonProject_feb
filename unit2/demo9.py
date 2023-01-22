# jeżeli temperature będzie dodatnia i będzie słonecznie to ...
# pójdziemy na spacer a jeżeli nie to zostaniemy w domu

temperature = 12
is_sun_shining = False

# if temperature > 0 and is_sun_shining: # True and False -> False
#     print("Idziemy na spacer")
# else:
#     print("Zostajemy w domu")
#
# jezeli temp bedzie ujemna lub bedzie pochmurno to zostaniemy w domu a jezeli nie to pojdziemy na spacer

# if temperature < 0 or not is_sun_shining:
#     print("Zostajemy w domu")
# else:
#     print("Idziemy na spacer")

# and - koniunkcja - czytamy jak i
# or - alternatywa - czytamy jak lub
# not - negacja - czytamy jak nie

# wyświetl cyfre chyba że ...
# liczba parzysta lub liczba większa od 6 to wyświetl *
#
# for i in range(10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)

#operatory bitowe
#
# a = 5
# b = 3
# # koniunkcja bitowa
# print(a, "&", b, "=", a & b)
# # print(bin(a))
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a & b))
#
# print()
#
# a = 5
# b = 3
# # alternatywa bitowa
# print(a, "|", b, "=", a | b)
# # print(bin(a))
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a | b))
#
# print()
#
# # alternatywa rozłączna bitowa
# print(a, "^", b, "=", a ^ b)
# # print(bin(a))
# print("{:08b}".format(a))
# print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a ^ b))
#
# print()
#
# print(a, ">>", b, "=", a >> b)
# # print(bin(a))
# print("{:08b}".format(a))
# # print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(a >> b))
#
# print()
# # negacja bitowa
# print("~" + str(a), "=", ~a)
# # print(bin(a))
# print("{:08b}".format(a))
# # print("{:08b}".format(b))
# print("-" * 8)
# print("{:08b}".format(~a))
#
# print()
#
# for i in range(5, -6, -1):
#     print("{0:08b} => {1:d}".format(i & 255, i))

a = 3
b = 4
c = 7

# def get(a):
#     print("!!!!")
#     return  a

print(a < b < c)
# znaczy to samo co
print(a < b and b < c)