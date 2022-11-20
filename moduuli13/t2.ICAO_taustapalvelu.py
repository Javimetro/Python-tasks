import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='rootformaria',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kentta/<icao>')
def haename(icao):
    tuple = (icao,)
    sql = '''SELECT name FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    name = kursori.fetchone()
    return name

app = Flask(__name__)
@app.route('/kentta/<icao>')
def haemunicipality(icao):
    tuple = (icao,)
    sql = '''SELECT municipality FROM airport 
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    municipality = kursori.fetchone()
    return municipality

app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta(icao):
    haename(icao)
    haemunicipality(icao)
    vastaus = {
        'ICAO' : icao,
        'Name' : haename(icao),
        'Municipality' : haemunicipality(icao)
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port =3000)