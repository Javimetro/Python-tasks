lentoasemat = {'Helsinki' : 'EFHK'}
sh = '____'
while sh != 'STOP':
    sh = input('Haluatko hakea lentoaseman(H), syöttää uuden lentoaseman(S) vai lopettaa(STOP)?: ')
    if sh == 'H':
        lentoasema = input('Kirjoita lentoaseman nimen: ')
        print(lentoasemat.get(lentoasema,'Ei löydetty :('))
    elif sh == 'S':
        lentoasema = input('Kirjoita lentoaseman nimen: ')
        koodi = input('Kirjoita lentoaseman ICAO-koodin: ')
        lentoasemat[lentoasema]=koodi
        print('Tiedot tallennetut.')
    else:
        print('Kirjoita (H) hakemiseen, (S) tideon syöttämiseen tai (STOP) lopettamiseen')

print('Hyvästi!')