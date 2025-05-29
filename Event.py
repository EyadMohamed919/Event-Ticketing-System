from customtkinter import *

class Event:
    def __init__(self, Name, Location, Time):
        self.Name = Name
        self.Location = Location
        self.Time = Time
        self.UserList = []
        print("Event System Started")
        print(f"Added Event {self.Name}, at location: {self.Location}, at {self.Time}")

    def getName(self):
        return self.Name

    def getLocation(self):
        return self.Location

    def getTime(self):
        return self.Time

    def addUser(self, user, NoTickets):
        for i in range(NoTickets):
            self.UserList.append(user)
            print(f"Added user: {user} to event: {self.Name}")
            print(self.UserList)

    def showEvent(self):
        app = CTk()
        app.geometry("1280x720")
        app.title("Event Ticketing System")
        eventFrame = CTkFrame(width=1280, height=700, corner_radius=20, fg_color="#ff0066", master=app,
                              border_width=1, border_color="#ff5e9f")
        eventFrame.pack(expand=True)
        eventFrame.place(relx=0.5, rely=0.5, anchor="center")
        app.mainloop()
