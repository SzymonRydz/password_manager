import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password = []
    password.extend(chr(random.randint(97, 122)) for _ in range(random.randint(6, 8)))
    password.extend(chr(random.randint(65, 90)) for _ in range(random.randint(4, 8)))
    password.extend(chr(random.randint(48, 57)) for _ in range(random.randint(4, 8)))
    password.extend(chr(random.randint(33, 38)) for _ in range(random.randint(4, 8)))
    random.shuffle(password)

    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def append_to_file():

    if website_entry.get() == "":
        messagebox.showwarning(title="Error!", message="Your website entry is empty!")
        website_entry.focus()
    elif username_entry.get() == "":
        messagebox.showwarning(title="Error!", message="Your username entry is empty!")
        username_entry.focus()
    elif password_entry.get() == "":
        messagebox.showwarning(title="Error!", message="Your password entry is empty!")
        password_entry.focus()
    else:
        is_ok = messagebox.askyesno(title=website_entry.get(), message=f"Save that data to file?\n"
                                                                    f"username: {username_entry.get()}\n"
                                                                    f"password: {password_entry.get()}\n")
        if is_ok:
            new_data = {
                website_entry.get() : {
                    "email": username_entry.get(),
                    "password": password_entry.get()
                }
            }
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "r") as file:
                    data=json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, 'end')
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                website_entry.focus()

def search_button():
    if website_entry.get() == "":
        messagebox.showwarning(title="Error!", message="Your website entry is empty!")
        website_entry.focus()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website_entry.get() in data:
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]
                messagebox.showinfo(title="Data", message=f"Email: {email}\n"
                                                          f"Password: {password}")
            else:
                messagebox.showinfo(title="Error", message="Not found a data")
    except FileNotFoundError:
        messagebox.showwarning(title="Error!", message="Not Found a File!")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website")
website_label.grid(column=0,row=1)

website_entry = tk.Entry(width=17)
website_entry.grid(column=1,row=1)
website_entry.focus()

website_button = tk.Button(text="Search", width=15, command=search_button)
website_button.grid(column=2, row=1)

username_label = tk.Label(text="Email/Username")
username_label.grid(column=0,row=2)

username_entry = tk.Entry(width=35)
username_entry.grid(column=1,row=2, columnspan=2)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=17)
password_entry.grid(column=1, row=3, padx=0)

generate_password_button = tk.Button(text="Generate password", padx=0, command=generate_password)
generate_password_button.grid(column=2, row=3, padx=0)

add_button = tk.Button(text="Add", width=30, command=append_to_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()