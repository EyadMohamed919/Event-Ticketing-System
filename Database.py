import mysql.connector
import json
class Database:

    def saveEvent(self, event):
        loaded_data = self.getAllEvents()
        event = {
            "name": event.getName(),
            "location": event.getLocation(),
            "time": event.getTime()
        }
        loaded_data.append(event)
        with open("event_data.json", "w") as file:
            json.dump(loaded_data, file, indent=4)

    def getAllEvents(self):
        with open("event_data.json", "r") as file:
            loaded_data = json.load(file)
            return loaded_data
