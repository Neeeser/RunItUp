import gmaps
from Interface import PopulateData
import tkinter
from tkinter import *
from tkintermapview import TkinterMapView
from BackEnd.retrieve_info import *

def testGPLOT():
    gmaps.configure(api_key="AIzaSyA-BRYsxwC4d1mNlFOwwjJtaQI9HGLm5u0")
    populate = PopulateData.PopulateGmap((37.220090, -80.422660), 50)

    populate.getAllLocationsNearUser()
    marker_locations =[]

    for i in populate.locationsOnMap:
        marker_locations.append(i.getLocation())
        print(i.getLocation())

    #fig = gmaps.figure()
    #markers = gmaps.marker_layer(marker_locations)
    #fig.add_layer(markers)

    root_tk = tkinter.Tk()
    root_tk.geometry("500x500")
    root_tk.title("Google Maps")

    def ScheduleEvent():
        e = Entry(PopUp, width= 50)
        e.pack()
        e.insert(0, "Enter your Name: ")

    def eventsPopUp(marker):
        global PopUp
        print(marker.data.id)
        PopUp = Toplevel(root_tk)
        PopUp.title('Event List')
        PopUp.geometry('400x650')

        popUpLabel = Label(PopUp, text='LIST OF EVENTS')
        popUpLabel.pack(pady=10)

        #geo = [marker.data.latitude, marker.data.longitude]
        for event in getEventInfo({'id': marker.data.id}):
            event_name = event['name'] + ':'
            event_label1 = Label(PopUp, text=event_name)
            event_label1.pack(pady=5)

            event_location = getLocationInfo({'id': event['location']})

            event_location_name = event_location[0]['name']
            event_label2 = Label(PopUp, text=event_location_name)
            event_label2.pack(pady=5)

            time = int(event['time']) % 12
            if (time == event['time']):
                suffix = 'PM'
            else:
                suffix = 'AM'
            event_date_time = event['date'] + ' at ' + str(time) + suffix
            event_label3 = Label(PopUp, text=event_date_time)
            event_label3.pack(pady=5)

            separator = Label(PopUp, text="-----------------")
            separator.pack(pady=5)

        myFrame = Frame(PopUp)
        myFrame.pack(pady=5)

        ScheduleButton = Button(myFrame, text='Schedule', command=ScheduleEvent)
        ScheduleButton.grid(row=0, column=1)
        ScheduleButton.pack(pady=20)
    #map inside window
    map_widget = TkinterMapView(root_tk, width=600,height=400,corner_radius=0)
    map_widget.pack(fill='both',expand=True)
    for i in populate.locationsOnMap:
        map_widget.set_marker(float(i.latitude), float(i.longitude), text=i.name, command=eventsPopUp, data=i)

    map_widget.set_position(37.220090, -80.422660)
    map_widget.set_zoom(15)

    root_tk.mainloop()


