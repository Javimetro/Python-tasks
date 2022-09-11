import math

def pizzafunktio(hinta, halkaisija):
    pizzaPA = math.pi * (halkaisija / 100 / 2) ** 2
    hintaM = hinta * pizzaPA
    return hintaM

pizza1hintta = float(input('Ensimmäinen pizzan hinta on: '))
pizza1halkaisija = float(input('Ensimmäinen pizzan halkaisija senttimetreina on: '))
tulos1 = pizzafunktio(pizza1hintta,pizza1halkaisija)
print(f' Ensimmäisen pizzan yksikköhinnan on {tulos1} €/m^2')


pizza2hinta = float(input('Toisen pizzan hinta on: '))
pizza2halkaisija = float(input('Toisen pizzan halkaisija senttimetreina on: '))
tulos2 = pizzafunktio(pizza2hinta,pizza2halkaisija)
print(f' Toisen pizzan yksikköhinnan on {tulos2} €/m^2')

if tulos1 < tulos2:
    print('Kannattaa ostaa ensimmäisen pizzan')
else:
    print('Kannattaa ostaa toisen pizzan.')