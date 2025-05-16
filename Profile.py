from customtkinter import *
from PIL.ImageOps import Image

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

user_profile = Profile(Name=input(), Age=input(), Email=input())

ProfileIcon = CTkFrame(width=100, height=100, corner_radius=50, fg_color="#001e63", master=app, border_width=1, border_color="#385ffc")


icon_image = Image.open("blank.png")
icon_image = icon_image.resize((40, 40))
icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(40, 40))


icon_label = CTkLabel(master=ProfileIcon, image=icon, text="")
icon_label.place(relx=0.5, rely=0.5, anchor="center")

ProfileIcon.place(x=100, y=100)

app.mainloop()
