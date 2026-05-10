def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            i = "FizzBuzz"
        elif i % 5 == 0:
            i = "Buzz"
        elif i % 3 == 0:
            i = "Fizz"
        print(i)


# громоздко переделать

fizz_buzz(17)
