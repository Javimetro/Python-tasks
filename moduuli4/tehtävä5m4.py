tunnus ='python'
salasana ='rules'
toistot = 5
yritykset = 0
tunnus = input('Anna käyttäjätunnus: ')
salasana = input('Anna salasana: ')

while not (tunnus == 'python' and salasana == 'rules') and yritykset < toistot:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    yritykset += 1



if yritykset >= 5:
    print('pääsy evätty ')
else:
    print('Tervetuloa')

