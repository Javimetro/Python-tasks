vuosiluku = int(input('Kirjoita vuosiluvun: '))
if vuosiluku%100==0 and not vuosiluku%400==0:
    print('Tämä vuosiluku ei ole karkausvuosi')
elif vuosiluku%4==0 or vuosiluku%400==0:
    print('TÄMÄ VUOSILUKU ON KARKAUSVUOSI!')
else:
    print('Tämä vuosiluku ei ole karkausvuosi')