"""Задание 11, демоверсия 2023"""

f = [1] * 2030
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n - 1]

print(f[2023] / f[2020])
