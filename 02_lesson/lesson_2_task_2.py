def is_year_leap(year):
    if year % 400 == 0:
        return True  # каждый 400 год - високосный
    if year % 100 == 0:
        return False  # каждый сотый год - невисокосный (кроме каждого 400)
    return year % 4 == 0
    # если return не прошел раньше, значит мы добрались до сюда. Тут можно проверить деление на 4


for year in (2000, 2100):
    print(f"Год {year}: {is_year_leap(year)}")
