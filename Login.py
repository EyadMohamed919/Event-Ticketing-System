from customtkinter import *
from System import System
from Profile import Profile
class Login:

    def __init__(self):
        self.app = CTk()
        self.app.geometry("1280x720")
        self.app.title("Event Ticketing System")

        # Create login frame
        self.login_frame = CTkFrame(master=self.app, corner_radius=10, width=600)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.message = CTkLabel(master=self.app, text="", font=CTkFont(size=20, weight="bold"), text_color="#ff0000")
        self.message.place(relx=0.5, rely=0.1, anchor="center")

        # Title label
        self.title = CTkLabel(self.login_frame, text="Login", font=CTkFont(size=20, weight="bold"))
        self.title.pack(pady=(20, 10))

        # Username entry
        self.username = CTkEntry(self.login_frame, placeholder_text="Username", width=200, height=35,
                                           corner_radius=8)
        self.username.pack(pady=10)

        # Password entry
        self.password = CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=200,
                                           height=35, corner_radius=8)
        self.password.pack(pady=10)

        # Login button
        self.login_button = CTkButton(self.login_frame, text="Login", width=200, height=35,
                                          corner_radius=8, command=lambda :self.authenticate())
        self.login_button.pack(pady=20)

        self.guestButton = CTkButton(self.login_frame, text="Login as Guest", width=200, height=35,
                                      corner_radius=8, command=lambda: self.loginGuest(), fg_color="#ff00f2")
        self.guestButton.pack(pady=20)

        # Login Container
        self.app.mainloop()

    def loginGuest(self):
        self.app.withdraw()
        profile = Profile()
        profile.showWindow()

    def authenticate(self):
        username = self.username.get()
        password = self.password.get()


        if username == "admin" and password == "123":
            self.app.withdraw()
            system = System()
            system.showWindow()

        else:
            self.message.configure(text="Incorrect Email or Password")


Login()
