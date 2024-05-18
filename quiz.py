import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import messagebox
import json

# Load quiz data from JSON file
with open("quiz_data.json", "r") as file:
    quiz_data = json.load(file)

# Create the main window
root = ttkb.Window(themename="flatly")  # Choose a theme from ttkbootstrap
root.title("Sustainability Quiz")
root.geometry("800x600")

# Create a header frame
header_frame = ttkb.Frame(root, bootstyle="primary")
header_frame.pack(fill="x")

# Header label
header_label = ttkb.Label(header_frame, text="Sustainability Quiz", font=("Arial", 24, "bold"), bootstyle="inverse-primary")
header_label.pack(pady=10)

# Create a frame for the question
question_frame = ttkb.Frame(root, padding=(20, 10))
question_frame.pack(pady=20)

# Question label
question_label = ttkb.Label(question_frame, text="", font=("Arial", 16), wraplength=600)
question_label.pack()

# Create a frame for the answer choices
answer_frame = ttkb.Frame(root, padding=(20, 10))
answer_frame.pack(pady=10)

# Create a frame for the fact
fact_frame = ttkb.Frame(root, padding=(20, 10))
fact_frame.pack(pady=10)

# Fact label
fact_label = ttkb.Label(fact_frame, text="", font=("Arial", 14), wraplength=600)
fact_label.pack()

# Create a frame for the buttons
button_frame = ttkb.Frame(root)
button_frame.pack(pady=20)

# Next button
next_button = ttkb.Button(button_frame, text="Next", width=10, bootstyle="success", command=lambda: load_next_question())
next_button.pack(side="left", padx=10)

# Submit button
submit_button = ttkb.Button(button_frame, text="Submit", width=10, bootstyle="primary", command=lambda: submit_answer())
submit_button.pack(side="left", padx=10)

# Create a frame for the score
score_frame = ttkb.Frame(root, padding=(20, 10))
score_frame.pack(pady=10)

# Score label
score_label = ttkb.Label(score_frame, text="Score: 0", font=("Arial", 14), bootstyle="secondary")
score_label.pack(side="left")

# Function to load the next question

score_path = "score.json"
def update_points(path, field, score):
    with open(path, 'r') as file:
        data = json.load(file)
    print(data)
    data[field] = score
    print(data)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_next_question():
    global current_question
    if current_question < len(quiz_data):
        question_label.config(text=quiz_data[current_question]["question"])
        for i, answer in enumerate(quiz_data[current_question]["answers"]):
            answer_buttons[i].config(text=answer)
        fact_label.config(text="")
    else:
        question_label.config(text="Quiz Completed!")
        update_points(score_path, "quiz_score", score)
        for button in answer_buttons:
            button.config(state="disabled")
        next_button.config(state="disabled")
        submit_button.config(state="disabled")


# Function to handle answer submission
def submit_answer():
    global current_question, score
    selected_answer = answer_var.get()
    if selected_answer == quiz_data[current_question]["correct_answer"]:
        score += 1
        fact_label.config(text=f"Fact: {quiz_data[current_question]['fact']}")
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        fact_label.config(text=f"Fact: {quiz_data[current_question]['fact']}")
        messagebox.showerror("Result", "Incorrect Answer. Try the next question!")
    score_label.config(text=f"Score: {score}")
    current_question += 1
    load_next_question()

# Create answer choice buttons dynamically
answer_var = tk.IntVar()
answer_buttons = []
for i in range(4):
    answer_button = ttkb.Radiobutton(answer_frame, text="", variable=answer_var, value=i, bootstyle="info")
    answer_button.pack(anchor='w')  # Align to the left
    answer_buttons.append(answer_button)

# Initialize variables
current_question = 0
score = 0

# Load the first question
load_next_question()

root.mainloop()