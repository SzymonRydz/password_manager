import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.pack()


window.mainloop()