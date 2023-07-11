"""Задание № 10"""

f = [1] * 2300
for n in range(len(f)):
    if n > 3:
        if n % 2:
            f[n] = n
        else:
            f[n] = f[n - 1] + f[n - 2] + f[n - 3]
print(f[2254] - f[2252])
