# Location Object
# Purpose is to hold data about the location you are trying to add

from Interface import Field
from Interface import Timeslots



class Locations:

    def __init__(self, name : str, address: str, latitude: int, longitude: int, fields: dict, new_id=0):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.fields = fields
        self.timeslots = Timeslots.Timeslot()
        self.id = new_id

    def __str__(self):
        return self.name

    def addField(self, field : Field):
        self.fields.append(field)

    def getLocation(self) ->tuple:
        return float(self.latitude), float(self.longitude)
