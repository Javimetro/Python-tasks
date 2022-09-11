import random

def noppa ():
    arvo = random.randint(1,6)
    return arvo

arvo = random.randint(1,6)
while arvo != 6:
    arvo=noppa()
    print(arvo)