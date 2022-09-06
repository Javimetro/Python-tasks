luvut = []

while True:
    data = input('kirjoita lukusi: ')
    if data == '':
        break
    luvut.append(data)


print('isoin luku on:' + max(luvut))

print('pienin luku on:' + min(luvut))