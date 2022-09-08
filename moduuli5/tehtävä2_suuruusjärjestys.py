list = []
stop = ('')
luku = '___'

while (luku != ''):
    luku = input('Kirjoita luvun: ')
    if luku != '':
        list.append(luku)
        list.sort(reverse=True)

else:
    print(f'Viisi suurimmat luvut ovat: {list[0:6]}')