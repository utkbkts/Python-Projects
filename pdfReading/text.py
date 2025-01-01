import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog


def pdf_to_speech(pdf_walls):
   text = ""
   pdf_read = PyPDF2.PdfReader(open(pdf_walls,"rb"))
   for i in range(len(pdf_read.pages)):
      text += pdf_read.pages[i].extract_text()
   return text

def text_to_speech(text, output_file):
   speech = gTTS(text=text, lang="tr")
   speech.save(output_file)

def convert_pdf():
   pdf_walls = filedialog.askopenfilename(initialdir="/", title="Select a PDF", filetypes=(("PDF files", "*.pdf"),))
   text = pdf_to_speech(pdf_walls)
   output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=(("MP3 files", "*.mp3"),))
   text_to_speech(text, output_file)


app = tk.Tk()
app.title("Speech Book App")
app.geometry("250x150")
label = tk.Label(app, text="PDF to Speech Book", font=("Arial", 24, "bold"))

button = tk.Button(app, text="Convert PDF", font=("Arial", 12), command=convert_pdf)
button.pack(pady=20)

app.mainloop()