"""Задание № 6"""

def f(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n > 15 and n % 3 == 0:
        return f(n - 1) + n * n + 3
    if n > 15 and n % 3 != 0:
        return f(n - 2) + n - 6

k = 0
for n in range(1, 1001):
    if '0' not in str(f(n)) and '2' not in str(f(n)) and '4' not in str(f(n)) and '6' not in str(f(n)) and '8' not in str(f(n)):
        k += 1
print(k)