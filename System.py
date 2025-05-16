from PIL.ImageOps import expand
from customtkinter import *
from docutils.nodes import transition


class System:
   
    def __init__(self):
        self.EventList = []
        

    def addEvent(self, event):
        self.EventList.append(event)

    def getAllEvents(self):
        return self.EventList

    def show(self):
        print("Hello world")

app = CTk()
app.geometry("1280x720")
system = System()
app.title("Event Ticketing System")

# Event Container data
eventContainerFrame = CTkFrame(width=900, height=700, corner_radius=40, fg_color="#001e63", master=app, border_width=1, border_color="#385ffc")
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

dontButton = CTkButton(master=formFrame, width=100, height=60, text="Done", corner_radius=32, fg_color="#4158D0")
dontButton.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()