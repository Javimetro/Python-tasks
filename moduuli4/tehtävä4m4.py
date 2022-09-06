import random
salainen_n = random.randint(1,10)

user_n = int(input('Anna numeron (1-10): '))

while user_n != salainen_n:
    if user_n < salainen_n:
        print('Liian pieni arvaus :( yritä uudelleen!')
    elif user_n > salainen_n:
        print('Liian suuri arvaus :( yritä uudelleen!')
    user_n = int(input('Arva numero (1-10): '))
print('Olet voittanut!')


