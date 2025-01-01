from tkinter import Label,Tk
import time

app_windows = Tk()

# Design create
app_windows.title("Digital Time")
app_windows.geometry("750x300")
app_windows.resizable(0,0)
app_windows.configure(bg="#4C585B")

# label create
text_font = ("Boulder",36,'bold')
background = "black"
foreground =  "white"
border_width = 20

#time tags
label = Label(app_windows,font=text_font,bg=background,fg=foreground)
label.grid(row = 0,column=1,padx=border_width,pady=border_width)

#date tags
date_label = Label(app_windows,font=text_font,bg=background,fg=foreground)
date_label.grid(row=1,column=1,padx=border_width,pady=border_width)

def digital_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    label.config(text=current_time)
    date_label.config(text=current_date)
    app_windows.after(1000, digital_clock)

digital_clock()

app_windows.mainloop()