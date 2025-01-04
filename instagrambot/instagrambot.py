import instaloader
import tkinter as tk
from tkinter import messagebox


def download_post():
    username = username_entry.get()

    try:
        # Instaloader nesnesi oluştur
        bot = instaloader.Instaloader()

        # Profil nesnesi oluştur
        profile = instaloader.Profile.from_username(bot.context, username)

        posts = profile.get_posts()

        for index, post in enumerate(posts, 1):
            # Gönderiyi indir
            bot.download_post(post, target=f"{profile.username}_{index}")

        messagebox.showinfo("Download", "All posts downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Tkinter arayüzü
root = tk.Tk()
root.title("Instagram Downloader")
root.geometry("300x200")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, pady=20)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, pady=20)

download_button = tk.Button(root, text="Download Posts", command=download_post)
download_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
