
import random

N = int(input('Kirjoita pisteiden määrä: '))
toistot = 0
n= 0

while toistot < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x+y*y < 1:
        n += 1

pi = 4 * n / N
print(f'Piin likiarvo on {pi}')