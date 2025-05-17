from customtkinter import *
from PIL import Image
import os

class Profile:
    def __init__(self, Name, Age, Email):
        self.name = Name
        self.age = Age
        self.email = Email

    def Get_info(self):
        return (self.name, self.age, self.email)




app = CTk()
app.geometry("1280x720")
app.title("Event Ticketing System")


name = input("Enter name: ")
age = input("Enter age: ")
email = input("Enter email: ")

user_profile = Profile(Name=name, Age=age, Email=email)


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "blank.png")
profile_img = CTkImage(light_image=Image.open(desktop_path), size=(60, 60))


CTkEntry(master=app, text_color="#4a6eff", placeholder_text="Enter event name", width=300)


profile_button = CTkButton(master=app, image=profile_img, width=60, height=60, corner_radius=100, fg_color="white", border_width=2, border_color="white")

profile_button.place(x=60, y=50)

app.mainloop()
