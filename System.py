from PIL.ImageOps import expand
from customtkinter import *
from Event import Event
from Database import Database
import tkinter as tk
from docutils.nodes import transition


class System:
    MAX_EVENTS = 5
    currentNoEvents = 0
    def __init__(self):
        self.Ycoordinates = 0.1
        self.EventList = []

        self.app = CTkToplevel()
        self.app.geometry("1280x720")
        self.database = Database()
        self.app.title("Event Ticketing System")

        # Event Container data
        self.eventContainerFrame = CTkFrame(width=900, height=800, corner_radius=40, fg_color="#001e63", master=self.app,
                                       border_width=1, border_color="#385ffc")
        self.eventContainerFrame.pack(expand=True)
        self.eventContainerFrame.place(relx=0.65, rely=0.5, anchor="center")

        # Form data
        self.formFrame = CTkFrame(width=400, height=600, corner_radius=40, fg_color="#001e63", master=self.app, border_width=1,
                             border_color="#385ffc")
        self.formFrame.pack(expand=True)
        self.formFrame.place(relx=0.2, rely=0.5, anchor="center")

        self.formTitle = CTkLabel(text="Add Event", master=self.formFrame, font=("Arial", 20))
        self.formTitle.place(relx=0.5, rely=0.1, anchor="center")

        self.nameInput = CTkEntry(master=self.formFrame, text_color="#4a6eff", placeholder_text="Enter event name", width=300)
        self.nameInput.place(relx=0.5, rely=0.3, anchor="center")

        self.locationInput = CTkEntry(master=self.formFrame, text_color="#4a6eff", placeholder_text="Enter event location",
                                 width=300)
        self.locationInput.place(relx=0.5, rely=0.4, anchor="center")

        self.ticketsInput = CTkEntry(master=self.formFrame, text_color="#4a6eff",
                                      placeholder_text="Enter the number of tickets available",
                                      width=300)
        self.ticketsInput.place(relx=0.5, rely=0.5, anchor="center")

        self.dateInput = CTkComboBox(master=self.formFrame, text_color="#4a6eff", width=300,
                                values=["6pm-8pm", "8:30pm-9:30pm", "10pm-12pm"])
        self.dateInput.place(relx=0.5, rely=0.6, anchor="center")

        self.dontButton = CTkButton(master=self.formFrame, width=100, height=60, text="Done", corner_radius=32,
                               fg_color="#4158D0", command=lambda: self.addEvent(self.nameInput, self.locationInput, self.dateInput, self.ticketsInput))
        self.dontButton.place(relx=0.5, rely=0.7, anchor="center")

        self.loadData()
        self.showWindow()

    def loadData(self):
        allEvents = self.database.getAllEvents()

        for data in allEvents:
            System.currentNoEvents += 1
            event = Event(data["name"], data["location"], data["time"], data["tickets"])
            # GUI
            eventFrame = CTkFrame(width=700, height=100, corner_radius=20, fg_color="#ff0066", master=self.eventContainerFrame,
                                  border_width=1,
                                  border_color="#ff5e9f")
            eventFrame.pack(expand=True)
            eventFrame.place(relx=0.43, rely=self.Ycoordinates, anchor="center")

            eventText = f"{event.getName()}\nLocation: {event.getLocation()}\nDate: {event.getTime()}"
            evenInfo = CTkLabel(text=eventText, master=eventFrame, font=("Cascadia Code", 16), justify="left")
            evenInfo.place(relx=0.05, rely=0.5, anchor="w")

            viewButton = CTkButton(master=eventFrame, width=80, height=40, text="View", corner_radius=32,
                                   fg_color="#4158D0", command=lambda: self.raiseTK(event))
            viewButton.place(relx=0.75, rely=0.5, anchor="center")

            dontButton = CTkButton(master=eventFrame, width=80, height=40, text="Delete", corner_radius=32,
                                        fg_color="#4158D0",
                                        command=lambda: self.deleteEvent(event))
            dontButton.place(relx=0.9, rely=0.5, anchor="center")

            self.Ycoordinates += 0.2

    def addEvent(self, name, location, date, ticket):
        print(System.currentNoEvents)
        if(System.currentNoEvents < System.MAX_EVENTS):
            System.currentNoEvents += 1

            event = Event(name.get(), location.get(), date.get(), ticket.get())
            self.EventList.append(event)
            print("Event added to the system")
            print(self.EventList)

            self.database.saveEvent(event)

            # GUI
            eventFrame = CTkFrame(width=700, height=100, corner_radius=20, fg_color="#ff0066", master=self.eventContainerFrame, border_width=1,
                                 border_color="#ff5e9f")
            eventFrame.pack(expand=True)
            eventFrame.place(relx=0.43, rely=self.Ycoordinates, anchor="center")

            eventText = f"{event.getName()}\nLocation: {event.getLocation()}\nDate: {event.getTime()}"
            evenInfo = CTkLabel(text=eventText, master=eventFrame, font=("Cascadia Code", 16), justify="left")
            evenInfo.place(relx=0.05, rely=0.5, anchor="w")

            viewButton = CTkButton(master=eventFrame, width=80, height=40, text="View", corner_radius=32,
                                   fg_color="#4158D0", command=lambda:self.raiseTK(event))
            viewButton.place(relx=0.75, rely=0.5, anchor="center")

            dontButton = CTkButton(master=eventFrame, width=80, height=40, text="Delete", corner_radius=32,
                                   fg_color="#4158D0",
                                   command=lambda: self.deleteEvent(event))
            dontButton.place(relx=0.9, rely=0.5, anchor="center")
            self.Ycoordinates += 0.2

    def deleteEvent(self, event):

        for i in range(len(self.EventList)):
            if (self.EventList[i].getName() == event.getName()):
                self.EventList.pop(i)

        print("Event removed from the system")
        print(self.EventList)
        self.database.removeEvent(event)

    def getAllEvents(self):
        return self.EventList

    def raiseTK(self, event):
        event.showEvent()
    def showWindow(self):
        self.app.mainloop()

system = System()
system.showWindow()