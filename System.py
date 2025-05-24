from PIL.ImageOps import expand
from customtkinter import *
from Event import Event
import tkinter as tk
from docutils.nodes import transition


class System:
   
    def __init__(self):
        self.Ycoordinates = 0.1
        self.EventList = []
        

    def addEvent(self, name, location, date):
        event = Event(name.get(), location.get(), date.get())
        self.EventList.append(event)
        print("Event added to the system")
        print(self.EventList)

        # GUI
        eventFrame = CTkFrame(width=700, height=100, corner_radius=20, fg_color="#ff0066", master=eventContainerFrame, border_width=1,
                             border_color="#ff5e9f")
        eventFrame.pack(expand=True)
        eventFrame.place(relx=0.43, rely=self.Ycoordinates, anchor="center")

        evenTitle = CTkLabel(text=name.get(), master=eventFrame, font=("Brick 3D", 24))
        evenTitle.place(relx=0.1, rely=0.5, anchor="center")

        evenLocation = CTkLabel(text="Location: " + location.get(), master=eventFrame, font=("Cascadia Code", 19))
        evenLocation.place(relx=0.3, rely=0.5, anchor="center")

        evenDate = CTkLabel(text="Date: " + date.get(), master=eventFrame, font=("Cascadia Code", 19))
        evenDate.place(relx=0.6, rely=0.5, anchor="center")

        # eventDetailFrame = CTkFrame(width=1280, height=720, corner_radius=0, fg_color="transparent", master=app)
        # eventDetailFrame.place(relx=0.5, rely=0.5, anchor="center")
        #
        # eventContainerFrame.tkraise()
        # formFrame.tkraise()

        viewButton = CTkButton(master=eventFrame, width=80, height=40, text="View", corner_radius=32,
                               fg_color="#4158D0", command=lambda:self.raiseTK(event))
        viewButton.place(relx=0.87, rely=0.5, anchor="center")
        self.Ycoordinates += 0.2

    def getAllEvents(self):
        return self.EventList

    def raiseTK(self, event):
        event.showEvent()

app = CTk()
app.geometry("1280x720")
system = System()
app.title("Event Ticketing System")

# Event Container data
eventContainerFrame = CTkFrame(width=900, height=800, corner_radius=40, fg_color="#001e63", master=app, border_width=1, border_color="#385ffc")
eventContainerFrame.pack(expand=True)
eventContainerFrame.place(relx=0.65, rely=0.5, anchor="center")

# Form data
formFrame = CTkFrame(width=400, height=600, corner_radius=40, fg_color="#001e63", master=app, border_width=1, border_color="#385ffc")
formFrame.pack(expand=True)
formFrame.place(relx=0.2, rely=0.5, anchor="center")


formTitle = CTkLabel(text="Add Event", master=formFrame, font=("Arial", 20))
formTitle.place(relx=0.5, rely=0.1, anchor="center")

nameInput = CTkEntry(master=formFrame, text_color="#4a6eff", placeholder_text="Enter event name", width=300)
nameInput.place(relx=0.5, rely=0.3, anchor="center")


locationInput = CTkEntry(master=formFrame, text_color="#4a6eff", placeholder_text="Enter event location", width=300)
locationInput.place(relx=0.5, rely=0.4, anchor="center")

dateInput = CTkComboBox(master=formFrame, text_color="#4a6eff", width=300, values=["6pm-8pm", "8:30pm-9:30pm", "10pm-12pm"])
dateInput.place(relx=0.5, rely=0.5, anchor="center")

dontButton = CTkButton(master=formFrame, width=100, height=60, text="Done", corner_radius=32, fg_color="#4158D0", command=lambda:system.addEvent(nameInput, locationInput, dateInput))
dontButton.place(relx=0.5, rely=0.7, anchor="center")



app.mainloop()