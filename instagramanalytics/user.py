import instaloader
import tkinter as tk
from tkinter import ttk, messagebox


# User information retrieval function
def get_user_info(username):
    try:
        bot = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(bot.context, username)

        # Create a dictionary
        user_info = {
            'username': profile.username,
            'biography': profile.biography,
            'profile_picture': profile.profile_pic_url,
            'follower_count': profile.followers,
            'following_count': profile.followees,
            'posts_count': profile.mediacount,
            'Last_Post_date': get_last_post_date(profile)
        }

        return user_info
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None


def get_last_post_date(profile):
    try:
        last_post = None

        for post in profile.get_posts():
            if last_post is None or post.date > last_post.date:
                last_post = post
        return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S") if last_post else "No posts"
    except Exception as e:
        return "Error fetching last post date"


def show_user():
    try:
        username = username_entry.get()
        if not username:
            messagebox.showwarning("Warning", "Please enter a username")
            return

        user_info = get_user_info(username)
        if isinstance(user_info, dict):
            # Clear the treeview
            for widget in tree.get_children():
                tree.delete(widget)

            # Insert user info into the treeview
            tree.insert("", "end", values=(
                user_info["username"],
                user_info["biography"],
                user_info["profile_picture"],
                user_info["follower_count"],
                user_info["following_count"],
                user_info["posts_count"],
                user_info["Last_Post_date"],
            ))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Tkinter frontend
root = tk.Tk()
root.title("Instagram User Information Viewer")
root.geometry("800x400")

# Username label and entry
username_label = tk.Label(root, text="Enter Instagram Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root, width=40)
username_entry.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Fetch User Info", command=show_user)
fetch_button.pack(pady=10)

# Treeview for displaying user info
columns = ("username", "biography", "profile_picture", "follower_count", "following_count", "posts_count", "Last_Post_date")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(pady=10, fill="both", expand=True)

# Define column headings
tree.heading("username", text="Username")
tree.heading("biography", text="Biography")
tree.heading("profile_picture", text="Profile Picture URL")
tree.heading("follower_count", text="Followers")
tree.heading("following_count", text="Following")
tree.heading("posts_count", text="Posts")
tree.heading("Last_Post_date", text="Last Post Date")

tree.column("username", width=100)
tree.column("biography", width=200)
tree.column("profile_picture", width=150)
tree.column("follower_count", width=100)
tree.column("following_count", width=100)
tree.column("posts_count", width=80)
tree.column("Last_Post_date", width=150)

# Run the application
root.mainloop()
