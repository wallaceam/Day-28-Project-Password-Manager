from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BLACK = "#000000"
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = website_entry.get()
    user = user_entry.get()
    pw = pass_entry.get()
    new_data = {
        website: {
            "username": user,
            "password": pw
        }
    }

    if website == "" or user == "" or pw == "":
        messagebox.showerror(title="Empty Field", message="All fields must contain an entry to save.")
        return
    else:
        try:
            with open("data.json", mode="r") as record:
                json.load(record)
        except FileNotFoundError:
            with open("data.json", mode="w") as record:
                json.dump(new_data, record, indent=4)
        else:
            with open("data.json", mode="r") as record:
                data = json.load(record)
                data.update(new_data)
            with open("data.json", mode="w") as record:
                json.dump(data, record, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def get_pw():
    website = website_entry.get()
    try:
        with open("data.json") as record:
            data = json.load(record)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if website in data:
            username = data[website]["username"]
            pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {pw}")
        else:
            messagebox.showerror("Not Found", f"There is no saved data for {website}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(bg=WHITE, fg=BLACK, text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(bg=WHITE, fg=BLACK, highlightbackground=WHITE, insertbackground=BLACK)
website_entry.config(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_search = Button(bg=WHITE, fg=BLACK, text="Search", highlightbackground=WHITE, command=get_pw, width=13)
website_search.grid(row=1, column=2)

# Email/Username
user_label = Label(bg=WHITE, fg=BLACK, text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = Entry(bg=WHITE, fg=BLACK, highlightbackground=WHITE, insertbackground=BLACK)
user_entry.config(width=38)
user_entry.insert(0, "example@email.com")
user_entry.grid(row=2, column=1, columnspan=2)

# Password
pass_label = Label(bg=WHITE, fg=BLACK, text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(bg=WHITE, fg=BLACK, highlightbackground=WHITE, insertbackground=BLACK)
pass_entry.config(width=21)
pass_entry.grid(row=3, column=1)

pass_gen_button = Button(bg=WHITE, fg=BLACK, text="Generate Password", highlightbackground=WHITE, command=generate_pw)
pass_gen_button.grid(row=3, column=2)

# Add
add_button = Button(bg=WHITE, fg=BLACK, text="Add", highlightbackground=WHITE, width=36, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
