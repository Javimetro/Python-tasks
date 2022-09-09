luku = int(input('Anna kokolaisluvun: '))

if luku == 1:
    print('ei ole alkuluku')
elif luku == 2:
    print('on alkuluku')
else:
    for i in range (2,luku):
        if luku % i == 0:
            print('ei ole alkuluku')
            break
    else:
        print('On alkuluku')
