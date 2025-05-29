import customtkinter as ctk
import os
import json
import random

app = ctk.CTk()
app.geometry("1280x720")
app.title("Event Ticketing System")

tickets_file = "tickets.json"
data_path = "profile_data.json"
event_data_path = "event_data.json"

def load_profile():
    if os.path.exists(data_path):
        with open(data_path, "r") as file:
            return json.load(file)
    return {"name": "", "age": "", "email": ""}

def save_profile(data):
    with open(data_path, "w") as f:
        json.dump(data, f)


def load_events():
    if os.path.exists(event_data_path):
        with open(event_data_path, "r") as f:
            return json.load(f)
    return []

def load_tickets():
    if os.path.exists(tickets_file):
        with open(tickets_file, "r") as file:
            return json.load(file)
    return []

def save_tickets(tickets):
    with open(tickets_file, "w") as f:
        json.dump(tickets, f, indent=4)

def purchase_ticket(event):
    ticket_number = random.randint(1000, 9999)
    ticket = {
        "ticket_number": ticket_number,
        "event_name": event["name"],
        "location": event["location"],
        "time": event["time"]
    }
    tickets = load_tickets()
    tickets.append(ticket)
    save_tickets(tickets)

def refund_ticket(ticket, parent_frame):
    tickets = load_tickets()
    updated = [t for t in tickets if t["ticket_number"] != ticket["ticket_number"]]
    save_tickets(updated)
    parent_frame.destroy()

def show_purchased_tickets():
    top = ctk.CTkToplevel(app)
    top.geometry("400x500")
    top.title("Purchased Tickets")

    tickets = load_tickets()

    if not tickets:
        ctk.CTkLabel(top, text="No tickets purchased yet.").pack(pady=20)
    else:
        for ticket in tickets:
            ticket_frame = ctk.CTkFrame(top)
            ticket_frame.pack(pady=5, padx=10, fill="x")

            ticket_text = f"#{ticket['ticket_number']} - {ticket['event_name']}\n{ticket['location']} at {ticket['time']}"
            ctk.CTkLabel(ticket_frame, text=ticket_text, font=("Arial", 12)).pack(side="left", padx=10)

            ctk.CTkButton(ticket_frame, text="Refund", width=80, command=lambda t=ticket, f=ticket_frame: refund_ticket(t, f)).pack(side="right", padx=10)

left_frame = ctk.CTkFrame(app, width=250)
left_frame.pack(side="left", fill="y", padx=20, pady=20)


def open_profile_window():
    win = ctk.CTkToplevel(app)
    win.geometry("400x300")
    win.title("Profile")
    win.lift()
    win.focus_force()

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
            "age": age_entry.get(),
            "email": email_entry.get()
        }
        save_profile(new_data)
        global user_profile
        user_profile = new_data
        win.destroy()

    ctk.CTkButton(win, text="Save", command=save_and_close).pack(pady=20)

user_profile = load_profile()


profile_button = ctk.CTkButton(master=left_frame, text="Profile", command=open_profile_window)
profile_button.pack(pady=(20, 10))


purchased_button = ctk.CTkButton(master=left_frame, text="Tickets Purchased", command=show_purchased_tickets)
purchased_button.pack(pady=(20, 10))

main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

ctk.CTkLabel(main_frame, text="Available Events", font=("Arial", 24)).pack(pady=10)

for event in load_events():
    event_frame = ctk.CTkFrame(main_frame)
    event_frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(event_frame, text=event["name"], font=("Arial", 18)).pack(side="left", padx=10)
    ctk.CTkLabel(event_frame, text=f"Location: {event['location']}", font=("Arial", 14)).pack(side="left", padx=10)
    ctk.CTkLabel(event_frame, text=f"Time: {event['time']}", font=("Arial", 14)).pack(side="left", padx=10)

    ctk.CTkButton(event_frame, text="Purchase", command=lambda e=event: purchase_ticket(e)).pack(side="right", padx=10)

app.mainloop()
