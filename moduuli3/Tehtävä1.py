pituus = float(input('kirjoita kuhan pituuden senttimetreina: '))

if pituus < 37:
    puuttuuCM = 37 - pituus
    print('Heitä kuhan takaisin järveen!')
    print('Kuhan pitää kasvata ' + str(puuttuuCM) + ' cm ennen kuin saat viedä sen kotiin')


else:
    print('Kiva! saat pitää kuhan itsellesi!')

