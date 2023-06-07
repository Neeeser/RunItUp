####################################### IMPORTS
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from BackEnd.retrieve_info import getPlayerInfo
import googlemaps
import json
from datetime import datetime
from BackEnd.BootUp import *
from Interface import Locations
from BackEnd import set_info


gmaps = googlemaps.Client(key="AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0")


sportsTypes = ["basketball", "soccer", "tennis", "volleyball"]


###################################### HELPER METHODS
def getGeocodeFromFirebase(locationDictionary):
    latlong = locationDictionary['lat'],locationDictionary['lng']
    return latlong

def getLocationDict(db_path):
    #gets a dictonary of the specific portion of the json file
    locationDict = db.reference('root/'+db_path+'/0/geometry/location').get()
    return locationDict


def searchCleanUp(db_path):
    rejectedHeaders = ['icon','icon_background_color','icon_mask_base_uri','plus_code','reference']
    db.reference('root/'+db_path+'/next_page_token').delete()

    listOfResults = db.reference('root/'+db_path+'/results').get()
    lengthOfResults = len(listOfResults)

    listOfItemsInIndex = db.reference('root/'+db_path+'/results/0').get()
    lengthOfItemsInIndex = len(listOfItemsInIndex)

    for i in range (0, lengthOfResults):
        for x in range(0, len(rejectedHeaders)):
            db.reference('root/'+db_path+'/results/'+str(i)+'/'+str(rejectedHeaders[x])).delete()

###################################### MAIN METHOD
def populateDatabase(gmaps, db_path, latLongTuple, radius):
    # Geocoding an address
    #geoCodeRes = gmaps.geocode(address)

    #dump to a json file
    #with open('customGeoSon.json','w') as fp:
    #    json.dump(geoCodeRes, fp)

    #Creates a new branch with the googlemapJson info
    gm = db.reference('root/'+db_path)

    #loads the json into the database
    #load_json_info(gm, 'customGeoSon.json')

    #gets the lat/long tuple by passing the dictionary
    #geocodeFromFB = getGeocodeFromFirebase(getLocationDict(db_path))

    # Look up type of places within 2 miles (3218.69 meters)

    places_result = {}
    for i in sportsTypes:
        places_result.update(gmaps.places(i, latLongTuple, radius))


    #dump this new GET to a new jsonFile
    with open('customplace.json','w') as f:
        json.dump(places_result, f)

    #Finally override the geocode info with the actual places we want
    load_json_info(gm, 'customplace.json')

    searchCleanUp(db_path)






######################################
def moveSavedLocationsIntoDatabase()->list:
    savedLocations = db.reference("root/SavedLocations/results").get()
    # list of saved locations turned into location objects
    locations = []

    for l in savedLocations:
        location = Locations.Locations(
            name=l['name'],
            address=l['formatted_address'],
            latitude=l['geometry']['location']['lat'],
            longitude=l['geometry']['location']['lng'],
            fields={"basketball": 0, "volleyball": 0, "soccer": 0, "tennis": 0}

        )
        locations.append(location)
    return locations


def popWithGoogleAndStoreInBackEnd(location: tuple, radius:int):
    if set_info.setNewUserLocation(location, radius):
        populateDatabase(gmaps,"SavedLocations",location, radius)
        location = moveSavedLocationsIntoDatabase()
        for i in location:
            set_info.setNewLocation(i)



