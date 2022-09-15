nimet = set()
stop = ('')
nimi = '____'

while nimi != stop:
    nimi = input('Kirjoita nimi: ')
    if nimi not in nimet:
        nimet.add(nimi)
        print('Uusi nimi')
    elif nimi in nimet:
        print('Aiemmin syötetty nimi')

for i in nimet:
    print(i)