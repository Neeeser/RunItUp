import googlemaps

from BackEnd.BootUp import *
from BackEnd.set_info import *
from Interface import Locations
from BackEnd import APIdata
from BackEnd import set_info
from Interface import PopulateData
from Testing import testGMPLOT
from Interface import GMapVis
'''
Bootup the firebase database connection. If so desired, reload all of the default information
'''

initialize_firebase(loadDefaults=False)

# add some new players to the database
# new_player = User('leo', 'messi')
# setNewPlayer(new_player)

# new_player = User('michael jordan', 'the_goat')
# setNewPlayer(new_player)

#exampleSearchs()
#APIdata.popWithGoogleAndStoreInBackEnd((37.220090, -80.422660), "Tennis", 50)
#APIdata.popWithGoogleAndStoreInBackEnd((37.220090, -80.422660), "Basketball", 50)

GMapVis.MainWindow()
