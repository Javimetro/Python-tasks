import random
n = int(input('Kuinka monta nopaa? '))
lukulist = []

for i in range(n):
    luvut = (random.randint(1,6))
    lukulist.append(luvut)
    print(luvut)

listsumma = sum(lukulist)
print(f'tuolosten summa on: {listsumma}')