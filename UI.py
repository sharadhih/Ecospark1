import tkinter as tk
from tkinter import ttk, messagebox
import imageio
from PIL import Image, ImageTk

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

    # Example login widgets
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

    login_button = ttk.Button(login_window, text="Login", command=lambda: print("Logged in"))
    login_button.pack(pady=10)

def show_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")

    # Example sign up widgets
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

    signup_button = ttk.Button(signup_window, text="Sign Up", command=lambda: print("Signed up"))
    signup_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("EcoSpark")
root.geometry("800x600")

# Define color theme for sustainability
sustainability_bg = "#90ee90"  # Light green background
sustainability_fg = "black"     # Black text

# Create a frame for the video player
video_frame = ttk.Frame(root)
video_frame.place(x=0, y=0, relwidth=1, relheight=1)
video_frame.grid_propagate(False)

# Create the video player
video_path = r"C:\Users\acer\OneDrive\Desktop\Bnmit\Projects\Hackaventus\UI\vid.mp4"
video_player = VideoPlayer(video_frame, video_path)

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

# Define button labels for lessons, quiz, etc.
button_labels = ["LESSONS", "QUIZ", "AR/MINI GAMES", "LEADERBOARD"]

# Create individual buttons for lessons, quiz, etc.
for label in button_labels:
    button = ttk.Button(root, text=label, width=20, style='Custom.TButton')
    button.pack(side=tk.TOP, pady=10)

# Run the main loop
root.mainloop()
