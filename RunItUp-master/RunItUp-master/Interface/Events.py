# Handles holding event data in front end
from Interface import Locations, Users, Team


class Events:

    def __init__(self, name : str, time: str, date: str, location: int, field: str):
        self.name = name
        self.time = time
        self.date = date
        self.location = location
        self.field = field

        # info that will be changed later
        self.players = []
        self.teams = []

    def addPlayer(self, player: Users):
        self.players.append(player)


    def addTeam(self, team: Team):
        self.teams.append(team)