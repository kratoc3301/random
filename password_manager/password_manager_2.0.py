#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
BG = "#EEEDEB"
FG = "#B43F3F"
BGB = "#F7E7DC"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def json_read():
    with open("/***/***/***/***", "r") as passwords:
        return json.load(passwords)


def json_write(data):
    with open("/***/***/***/***", "w") as passwords:
        json.dump(data, passwords, indent=4)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
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
            data = json_read()
        except FileNotFoundError:
            if messagebox.askyesno(title=".json not found", message="Create a new .json file?", default="yes"):
                json_write(new_data)
            else:
                pass
        else:
            # Updating old data with mew data
            data.update(new_data)
            json_write(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    name = website_entry.get()
    website = name.title()
    try:
        json_read()
    except FileNotFoundError:
        messagebox.showerror("Error 404", "File not found")
    else:
        if website in json_read():
            pyperclip.copy(json_read()[website]['password'])
            messagebox.showinfo(title=f"{website}", message=f"Email: {json_read()[website]['email']}\n"
                                                            f"Password: {json_read()[website]['password']}")
        else:
            messagebox.showerror("Error", "No details for the website exists")
            print(json_read().get(website))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
logo_img = PhotoImage(file="/***/***/***/***")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ______________________________ Labels ______________________________ #
website_label = Label(text="Website:",
                      bg=BG,
                      fg=FG,
                      font=("Arial", 15, "bold"),
                      highlightthickness=0
                      )
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:",
                             bg=BG,
                             fg=FG,
                             font=("Arial", 15, "bold"),
                             highlightthickness=0
                             )
email_username_label.grid(column=0, row=2, )
password_label = Label(text="Password:",
                       bg=BG,
                       fg=FG,
                       font=("Arial", 15, "bold"),
                       highlightthickness=0
                       )
password_label.grid(column=0, row=3)

# ______________________________ Entries ______________________________ #
website_entry = StringVar()
website_entry = Entry(width=25, textvariable=website_entry)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = StringVar()
email_entry = Entry(width=43, textvariable=email_entry)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "************")

password_entry = StringVar()
password_entry = Entry(width=25, textvariable=password_entry)
password_entry.grid(column=1, row=3)

# ______________________________ Buttons ______________________________ #
search_button = Button(text="Search", command=find_password,
                       bg=BGB, fg=FG,
                       highlightthickness=0,
                       cursor="hand2", width=13,
                       )
search_button.grid(column=2, row=1)
generator_button = Button(text="Generate Password", command=password_generator,
                          bg=BGB, fg=FG,
                          highlightthickness=0,
                          cursor="hand2", width=13,
                          )
generator_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save,
                    bg=BGB, fg=FG,
                    highlightthickness=0,
                    cursor="hand2",
                    height=1, width=40,
                    )
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
