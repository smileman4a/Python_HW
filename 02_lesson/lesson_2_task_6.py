lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
a = [el for el in lst if el < 30 and el % 3 == 0]
print(*a)
