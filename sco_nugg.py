import tkinter as tk
import json
import random

class FactDisplayApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Fact Display")
        self.master.geometry("400x200")

        # Load facts from JSON file
        with open("eco_facts.json", "r") as file:
            self.facts = json.load(file)

        # Create fact label
        self.fact_label = tk.Label(master, text="", wraplength=380)
        self.fact_label.pack(pady=20)

        # Display initial random fact
        self.display_random_fact()

        # Create back button
        self.back_button = tk.Button(master, text="Back", command=self.close_window)
        self.back_button.pack()

    def display_random_fact(self):
        # Get a random fact from the list
        random_fact = random.choice(self.facts)
        # Update the fact label
        self.fact_label.config(text=random_fact)

    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = FactDisplayApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
