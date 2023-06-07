from time import sleep
from BackEnd.set_info import *
from BackEnd.retrieve_info import *
from Interface import Locations
from Interface import Events

def testSetEvent():
    # create a new event, registered by player w/ id = 0
    search_params = {'name': 'Prairie Quad'}
    event_location = getLocationInfo(search_params)[0]['id']
    temp_event = Events.Events(name="pickup volleyball", time="14", date="11/14/22",
                                location=event_location, field="volleyball")
    player = getAllPlayers()[0]
    if setNewEvent(temp_event, player):
    
        # register another player to join this event
        event_to_join = getEventInfo({'name': 'pickup volleyball'})
        event_id = event_to_join[0]['id']
        player1 = getPlayerInfo({'name': 'Carlos Urbina'})[0]
        joinEvent(event_id, player1)


def testSetLocation():
    # add a new location to the database
    temp_location = Locations.Locations(name="McComas Gym", address="895 Washington St SW, Blacksburg, VA 24060",
                                latitude=37.220090, longitude=80.422660, fields={"basketball": 2, "volleyball": 1, "soccer": 1, "tennis": 0 })
    
    setNewLocation(temp_location)


def testSetPlayer():
    # add some new players to the database
    new_player = User('21', 'canyoudosomnforme')
    setNewPlayer(new_player)

    new_player = User('michael jordan', 'the_goat')
    setNewPlayer(new_player)

def create_many_events():
    # create a new event, at all soccer fields
    search_params = {'fields': ['soccer']}
    locations_list = getLocationInfo(search_params)
    for location in locations_list:
        #print(location['name'])
        event_name = "soccer pickup rematch game at " + location['name']
        #print(event_name)
        temp_event = Events.Events(name=event_name, time="11", date="11/14/22",
                                location=location['id'], field="soccer")
        player = getAllPlayers()[0]
        setNewEvent(temp_event, player)
