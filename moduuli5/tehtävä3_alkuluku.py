luku = int(input('Anna kokonaisluvun: '))

if luku == 1:
    print('ei ole kokonaisluku')
elif luku == 2:
    print('on kokonaisluku')
else:
    for i in range (2,luku):
        if luku % i == 0:
            print('ei ole kokonaisluku')
            break
    else:
        print('On kokonaisluku')