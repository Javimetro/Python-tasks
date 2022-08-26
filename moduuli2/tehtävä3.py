kanta_str = input('kirjoita suorakulmion kanta: ')
kanta = float(kanta_str)
korkeus_str = input('kirjoita suorakulmion korkeus: ')
korkeus = float(korkeus_str)
pintaala = kanta * korkeus
piiri = (kanta + korkeus)*2
print('suorakulmion pinta-ala on: '+ str(pintaala))
print('suorakulmion piiri on: '+ str(piiri))