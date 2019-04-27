import requests
import sys
import googlemaps
import urllib
import MySQLdb

# URL = 'https://api.darksky.net/forecast/1f6bf3c3f3b572567ae46ac0343b974c/'
# KEY = 'AIzaSyBtFVBD73TGr0-jAGUq_3qO-o1StlH2PsY'

# local = ' '.join(sys.argv[1:])

# gmaps = googlemaps.Client(key=KEY)
# geocode_result = gmaps.geocode(local)
# location = geocode_result[0]['geometry']['location']

# PARAMS = {
#     'units': 'si',
#     'exclude': 'minutely,hourly,daily,alerts,flags'
# }

# # request = requests.get(url=f"{URL}{location['lat']},{location['lng']}/?units=si&exclude=minutely,hourly,daily,alerts,flags")
# request = requests.get(url=f"{URL}{location.get('lat')},{location.get('lng')}", params=PARAMS)
# print('type before', request)
# response = request.json()
# print('type', type(response))
# print(response)

# print(f"Temperatura: {response['currently']['temperature']} ºC")
# print(f"Sensação térmica: {response['currently']['apparentTemperature']} ºC")

conn = MySQLdb.connect(db='world', user='brunoabe', password='91946624')

