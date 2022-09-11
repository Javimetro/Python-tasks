import random
banaani = int(input('Kuinka monta tahkoa? '))
def noppa ():
    arvo = random.randint(1,banaani)
    return arvo

arvo = random.randint(1,banaani)
while arvo != banaani:
    arvo = noppa()
    print(arvo)