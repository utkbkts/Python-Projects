import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode


def create_qr_code():
    url = url_entry.get()

    if url:
        try:
            qr_code = pyqrcode.create(url)
            file_path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg")])

            if file_path:
                qr_code.svg(file_path, scale=8)
                status_label.config(text="QR code saved successfully!")
            else:
                status_label.config(text="No file selected. Try again.")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")
    else:
        status_label.config(text="Please enter a URL.")


# Setup the application window
app_window = tk.Tk()
app_window.title("QR Code Generator")

# Create and arrange widgets
url_label = tk.Label(app_window, text="Enter URL:")
url_entry = tk.Entry(app_window, width=40)
generate_qr_button = tk.Button(app_window, text="Generate QR Code", command=create_qr_code)
status_label = tk.Label(app_window, text="")

# Layout using grid system
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry.grid(row=0, column=1, padx=10, pady=10)
generate_qr_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
app_window.mainloop()
