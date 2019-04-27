import requests
import sys
import googlemaps
import urllib
import MySQLdb
from datetime import datetime

URL = 'https://api.darksky.net/forecast/1f6bf3c3f3b572567ae46ac0343b974c/'
KEY = 'AIzaSyBtFVBD73TGr0-jAGUq_3qO-o1StlH2PsY'

local = ' '.join(sys.argv[1:])

gmaps = googlemaps.Client(key=KEY)
geocode_result = gmaps.geocode(local)
location = geocode_result[0]['geometry']['location']

PARAMS = {
    'units': 'si',
    'exclude': 'minutely,hourly,daily,alerts,flags'
}

# request = requests.get(url=f"{URL}{location['lat']},{location['lng']}/?units=si&exclude=minutely,hourly,daily,alerts,flags")
request = requests.get(url=f"{URL}{location.get('lat')},{location.get('lng')}", params=PARAMS)
print('type before', request)
response = request.json()
print('type', type(response))
print(response)

temp = response['currently']['temperature']
sencacao = response['currently']['apparentTemperature']
print(f"Temperatura: {temp} ºC")
print(f"Sensação térmica: {sencacao} ºC")

conn = MySQLdb.connect(db='temperatura', user='root', password='rocambole')
cur = conn.cursor()
cur.execute(f'''
        INSERT INTO consultas (local, temp, sensacao_termica, data_consulta) VALUES('{local}', {temp}, {sencacao}, '{datetime.now()}')
    ''')
conn.commit()
cur.close()


