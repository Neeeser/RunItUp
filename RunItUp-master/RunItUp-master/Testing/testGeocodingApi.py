import googlemaps
import json
from datetime import datetime


gmaps = googlemaps.Client(key="AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0")
key = "AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0"
geocodeAPII = geocodeAPIData(key)
print(geocodeAPII.geocode('1600 Amphitheatre Parkway, Mountain View, CA'))
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((37.229572, -80.413940))
print(type((37.229572, -80.413940)))

# Look up type of places nearby
places_result = gmaps.places("soccer", (37.229572, -80.413940), 3218.69, "english")

# look up places using a search query
placesQuery_result = gmaps.places_autocomplete("Soccer fields near Virginia Tech")

#dump to a json file
with open('../placesDump.json', 'w') as fp:
    json.dump(places_result, fp)