import math
LUOTI = 13.3
NAULA = 32 * LUOTI
LEIVISKA = 20 * NAULA

leiviskat = input('Montako leiviskaa: ')
leiviskatGrammoina = float(leiviskat) * LEIVISKA
print(leiviskatGrammoina)

naulat = input('montako naulaa: ')
naulatGrammoina = float(naulat) * NAULA
print(naulatGrammoina)

luotit = input('montako luotia: ')
luotitGrammoina = float(luotit) * LUOTI
print(luotitGrammoina)

Kokonaipaino = luotitGrammoina + naulatGrammoina + leiviskatGrammoina

kilot = float(math.floor(Kokonaipaino/1000))
print('Kokonaispaino grammoina on '+ str(Kokonaipaino))
print('Massa nykymittojen mukaan kilogrammoina: '+ str(kilot))
grammat = float(math.floor(Kokonaipaino%1000))
print('Massa nykymittojen mukaan grammoinna: ' + str(grammat))