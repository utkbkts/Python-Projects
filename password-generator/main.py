from tkinter import *
from tkinter import messagebox
import random
import string

# ---------------- Password Generation ---------------- #
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------- Save Password ---------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}\n")

    messagebox.showinfo("Success", "Password saved successfully!")

    # Clear fields after saving
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------- UI Setup ---------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas (Logo)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=4)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=4)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=4)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, "Your Email address")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=4, sticky="ew", padx=5)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=20)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
