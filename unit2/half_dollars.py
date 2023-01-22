# liczba produkcji monet półdolarowych w latach 2012, 2013, 2014 w Denver i Philadelphi
denver = [1_700_000, 4_600_000, 2_100_000]
philadelphia = []
philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

total = [0, 0, 0]
total[0] = denver[0] + philadelphia[0]
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]

average = (total[0] + total[1] + total[2]) / len(total)
print("{:,d}".format(total[0]).replace((","," ")))
print("Produkcja w roku 2012 wyniosła", total[0], "sztuk.")
print("Produkcja w roku 2013 wyniosła", total[1], "sztuk.")
print("Produkcja w roku 2014 wyniosła", total[2], "sztuk.")