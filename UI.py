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

class Quiz:
    def __init__(self, root):
        self.root = root
        self.questions = [
            ("Which of the following actions helps reduce energy consumption at home?",
             ["A) Leaving lights on all day", "B) Turning off lights when not in use", "C) Using incandescent bulbs", "D) Keeping electronics plugged in"], 
             1, "mcq", 
             "Fact: Turning off lights when they're not needed can save a significant amount of energy and reduce electricity bills."),
            
            ("What should you do with an empty glass bottle?",
             ["A) Throw it in the trash", "B) Recycle it", "C) Burn it", "D) Bury it"], 
             1, "mcq", 
             "Fact: Recycling glass saves raw materials and reduces energy consumption compared to producing new glass from raw materials."),
            
            ("What is the benefit of using a reusable water bottle instead of disposable plastic bottles?",
             ["A) It's heavier", "B) It's cheaper in the long run", "C) It's more fashionable", "D) It's easier to lose"], 
             1, "mcq", 
             "Fact: Using a reusable water bottle reduces plastic waste and can save money over time compared to buying disposable bottles."),
            
            ("Which type of energy is considered renewable?",
             ["A) Coal", "B) Oil", "C) Wind", "D) Natural Gas"], 
             2, "mcq", 
             "Fact: Wind energy is renewable because it uses wind to generate electricity without depleting natural resources."),
            
            ("How can you conserve water while taking a shower?",
             ["A) Taking shorter showers", "B) Using a high-flow showerhead", "C) Leaving the water running when not needed", "D) Taking multiple showers a day"], 
             0, "mcq", 
             "Fact: Shorter showers save water and energy used to heat the water, reducing your environmental footprint."),
            
            ("Recycling helps reduce the need for new raw materials.",
             ["True", "False"], 
             0, "tf", 
             "Fact: Recycling materials like paper, glass, and metals reduces the need to extract and process raw materials, saving energy and reducing pollution."),
            
            ("Using public transportation instead of driving alone can lower your carbon footprint.",
             ["True", "False"], 
             0, "tf", 
             "Fact: Public transportation is more efficient and produces fewer emissions per person compared to individual car use."),
            
            ("Turning off your computer when it's not in use saves energy.",
             ["True", "False"], 
             0, "tf", 
             "Fact: Turning off or putting your computer to sleep when not in use can significantly reduce its energy consumption."),
            
            ("Composting food scraps can reduce the amount of waste sent to landfills.",
             ["True", "False"], 
             0, "tf", 
             "Fact: Composting converts food scraps into valuable organic matter that can enrich soil, reducing landfill waste and methane emissions."),
            
            ("LED bulbs use more energy than traditional incandescent bulbs.",
             ["True", "False"], 
             1, "tf", 
             "Fact: LED bulbs use up to 80% less energy than incandescent bulbs and last much longer, making them a more sustainable choice.")
        ]
        self.current_question = 0
        self.score = 0

        self.quiz_window = tk.Toplevel(root)
        self.quiz_window.title("Quiz")
        self.quiz_window.geometry("600x500")

        self.question_label = ttk.Label(self.quiz_window, wraplength=400)
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()

        self.options_frame = ttk.Frame(self.quiz_window)
        self.options_frame.pack(pady=10)

        self.options = [ttk.Radiobutton(self.options_frame, variable=self.var, value=i) for i in range(4)]
        for option in self.options:
            option.pack(anchor="w")

        self.nav_frame = ttk.Frame(self.quiz_window)
        self.nav_frame.pack(pady=20)

        self.prev_button = ttk.Button(self.nav_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = ttk.Button(self.nav_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=10)

        self.update_question()

    def update_question(self):
        question, options, correct_answer, qtype, fact = self.questions[self.current_question]
        self.question_label.config(text=question + "\n\n" + fact)
        for i, option in enumerate(options):
            self.options[i].config(text=option, value=i)
            self.options[i].pack(anchor="w")
        self.var.set(-1)
        if qtype == "tf":
            for i in range(2, 4):
                self.options[i].pack_forget()
        else:
            for i in range(2, 4):
                self.options[i].pack(anchor="w")

    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.update_question()

    def next_question(self):
        if self.var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer")
            # Return to quiz window without incrementing current_question
            self.quiz_window.lift()
            return
            
        else:
            question, options, correct_answer, qtype, fact = self.questions[self.current_question]
            if self.var.get() == correct_answer:
                self.score += 1
            if self.current_question < len(self.questions) - 1:
                self.current_question += 1
                self.update_question()
            else:
                messagebox.showinfo("Quiz Completed", f"Congratulations! Your score is {self.score}/{len(self.questions)}")
                self.quiz_window.destroy()

def show_quiz_window():
    Quiz(root)

# Create the main window
root = tk.Tk()
root.title("EcoSpark")
root.geometry("800x600")

# Define color theme for sustainability
sustainability_bg = "#90ee90"  # Light green background
sustainability_fg = "black"    # Black text

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
    if label == "QUIZ":
        button = ttk.Button(root, text=label, width=20, style='Custom.TButton', command=show_quiz_window)
    else:
        button = ttk.Button(root, text=label, width=20, style='Custom.TButton')
    button.pack(side=tk.TOP, pady=10)

# Run the main loop
root.mainloop()
