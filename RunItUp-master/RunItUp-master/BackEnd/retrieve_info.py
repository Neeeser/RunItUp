from firebase_admin import db

'''
Search the player database table and return all players where
field = value
'''
def getPlayerInfo(params: dict):
    players = db.reference('root/backend/players').get()
    res = []

    for player in players:
        equal = True
        for key, value in params.items():
            if player[key] != value:
                equal = False
                break
        if equal:
            res.append(player)

    return res

'''
Get all players from the database.
'''
def getAllPlayers():
    return db.reference('root/backend/players').get()


'''
Search the location database table and return all players where
field = value
'''

def getLocationInfo(params: dict):
    locations = db.reference('root/backend/locations').get()
    res = []

    for location in locations:
        for key, value in params.items():
            if key == 'fields':
                for val in value:
                    if location[key][val] != 0:
                        res.append(location)
            else:
                if location[key] == value:
                    res.append(location)

    return res

'''
Get all locations from the database.
'''
def getAllLocations():
    return db.reference('root/backend/locations').get()

'''
Search the event database table and return all events where
field = value
'''
def getEventInfo(params: dict):
    events = db.reference('root/backend/events').get()
    res = []

    for event in events:
        for key, value in params.items():
            if key == 'fields':
                if event[key][value] != 0:
                    res.append(event)
            else:
                if event[key] == value:
                    res.append(event)

    return res

'''
Get all events from the database.
'''
def getAllEvents():
    return db.reference('root/backend/events').get()


'''
Run a few example searches
'''
def exampleSearchs():
    # returns a list of results from the search
    print('\n--searching for player with id "0"--')
    player = getPlayerInfo({'id': 0})
    for i in range(len(player)):
        print('name:', player[i]['name'], 'id:', player[i]['id'])

    print('\n--searching for player with name "carlos urbina"--')
    player = getPlayerInfo({'name': 'carlos urbina'})
    for i in range(len(player)):
        print('name:', player[i]['name'], 'id:', player[i]['id'])

    print('\n--searching for location with name "prairie quad"--')
    location = getLocationInfo({'name': 'prairie quad'})
    for i in range(len(location)):
        print('name:', location[i]['name'])
        print('id:', location[i]['id'])
        print('hours:', location[i]['hours'])
        print('address:', location[i]['address'])
        print('geolocation:', location[i]['geolocation'])
        print('fields:', location[i]['fields'])

    print('\n--searching for location with id "1"--')
    location = getLocationInfo({'id': 1})
    for i in range(len(location)):
        print('name:', location[i]['name'])
        print('id:', location[i]['id'])
        print('hours:', location[i]['hours'])
        print('address:', location[i]['address'])
        print('geolocation:', location[i]['geolocation'])
        print('fields:', location[i]['fields'])

    print('\n--searching for event with id "0"--')
    events = getEventInfo({'id': 0})
    for i in range(len(events)):
        event = events[i]
        print('id:', event['id'])
        print('name:', event['name'])
        print('location:', event['location'])
        print('players:')
        for player in event['players']:
            print(getPlayerInfo('id', player))
        print('field:', event['field'])
        print('date:', event['date'])
        print('time:', event['time'])

    print('\n')
