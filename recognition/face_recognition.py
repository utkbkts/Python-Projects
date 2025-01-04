import cv2
import tkinter as tk
from tkinter import filedialog
from PIL  import Image, ImageTk



def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))


        for (x, y, w, h) in faces:
          cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
          cv2.putText(img, "HUMAN", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 4.5, (255, 0, 0), 12)


        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((600,400), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        canvas.img = img
        canvas.create_image(0,0, anchor = tk.NW, image=img)


face_cascade = cv2.CascadeClassifier("C:/Users/Casper/Desktop/python/recognition/face_detector.xml")



#arayüz
root = tk.Tk()
root.title("Face Detector")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

open_button = tk.Button(root, text="File Choose", command=open_file)
open_button.pack()




root.mainloop()