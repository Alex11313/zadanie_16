"""Задание № 8, показать как работают исключения"""

def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 3 == 0:
        return n + f(n / 3 + 2)
    if n > 5 and n % 3 != 0:
        return n + f(n + 3)

for n in range(1, 10000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except:
        pass
