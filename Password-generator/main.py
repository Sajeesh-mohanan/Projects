from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LETTERS = 'a A b B c C d D e E f F g G h H i I j J k K l M n N o O p Q r R s S t T u U v V w W x X y Y z Z'.split()

NUMBERS = '1 2 3 4 5 6 7 8 9 0'.split()

SYMBOLS = '! @ # $ % ^ & * ( ) _ +'.split()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global LETTERS
    global NUMBERS
    global SYMBOLS
    flag = 0
    while flag != 1:
        password = ''
        password_list = [random.choice(LETTERS) for i in range(random.randint(5, 9))]

        password_list += [random.choice(NUMBERS) for i in range(random.randint(2, 4))]

        password_list += [random.choice(SYMBOLS) for i in range(random.randint(1, 3))]

        random.shuffle(password_list)

        for i in password_list:
            password += i
            if i.isupper():
                flag = 1

    psw_entry.delete(0, END)
    psw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().upper()
    email = email_entry.get()
    password = psw_entry.get()

    new_dict = {
                website: {
                    "email": email,
                    "password": password
                }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="Please don't leave empty fields")

    else:
        try:
            with open("data.json", "r") as json_data:
                data = json.load(json_data)
                data.update(new_dict)
        except FileNotFoundError:
            with open("data.json", "w") as json_data:
                json.dump(new_dict, json_data, indent=4)
        else:
            with open("data.json", "w") as json_data:
                json.dump(data, json_data, indent=4)

        website_entry.delete(0, END)
        psw_entry.delete(0, END)


# ---------------------------search website----------------------------#
def search_website():
    website = website_entry.get().upper()
    if website == "":
        messagebox.showerror(title="Error", message="Please don't leave empty fields")
    else:

        try:
            with open("data.json", "r") as json_data:
                data_dict = json.load(json_data)

        except FileNotFoundError:
            messagebox.showerror(title="Data file not found", message="No data found, please enter data in data.json file.")

        else:
            if website in data_dict:
                email = data_dict[website]["email"]
                password = data_dict[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

            else:
                messagebox.showerror(title=f"{website} Not found", message=f"Email and password not found for \"{website}\" ")


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.config(pady=50, padx=50)
window.title("MyPassword Manager")

img = PhotoImage(file="logo.png")   # -----image file------#

# Canvas
canvas = Canvas(height=200, width=200)
canvas.create_image(110, 100, image=img) # ----Image Canvas-----#
canvas.grid(row=0, column=1)

# Website Entry
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Search Button
sch_btn = Button(text="Search", width=14, command=search_website)
sch_btn.grid(row=1, column=2)

# Email label
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0, "sajeesh.mohan29@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password Label
psw_label = Label(text="Password: ")
psw_label.grid(row=3, column=0)
psw_entry = Entry(width=33)
psw_entry.grid(row=3, column=1)


# Generate password button
gen_pass_btn = Button(text="Generate Password", width=14, command=generate_password)
gen_pass_btn.grid(row=3, column=2)

# Add Button
add_btn = Button(text="Add", width=44, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

Tk.mainloop(window)
