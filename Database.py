import json
class Database:

    def saveEvent(self, event):
        loaded_data = self.getAllEvents()
        event = {
            "name": event.getName(),
            "location": event.getLocation(),
            "tickets": event.getAvailableTickets(),
            "time": event.getTime()
        }
        loaded_data.append(event)
        with open("event_data.json", "w") as file:
            json.dump(loaded_data, file, indent=4)

    def getAllEvents(self):
        with open("event_data.json", "r") as file:
            loaded_data = json.load(file)
            return loaded_data

    def removeEvent(self, event):
        old_loaded_data = self.getAllEvents()
        event = {
            "name": event.getName(),
            "location": event.getLocation(),
            "time": event.getTime()
        }
        dataToBeSave = []
        print(event)
        for i in range(len(old_loaded_data)):
            if old_loaded_data[i]["name"] != event["name"]:
                dataToBeSave.append(i)

        with open("event_data.json", "w") as file:
            json.dump(dataToBeSave, file, indent=4)
