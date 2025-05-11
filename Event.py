class Event():

    
    def __init__(self, Location, Time, Name):
        self.Location = Location
        self.Time = Time
        self.Name = Name
        self.UserList = []
        print("Event System Started")
        print("Added Event " + self.Name + ", at location: " + self.Location + ", at " + self.Time)

    def addUser(self, user, NoTickets):
        for i in range(NoTickets):
            self.UserList.append(user)
            print("Added user: " + user + " to event: " + self.Name)
            print(self.UserList)

event1 = Event("Cairo", "11pm", "Kairokee")

event1.addUser("Ahmed", 3)


        


    