import customtkinter as ctk
import os
import json
import random
class Profile:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Event Ticketing System")

        self.tickets_file = "tickets.json"
        self.data_path = "profile_data.json"
        self.event_data_path = "event_data.json"
        # self.user_profile = self.load_profile()
        self.left_frame = ctk.CTkFrame(self.app, width=250)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        self.profile_button = ctk.CTkButton(master=self.left_frame, text="Profile", command=self.open_profile_window)
        self.profile_button.pack(pady=(20, 10))

        self.purchased_button = ctk.CTkButton(master=self.left_frame, text="Tickets Purchased", command=self.show_purchased_tickets)
        self.purchased_button.pack(pady=(20, 10))

        self.balanceIndicator = ctk.CTkLabel(self.left_frame, text="Balance:" + str(self.load_profile().get("balance", "")), font=("Arial", 24), text_color="#FF0000")
        self.balanceIndicator.pack(pady=(20, 10))

        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # ctk.CTkLabel(self.main_frame, text="Available Events", font=("Arial", 24)).pack(pady=10)
        self.errorLabel = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 24), text_color="#FF0000")
        self.errorLabel.pack(pady=10)

        for event in self.load_events():
            self.event_frame = ctk.CTkFrame(self.main_frame)
            self.event_frame.pack(pady=10, padx=20, fill="x")

            ctk.CTkLabel(self.event_frame, text=event["name"], font=("Arial", 18)).pack(side="left", padx=10)
            ctk.CTkLabel(self.event_frame, text=f"Location: {event['location']}", font=("Arial", 14)).pack(side="left",
                                                                                                           padx=10)
            ctk.CTkLabel(self.event_frame, text=f"Time: {event['time']}", font=("Arial", 14)).pack(side="left", padx=10)

            ctk.CTkLabel(self.event_frame, text=f"Ticket Price: {event['price']}", font=("Arial", 14)).pack(side="left", padx=10)

            ctk.CTkButton(self.event_frame, text="Purchase", command=lambda e=event: self.purchase_ticket(e)).pack(side="right",
                                                                                                                   padx=10)

    def showWindow(self):
        self.app.mainloop()


    def load_profile(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as file:
                return json.load(file)
        return {"name": "", "age": "", "email": "", "balance":0}

    def save_profile(self, data):
        with open(self.data_path, "w") as f:
            json.dump(data, f)


    def load_events(self):
        if os.path.exists(self.event_data_path):
            with open(self.event_data_path, "r") as f:
                return json.load(f)
        return []

    def load_tickets(self):
        if os.path.exists(self.tickets_file):
            with open(self.tickets_file, "r") as file:
                return json.load(file)
        return []

    def save_tickets(self, tickets):
        with open(self.tickets_file, "w") as f:
            json.dump(tickets, f, indent=4)

    def purchase_ticket(self, event):
        if int(self.load_profile().get("balance", "")) >= int(event["price"]):
            self.errorLabel.configure(text="")
            ticket_number = random.randint(1000, 9999)
            ticket = {
                "ticket_number": ticket_number,
                "event_name": event["name"],
                "location": event["location"],
                "time": event["time"]
            }
            tickets = self.load_tickets()
            tickets.append(ticket)
            self.save_tickets(tickets)
            self.show_purchased_tickets()

            new_data = {
                "name": self.load_profile().get("name"),
                "age": self.load_profile().get("age"),
                "email": self.load_profile().get("email"),
                "balance": (int(self.load_profile().get("balance", "")) - int(event["price"]))
            }

            self.save_profile(new_data)
            self.balanceIndicator.configure(text="Balance:" + str(self.load_profile().get("balance", "")))
        else:
            self.errorLabel.configure(text="Insufficient Funds")
            print("User doesn't have enough funds")


    def refund_ticket(self, ticket, parent_frame):
        tickets = self.load_tickets()
        updated = [t for t in tickets if t["ticket_number"] != ticket["ticket_number"]]
        self.save_tickets(updated)
        parent_frame.destroy()

    def show_purchased_tickets(self):
        top = ctk.CTkToplevel(self.app)
        top.geometry("400x500")
        top.title("Purchased Tickets")

        tickets = self.load_tickets()

        if not tickets:
            ctk.CTkLabel(top, text="No tickets purchased yet.").pack(pady=20)
        else:
            for ticket in tickets:
                ticket_frame = ctk.CTkFrame(top)
                ticket_frame.pack(pady=5, padx=10, fill="x")

                ticket_text = f"#{ticket['ticket_number']} - {ticket['event_name']}\n{ticket['location']} at {ticket['time']}"
                ctk.CTkLabel(ticket_frame, text=ticket_text, font=("Arial", 12)).pack(side="left", padx=10)

                ctk.CTkButton(ticket_frame, text="Refund", width=80, command=lambda t=ticket, f=ticket_frame: self.refund_ticket(t, f)).pack(side="right", padx=10)

    def open_profile_window(self):
        win = ctk.CTkToplevel(self.app)
        win.geometry("400x300")
        win.title("Profile")
        win.lift()
        win.focus_force()

        ctk.CTkLabel(win, text="Name:").pack(pady=(10, 0))
        name_entry = ctk.CTkEntry(win)
        name_entry.insert(0, self.load_profile().get("name", ""))
        name_entry.pack()

        ctk.CTkLabel(win, text="Age:").pack(pady=(10, 0))
        age_entry = ctk.CTkEntry(win)
        age_entry.insert(0, self.load_profile().get("age", ""))
        age_entry.pack()

        ctk.CTkLabel(win, text="Email:").pack(pady=(10, 0))
        email_entry = ctk.CTkEntry(win)
        email_entry.insert(0, self.load_profile().get("email", ""))
        email_entry.pack()

        ctk.CTkLabel(win, text="Balance:").pack(pady=(10, 0))
        balance_entry = ctk.CTkEntry(win)
        balance_entry.insert(0, self.load_profile().get("balance", ""))
        balance_entry.pack()

        def save_and_close():
            new_data = {
                "name": name_entry.get(),
                "age": age_entry.get(),
                "email": email_entry.get(),
                "balance": balance_entry.get()
            }
            self.save_profile(new_data)
            self.balanceIndicator.configure(text="Balance:" + str(self.load_profile().get("balance", "")))
            win.destroy()

        ctk.CTkButton(win, text="Save", command=save_and_close).pack(pady=20)





Profile()