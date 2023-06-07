# Holds data about fields
from enum import Enum
from Interface import Events
class Types(Enum):
    Basketball = 0
    Baseball = 1
    Soccer = 2
    Volleyball= 3



class Field:

    def __init__(self, fieldsDict: dict):
        self.fieldDictionary = fieldsDict

    def addEvent(self, event : Events):
        self.events.append(event)


