import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip


def shorten_url():
    long_url = entry.get()
    if not long_url.strip():
        messagebox.showwarning("Warning", "Please enter a URL")
        return

    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
        response.raise_for_status()
        short_url = response.text
        result_label.config(text=f"Shortened URL: {short_url}")
        copy_button.config(state=tk.NORMAL)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to shorten the URL: {e}")


def copy_to_clipboard():
    short_url = result_label.cget("text")[15:]  # Extract the URL from the label text
    if short_url:
        pyperclip.copy(short_url)
        messagebox.showinfo("Copy Success", "Shortened URL copied to clipboard!")
    else:
        messagebox.showerror("Error", "No shortened URL to copy.")


# Create the main application window
app = tk.Tk()
app.title("URL Shortener")

# Input Label and Entry
label = tk.Label(app, text="Enter the URL to shorten:")
label.pack(pady=10)

entry = tk.Entry(app, width=50)
entry.pack(pady=5)

# Shorten Button
shorten_button = tk.Button(app, text="Shorten", command=shorten_url)
shorten_button.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="", wraplength=400, fg="blue")
result_label.pack(pady=10)

# Copy Button
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

# Run the application
app.mainloop()
