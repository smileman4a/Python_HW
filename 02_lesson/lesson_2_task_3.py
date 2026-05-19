from math import ceil


def square(x):
    return ceil(x**2)


print("Введите сторону квадрата:")
str_x = input()
x = float(str_x.replace(",", "."))  # вдруг введут с запятой
print(
    f"Площадь квадрата со стороной {str_x} {'примерно ' if x != int(x) else ''}равна {square(x)}"
)
