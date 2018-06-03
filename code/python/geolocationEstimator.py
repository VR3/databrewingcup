import numpy as np
import reverse_geocoder as rg
import pandas as pd
import requests
import googlemaps

# Gmaps client
gmaps = googlemaps.Client(key='AIzaSyBbIO8719Lq7W_QM_GDOBz-oJsiJz3sEi8')

# Dataframe in Pandas
df = pd.read_csv('../data/subagencias.csv')
df.info()

# Create arrays for State and City
states = []
cities = []

# Iterate through dataframe to geocode LatLong
for index, row in df.iterrows():
	coordinates = (row["Latitud"], row["Longitud"])
	result = rg.search(coordinates)
	#result = gmaps.reverse_geocode(coordinates)
	#print (result[0])
	states.append(result[0]['admin1'])
	cities.append(result[0]['admin2'])

# Append the array to new dataframe col
df["Estado"] = states
df["Ciudad"] = cities

# Print modified
df.to_csv("subagencias_modified_geopos.csv")


# Geocoder func
def revgeo(latLng):
	result = {}
	url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={0}&key=AIzaSyBbIO8719Lq7W_QM_GDOBz-oJsiJz3sEi8'
	request = url.format(latLng)
	data = json.loads(requests.get(request).text)
	if len(data['results']) > 0:
		result = data['results'][0]
	return result
