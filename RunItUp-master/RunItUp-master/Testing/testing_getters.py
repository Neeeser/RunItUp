from Testing.testing_setters import *

def test_get_player():
    params = {'username': 'couch', 'name': 'Moeed Chaudhry'}
    players = getPlayerInfo(params)
    print(players)

def test_get_location():
    params = {'fields': ['basketball']}
    locations = getLocationInfo(params)
    # for location in locations:
    #     print(location['geolocation'])

    params = {'fields': ['soccer']}
    locations = getLocationInfo(params)
    #print(len(locations))

def test_get_event(params: dict):
    events = getEventInfo(params)
    # for event in events:
    #     print(event['name'])

