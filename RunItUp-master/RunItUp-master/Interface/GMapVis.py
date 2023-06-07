import googlemaps
from googlemaps import geocoding
from Interface import PopulateData
from BackEnd import APIdata
import tkinter
from tkintermapview import TkinterMapView
from BackEnd.retrieve_info import *

class MainWindow:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("1200x800")
        self.root.title("RunItUp")
        self.map = MapCanvas(self.root)

        self.search = SearchBar(self.root, self.map)

        self.filters = Filters(self.root, self.map)
        self.root.mainloop()




class Filters:

    def __init__(self, rootWindow:tkinter, map):
        self.map = map

        self.filterCanvas = tkinter.Canvas(rootWindow, width=100, height=500)

        self.volState = tkinter.IntVar()
        self.volleyBallBox = tkinter.Checkbutton(self.filterCanvas, text="Volleyball", variable=self.volState)
        self.filterCanvas.create_window(50, 20, window=self.volleyBallBox)


        self.basketState = tkinter.IntVar()
        self.BasketBallBox = tkinter.Checkbutton(self.filterCanvas, text="Basketball", variable=self.basketState)
        self.filterCanvas.create_window(50, 40, window=self.BasketBallBox)

        self.soccerState = tkinter.IntVar()
        self.SoccerBox = tkinter.Checkbutton(self.filterCanvas, text="Soccer", variable=self.soccerState)
        self.filterCanvas.create_window(50, 60, window=self.SoccerBox)

        self.tennisState = tkinter.IntVar()
        self.TennisBox = tkinter.Checkbutton(self.filterCanvas, text="Tennis", variable=self.tennisState)
        self.filterCanvas.create_window(50, 80, window=self.TennisBox)

        self.enterButton = tkinter.Button(text="Search", command=self.search)
        self.filterCanvas.create_window(50, 100, window=self.enterButton)


        self.filterCanvas.pack()

    def search(self):
        print(self.volState.get(), self.basketState.get(), self.soccerState.get(), self.tennisState.get())
        fields = []

        if (self.volState.get() == 1):
            fields.append('volleyball')
        if (self.basketState.get() == 1):
            fields.append('basketball')
        if (self.soccerState.get() == 1):
            fields.append('soccer')
        if (self.tennisState.get() == 1):
            fields.append('tennis')

        self.map.clearMarkers()
        self.map.populate.getLocationsFilter(fields)
        self.map.popMap()




class SearchBar:

    def __init__(self, rootWindow: tkinter, map):
        self.map = map
        self.searchCanvas = tkinter.Canvas(rootWindow, width=800, height=50)
        self.search_widget = tkinter.Entry(self.searchCanvas, width=80, justify=tkinter.LEFT)
        self.searchCanvas.create_window(450, 20, window=self.search_widget)
        self.enterButton = tkinter.Button(text="Search", command=self.updateSearch)
        self.searchCanvas.create_window(725, 20, window=self.enterButton)
        self.searchCanvas.pack()

    def updateSearch(self):
        text = self.search_widget.get()
        res = geocoding.geocode(googlemaps.Client("AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0"), address=text)
        if len(res) == 0:
            self.search_widget.insert(0, "Not a valid address")
        else:
            lat = res[0]['geometry']['location']['lat']
            long = res[0]['geometry']['location']['lng']
            APIdata.popWithGoogleAndStoreInBackEnd((lat, long), self.map.populate.radius)


            self.map.setMapLocation((lat,long))
            self.map.raidusSearch()
            self.map.popMap()




class MapCanvas:

    def __init__(self, rootWindow: tkinter):
        self.root = rootWindow
        self.mapCanvas = tkinter.Canvas(rootWindow, width=800, height=600)
        self.map_widget = TkinterMapView(self.mapCanvas, width=800, height=600, corner_radius=0)
        self.mapCanvas.create_window(400, 200, window=self.map_widget)
        self.mapCanvas.pack(side=tkinter.BOTTOM)
        self.map_widget.pack(side=tkinter.BOTTOM, fill='both',expand=True)
        self.map_widget.set_position(37.220090, -80.422660)
        self.populate = PopulateData.PopulateGmap((37.220090, -80.422660), 50)
        self.popMap()
        self.map_widget.set_zoom(15)



    def popMap(self):
        #self.map_widget.set_position(self.populate.userLocation[0],self.populate.userLocation[1])

        for i in self.populate.locationsOnMap:
            self.map_widget.set_marker(float(i.latitude), float(i.longitude), text=i.name)


    def raidusSearch(self):
        self.populate.getAllLocationsNearUser()

    def clearMarkers(self):
        while len(self.map_widget.canvas_marker_list) != 0:
            self.map_widget.canvas_marker_list[0].delete()
        self.root.update()

    def popMapWithData(self, locationList):
        for i in locationList:
            self.map_widget.set_marker(float(i.latitude), float(i.longitude), text=i.name, data=i)


    def setMapLocation(self, location:tuple):
        self.map_widget.set_position(location[0], location[1])
        self.populate.setUserLocation((location[0], location[1]))
