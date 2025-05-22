import customtkinter as ctk
import os
import json

app = ctk.CTk()
app.geometry("1280x720")
app.title("Event Ticketing System")

data_path = "profile_data.json"

def load_profile():
    if os.path.exists(data_path):
        with open(data_path, "r") as file:
            return json.load(file)
    return {"name": "", "age": "", "email": ""}

def save_profile(data):
    with open(data_path, "w") as f:
        json.dump(data, f)


user_profile = load_profile()

def open_profile_window():
    win = ctk.CTkToplevel(app)
    win.geometry("400x300")
    win.title("Profile")

    ctk.CTkLabel(win, text="Name:").pack(pady=(10, 0))
    name_entry = ctk.CTkEntry(win)
    name_entry.insert(0, user_profile.get("name", ""))
    name_entry.pack()

    ctk.CTkLabel(win, text="Age:").pack(pady=(10, 0))
    age_entry = ctk.CTkEntry(win)
    age_entry.insert(0, user_profile.get("age", ""))
    age_entry.pack()

    
    ctk.CTkLabel(win, text="Email:").pack(pady=(10, 0))
    email_entry = ctk.CTkEntry(win)
    email_entry.insert(0, user_profile.get("email", ""))
    email_entry.pack()

  
    def save_and_close():
        new_data = {
        "name": name_entry.get(),
        "age" : age_entry.get(),
        "email" : email_entry.get()
        }
        save_profile(new_data)
        win.destroy()

    ctk.CTkButton(win, text="Save", command=save_and_close).pack(pady=20)


profile_button = ctk.CTkButton(master=app, text="Profile", command=open_profile_window)
profile_button.place(x=60, y=50)

app.mainloop()