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

kentta = '___'
while True:
    kentta = haelentokentta(input('Anna lentokennan ICAO koodin: '))
    if kentta is not None:
        print(kentta)
    else:
        print('Ei löydetty, yritä uudelleen.')