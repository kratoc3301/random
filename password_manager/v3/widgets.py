import tkinter
from random import choice, randint, shuffle
from tkinter import messagebox

import customtkinter as ctk
import pyperclip
import json


class Labels(ctk.CTkFrame):
    """
    Create a frame with Labels Entries and Buttons with their functions
    """

    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="equal")
        # Title
        self.title = ctk.CTkLabel(self, text="Password Manager",
                                  font=("Arial", 25, "bold"),
                                  fg_color="transparent")
        self.title.grid(row=0, column=1, sticky="nsew")
        # -------------------- LABELS --------------------
        # Website label
        self.website_label = ctk.CTkLabel(self, text="Website:",
                                          font=("Arial", 15, "bold"),
                                          fg_color="transparent", anchor="e")
        self.website_label.grid(row=1, column=0, padx=10, pady=10, sticky="e",
                                ipady=5, ipadx=5)

        # Email/Username label
        self.email_username_label = ctk.CTkLabel(self, text="Email/Username:",
                                                 font=("Arial", 15, "bold"),
                                                 fg_color="transparent", anchor="e")
        self.email_username_label.grid(row=2, column=0, padx=10, pady=10, sticky="e",
                                       ipady=5, ipadx=5)

        # Password label
        self.password_label = ctk.CTkLabel(self, text="Password:",
                                           font=("Arial", 15, "bold"),
                                           fg_color="transparent", anchor="e")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e",
                                 ipady=5, ipadx=5)

        # -------------------- ENTRIES --------------------
        # ---------- Search entry ---------- |
        # self.website_entry = tkinter.StringVar()
        self.website_entry = ctk.CTkEntry(self, fg_color="transparent", justify="center", width=200)  # textvariable=self.website_entry
        self.website_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.website_entry.focus()

        # ---------- Generate Password entry ---------- |
        # self.email_entry = tkinter.StringVar()
        self.email_entry = ctk.CTkEntry(self, fg_color="transparent", justify="center", width=200)  # textvariable=self.website_entry
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.email_entry.insert(0, "karlis.panagiotis@gmail.com")

        # ---------- Add entry ---------- |
        # self.password_entry = tkinter.StringVar()
        self.password_entry = ctk.CTkEntry(self, fg_color="transparent", justify="center", width=200)  # textvariable=self.website_entry
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # -------------------- BUTTONS --------------------
        # Search button
        self.search_button = ctk.CTkButton(self, text="Search", command=lambda: self.search_password())
        self.search_button.grid(row=1, column=2, padx=10, pady=10, sticky="w", )

        # Generate Password button
        self.generator_button = ctk.CTkButton(self, text="Generate Password", command=self.password_generator)
        self.generator_button.grid(row=3, column=2, padx=10, pady=10, sticky="w", )

        # Add button
        self.add_button = ctk.CTkButton(self, text="Save", command=lambda: self.save_as()
                                        )
        self.add_button.grid(row=4, padx=10, pady=10, columnspan=3, sticky="ew")

    # Button functions
    def search_password(self) -> None:
        name = self.website_entry.get().strip()
        website = name.lower()

        data = self.opener()

        if not data:
            messagebox.showerror("Error 404", "File not found or empty")
            return

        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            pyperclip.copy(password)
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", print(data))

    def password_generator(self) -> None:
        self.password_entry.delete(0, tkinter.END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letter = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(4, 6))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        password_list = password_letter + password_numbers + password_symbols
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save_as(self) -> None:
        website = self.website_entry.get().title().lower()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if website == '' or email == '' or password == '':
            messagebox.showerror("Error", "Please fill all fields")
        else:
            try:
                with open("password.json", "r") as passwords:
                    data = json.load(passwords)
            except (FileNotFoundError, json.JSONDecodeError):
                if messagebox.askyesno(title=".json not found",
                                       message="Create a new .json file?",
                                       default="yes"):
                    self.json_write(new_data)
                else:
                    pass
            else:
                # Updating old data with mew data
                data.update(new_data)
                self.json_write(data)
            finally:
                self.website_entry.delete(0, tkinter.END)
                self.password_entry.delete(0, tkinter.END)

    @staticmethod
    def opener() -> dict:
        try:
            with open("password.json", "r") as passwords:
                return json.load(passwords)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def json_write(data: object) -> None:
        with open("password.json", "w") as passwords:
            json.dump(data, passwords, indent=4)