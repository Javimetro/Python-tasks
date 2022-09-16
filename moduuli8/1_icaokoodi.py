import mysql.connector

def haelentokentta(icao):
    tuple = (icao,)
    sql = '''SELECT name, municipality FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos;


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='rootformaria',
         autocommit=True
         )

kentta = haelentokentta('007') #input puuttuu
print('kentta: ',kentta)
if not kentta is not None:
    print(f'Nimi: {kentta[0]}, kunta: {kentta[1]}')

    #3 tehtävässä lasketaan etäisyys, tarvitaan kordinaatit (longitude ja latitude_deg)
    #geopy importetaan vain "distance" eli from geopy import distance.