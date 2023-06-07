from firebase_admin import db
from Interface.Users import *
from Interface.Timeslots import *
from BackEnd.retrieve_info import *

'''
Add a new User/Player object to the database. Does not allow for repeat usernames.
'''
def setNewPlayer(player):
    players = db.reference('root/backend/players') # get reference to players branch

    player_name = player.name
    username = player.username

    for player in players.get():    # ensure no repeat usernames
        if player['username'] == username:
            return False

    new_key = len(players.get())    # new index to add to
    new_player = { new_key: { "name": player_name, "username": username} }

    players.update(new_player)      # push to DB
    return True


'''
Add a new Location to the database. Does not allow for repeat id values.
'''
def setNewLocation(location):
    locations = db.reference('root/backend/locations') # get reference to players branch

    # turn lat long info into a tuple
    location_geo = [location.latitude, location.longitude]

    new_id = len(locations.get())    # new id


    for currLocation in locations.get():    # ensure no repeat ids
        if currLocation['geolocation'] == location_geo:
            return False

    # create the new json style dict, mapping id to location object
    new_location = { new_id: { "id": new_id, 
                            "name": location.name,
                            "address": location.address,
                            "geolocation": location_geo,
                            "fields": location.fields,
                            "timeslots": location.timeslots.times }}

    locations.update(new_location)      # push to DB
    return True


'''
Add a new Event to the database. The player creating the event is automatically joined.
Does not allow for repeat id values. The location's timeslot information will be adjusted.
'''
def setNewEvent(new_event, player):
    events = db.reference('root/backend/events') # get reference to players branch

    new_id = len(events.get())    # new id

    same_location_list = getEventInfo({'location': new_event.location})    
    for similar_event in same_location_list:        # ensure no repeat time/locations
        if similar_event['time'] == new_event.time and similar_event['date'] == new_event.date and similar_event['field'] == new_event.field:
            return False


    # create the new json style dict, mapping id to location object
    new_event_dict = { new_id: { "id": new_id, 
                            "name": new_event.name,
                            "date": new_event.date,
                            "location": new_event.location,
                            "field": new_event.field,
                            "players": [player],
                            "time": new_event.time} }

    events.update(new_event_dict)      # push to DB

    # update the location's timeslot info
    location_list = getLocationInfo({'id': new_event.location})
    location = location_list[0]
    timeslots = location['timeslots']
    timeslots[int(new_event.time)] = True

    # get the path to this location in the database and write to it
    path = '/root/backend/locations/' + str(new_event.location)
    location_ref = db.reference(path)
    location_ref.update(location)

    return True

'''
Add the player with given username to the event with given id
'''
def joinEvent(event_id, player):
    #print('adding player w/ username', player['username'], 'to the event w/ id', event_id)
    
    # find the event based on the id
    event_list = getEventInfo({'id': event_id})
    if len(event_list) == 0:    # event not found
        return False

    # add the player
    event_to_join = event_list[0]
    event_to_join['players'].append(player)
    path = '/root/backend/events/' + str(event_id)
    player_list = db.reference(path)
    player_list.update(event_to_join)
    return True


# Caches new user location in database so we don't have to search there again
# Stores a location tuple and a radius
def setNewUserLocation(location: tuple, radius: int):
    users = db.reference('root/backend/UserLocations') # get reference to players branch



    for usrLoc in users.get():    # ensure no repeat usernames
        if usrLoc['location'][0] == location[0] and usrLoc['location'][1] and usrLoc["radius"] >= radius:
            return False


    new_key = len(users.get())    # new index to add to
    new_userLoc = { new_key: { "location": location, "radius": radius} }

    users.update(new_userLoc)      # push to DB
    return True

