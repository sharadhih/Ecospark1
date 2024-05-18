import tkinter as tk
from tkinter import ttk, messagebox

def show_next_fact():
    global fact_index, eco_nuggets_window, facts  # Declare all necessary global variables
    fact_index = (fact_index + 1) % len(facts)
    messagebox.showinfo("Eco Nugget", facts[fact_index])
    if fact_index == len(facts) - 1:
        eco_nuggets_window.destroy()

def open_eco_nuggets_window():
    global eco_nuggets_window, fact_index, facts  # Declare all necessary global variables

    eco_nuggets_window = tk.Toplevel(root)
    eco_nuggets_window.title("Eco Nuggets")
    eco_nuggets_window.geometry("300x200")

    facts = [
        "Fact 1: Recycling one aluminum can saves enough energy to run a TV for three hours.",
        "Fact 2: The energy saved from recycling one glass bottle can run a 100-watt light bulb for four hours.",
        "Fact 3: Recycling paper saves around 15 trees per ton of paper recycled.",
        "Fact 4: Plastic bags and other plastic garbage thrown into the ocean kill as many as 1 million sea creatures every year.",
        "Fact 5: On average, it takes 450 years for a plastic bottle to completely degrade.",
        # Add more facts as needed
    ]

    fact_index = 0  # Initialize fact_index to 0

    show_next_fact()

    next_button = ttk.Button(eco_nuggets_window, text="OK", command=show_next_fact)
    next_button.pack(pady=5)

if __name__ == "__main__":
    # Create the main application
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("400x300")

    # Button to open Eco Nuggets window
    eco_nuggets_button = ttk.Button(root, text="Open Eco Nuggets", command=open_eco_nuggets_window)
    eco_nuggets_button.pack(pady=10)

    root.mainloop()
