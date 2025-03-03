from tkinter import *

# Pencereyi oluştur
window = Tk()
window.title("Miles to Kilometer Converter")
window.geometry("400x250")
window.config(padx=20, pady=20, bg="#f7f5dd")  # Arka plan rengi ve padding


# Giriş Kutusu (Miles)
miles_input = Entry(width=10, font=("Arial", 14))
miles_input.grid(column=1, row=0, padx=10, pady=10)

# "Miles" etiketi
miles_label = Label(text="Miles", font=("Arial", 14), bg="#f7f5dd")
miles_label.grid(column=2, row=0, padx=10, pady=10)

# "is equal to" etiketi
is_equal_label = Label(text="is equal to", font=("Arial", 14), bg="#f7f5dd")
is_equal_label.grid(column=0, row=1, padx=10, pady=10)

# Sonuç etiketi (Kilometre sonucu)
kilometer_result_label = Label(text="0", font=("Arial", 14, "bold"), bg="#f7f5dd", fg="blue")
kilometer_result_label.grid(column=1, row=1, padx=10, pady=10)

# "Km" etiketi
kilometer_label = Label(text="Km", font=("Arial", 14), bg="#f7f5dd")
kilometer_label.grid(column=2, row=1, padx=10, pady=10)




def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=km)

    # Hesapla Butonu
calculate_button = Button(text="Calculate", font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5,command=miles_to_km)
calculate_button.grid(column=1, row=2, pady=20)
# Pencereyi aç
window.mainloop()
