import math
LUOTI = 13.3
NAULA = 32 * LUOTI
LEIVISKA = 20 * NAULA

leiviskat = input('Montako leiviskaa: ')
leiviskatGrammoina = float(leiviskat) * LEIVISKA
print(leiviskatGrammoina)
#kysy montako naula
naulat = input('montako naulaa: ')
naulatGrammoina = float(naulat) * NAULA
print(naulatGrammoina)
#kysy montako luotia
luotit = input('montako luotia: ')
luotitGrammoina = float(luotit) * LUOTI
print(luotitGrammoina)
#kerro annetut luvut LUOTI, NAULA ja  LEIVISKÄ muuttujien kanssa
Kokonaipaino = luotitGrammoina + naulatGrammoina + leiviskatGrammoina
print(Kokonaipaino)
print('Kokonaispaino grammoina on '+ str(Kokonaipaino))
print('Massa nykymittojen mukaan kilogrammoina: '+ str(math.floor(Kokonaipaino/1000)))
print('Massa nykymittojen mukaan grammoinna: ' + str(math.floor()))

