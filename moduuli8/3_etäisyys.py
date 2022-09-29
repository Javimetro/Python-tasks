
import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='rootformaria',
         autocommit=True
         )



def haelongitudeicaolla(icao):
    tuple = (icao,)
    sql = '''SELECT latitude_deg, longitude_deg FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    print(tulos)
    return tulos


icao1 = input('Anna ensimmäisen lentoaseman ICAO koodin: ')
icao2 = input('Anna toisen lentoaseman ICAO koodin: ')

print(f' Etäisyys lentokenttien välillä on: {round(geodesic(haelongitudeicaolla(icao1), haelongitudeicaolla(icao2)).km,3)} Km.')