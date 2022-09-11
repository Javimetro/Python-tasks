
gallona = float(input('Kuinka monta gallonaa? '))
def converter ():
    litra = (gallona)*3.785
    return litra


while gallona >= 0:
    gallona = converter()
    print(f'{gallona} litraa')
    gallona = float(input('Kuinka monta gallonaa? '))