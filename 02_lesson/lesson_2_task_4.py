def fizz_buzz(n):
    for i in range(1, n + 1):
        a = str(i) * (i % 5 != 0) * (i % 3 != 0)
        a += "Fizz" * (i % 3 == 0)
        a += "Buzz" * (i % 5 == 0)
        print(a)


fizz_buzz(17)
