from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if website == "" or user == "" or pw == "":
        messagebox.showerror(title="Empty Field", message="All fields must contain an entry to save.")
        return
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Save this data?\nWebsite: {website}\nUsername: {user}\nPassword: {pw}")
        if is_ok:
            with open("data.txt", mode="a") as record:
                record.write(f"{website} | {user} | {pw}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


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
website_entry.config(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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
