
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input('Mitä on sinun sukupuolesi?: ')
hb = int(input('Kirjoita hemoglobiiniarvosi (g/l): '))

if sukupuoli=='Mies' or sukupuoli=='mies' and 134<=hb<195:
    print('Sinun hemoglobiiniarvo on normaali.')
elif sukupuoli=='Mies' or sukupuoli=='mies' and 134>hb:
    print('Sinun hemoglobiiniarvo on matala.')
elif sukupuoli=='Mies' or sukupuoli=='mies' and 195<hb:
    print('Sinun hemoglobiiniarvo on korkea.')

if sukupuoli=='Nainen' or sukupuoli=='nainen' and 117<=hb<175:
    print('Sinun hemoglobiiniarvo on normaali.')
elif sukupuoli=='Nainen' or sukupuoli=='nainen' and 117>hb:
    print('Sinun hemoglobiiniarvo on matalia.')
elif sukupuoli=='Nainen' or sukupuoli=='nainen' and 175<hb:
    print('Sinun hemoglobiiniarvo on korkea.')