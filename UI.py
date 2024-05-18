import tkinter as tk
from tkinter import ttk, messagebox
import imageio
from PIL import Image, ImageTk
import subprocess

class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.video_path = video_path
        self.video = imageio.get_reader(video_path)
        self.video_label = tk.Label(root)
        self.video_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_video()

    def update_video(self):
        try:
            frame = self.video.get_next_data()
            frame = Image.fromarray(frame)
            frame = frame.resize((self.root.winfo_width(), self.root.winfo_height()))
            frame = ImageTk.PhotoImage(frame)
            self.video_label.config(image=frame)
            self.video_label.image = frame
        except StopIteration:
            self.video.close()
            self.video = imageio.get_reader(self.video_path)
        
        self.root.after(50, self.update_video)  # Schedule the next update

def toggle_password_visibility(entry, show_password_var):
    if show_password_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def show_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    label = ttk.Label(login_window, text="Enter your username and password")
    label.pack(pady=10)

    username_label = ttk.Label(login_window, text="Username:")
    username_label.pack()

    username_entry = ttk.Entry(login_window)
    username_entry.pack()

    password_label = ttk.Label(login_window, text="Password:")
    password_label.pack()

    password_entry = ttk.Entry(login_window, show="*")
    password_entry.pack()

    show_password_var = tk.BooleanVar()
    show_password_checkbox = ttk.Checkbutton(login_window, text="Show Password", variable=show_password_var,
                                             command=lambda: toggle_password_visibility(password_entry, show_password_var))
    show_password_checkbox.pack()

    def login():
        username = username_entry.get()
        if username:  # Add your actual authentication logic here
            app.username = username
            app.update_user_info()
            login_window.destroy()
            print("Logged in")
        else:
            messagebox.showwarning("Login failed", "Please enter a username")

    login_button = ttk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=10)
def signup_user(file_path, username, user_pass):
    # Read the existing JSON data
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create a new structure
        data = {'users': []}

    # Check if the username already exists
    for user in data['users']:
        if user['username'] == username:
            print(f"Username '{username}' already exists. Choose a different username.")
            return

    # Create a new user entry
    new_user = {
        "username": username,
        "user_pass": user_pass,
        "quiz_score": 0,
        "ar_game_score": 0
    }

    # Add the new user to the list
    data['users'].append(new_user)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"User '{username}' successfully signed up.")

def show_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")

    label = ttk.Label(signup_window, text="Create a new account")
    label.pack(pady=10)

    username_label = ttk.Label(signup_window, text="Choose a username:")
    username_label.pack()

    username_entry = ttk.Entry(signup_window)
    username_entry.pack()

    password_label = ttk.Label(signup_window, text="Password:")
    password_label.pack()

    password_entry = ttk.Entry(signup_window, show="*")
    password_entry.pack()

    show_password_var = tk.BooleanVar()
    show_password_checkbox = ttk.Checkbutton(signup_window, text="Show Password", variable=show_password_var,
                                             command=lambda: toggle_password_visibility(password_entry, show_password_var))
    show_password_checkbox.pack()

    def signup():
        username = username_entry.get()
        password = password_entry.get()
        if username:  # Add your actual sign-up logic here
            app.username = username
            app.update_user_info()
            signup_window.destroy()
            signup_user(user_data,username, password)
            print(username, password)
        else:
            messagebox.showwarning("Sign-up failed", "Please enter a username")

    signup_button = ttk.Button(signup_window, text="Sign Up", command=signup)
    signup_button.pack(pady=10)

def open_quiz_window():
    subprocess.Popen(["python", "quiz.py"])
fact_index = None  # Define fact_index as a global variable

# def open_eco_nuggets_window():
#     subprocess.Popen(["python", "eco_nuggets.py"])

def open_ar_game():
    subprocess.Popen(["python", "ar_ui.py"])
def open_eco_nuggets():
    subprocess.Popen(["python", "sco_nugg.py"])
#fact_index = None  # Define fact_index as a global variable

import tkinter as tk
from tkinter import ttk, messagebox

class EcoSparkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoSpark")
        self.root.geometry("800x600")

        self.username = None

        # Define color theme for sustainability
        sustainability_bg = "#90ee90"  # Light green background
        sustainability_fg = "black"    # Black text

        # Create a frame for the video player
        video_frame = ttk.Frame(root)
        video_frame.place(x=0, y=0, relwidth=1, relheight=1)
        video_frame.grid_propagate(False)

        # Create the video player
        video_path = r"C:\Users\Impana J\OneDrive\Desktop\F1EcoSpark\dummy\assets\vid.mp4"
        self.video_player = VideoPlayer(video_frame, video_path)

        # Create a frame for the navigation bar
        navbar_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style="Navbar.TFrame")
        navbar_frame.pack(side=tk.TOP, fill=tk.X)

        # Create Login button
        login_button = ttk.Button(navbar_frame, text="Login", width=15, style='Navbar.TButton', command=show_login_window)
        login_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create Sign up button
        sign_up_button = ttk.Button(navbar_frame, text="Sign up", width=15, style='Navbar.TButton', command=show_signup_window)
        sign_up_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Define a custom style for the navigation bar frame and buttons
        style = ttk.Style()
        style.configure('Navbar.TFrame', background=sustainability_bg)
        style.configure('Navbar.TButton', foreground=sustainability_fg, font=('Arial', 12), borderwidth=0, relief=tk.RAISED, padding=10)
        style.map('Navbar.TButton', background=[('active', '#77dd77')])  # Change background color on button click

        # Define button labels for lessons, AR/MINI GAMES, and LEADERBOARD
        button_labels = ["ECO-QUIZ", "ECO-SCAN", "ECO NUGGETS"]


        # Create individual buttons for lessons, quiz, AR/MINI GAMES, and LEADERBOARD
        for label in button_labels:
            if label == "ECO-QUIZ":
                button = ttk.Button(root, text=label, width=20, style='Custom.TButton', command=open_quiz_window)
            elif label == "ECO-SCAN":
                button = ttk.Button(root, text=label, width=20, style='Custom.TButton', command=open_ar_game)
            elif label == "ECO NUGGETS":
                button = ttk.Button(root, text=label, width=20, style='Custom.TButton', command=open_eco_nuggets)
            else:
                button = ttk.Button(root, text=label, width=20, style='Custom.TButton')
            button.pack(side=tk.TOP, pady=10)


        # Create a frame for displaying user info
        self.user_info_frame = ttk.Frame(root, padding=(10, 10, 10, 10), style="UserInfo.TFrame")
        self.user_info_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.user_info_label = ttk.Label(self.user_info_frame, text="No user logged in.", style="UserInfo.TLabel")
        self.user_info_label.pack(pady=10)
        
        # Define a custom style for the user info frame and label
        style.configure('UserInfo.TFrame', background=sustainability_bg)
        style.configure('UserInfo.TLabel', foreground=sustainability_fg, font=('Arial', 12))
        
    def update_user_info(self):
        if self.username:
            self.user_info_label.config(text=f"User: {self.username}")
        else:
            self.user_info_label.config(text="No user logged in.")

# Create the main application
root = tk.Tk()
app = EcoSparkApp(root)

# Run the main loop
root.mainloop()
