import os
import random
from playsound3 import playsound
import tkinter as tk
from tkinter import messagebox

soundpath = "/Users/game/github/scrapyard/sound.mp3"

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fail Math And Get Nuked")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.score = 0
        self.total_questions = 0
        self.nuke = False
        
        # Create widgets
        self.create_widgets()
        
        # Start the first question
        self.new_question()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Fail Math And Get Nuked",
            font=("Arial", 20, "bold"),
        )
        title_label.pack(pady=10)
        
        # Question frame
        question_frame = tk.Frame(self.root)
        question_frame.pack(pady=10)
        
        self.question_label = tk.Label(
            question_frame,
            text="",
            font=("Arial", 16),
        )
        self.question_label.pack()
        
        # Answer frame
        answer_frame = tk.Frame(self.root)
        answer_frame.pack(pady=10)
        
        tk.Label(
            answer_frame,
            text="Your answer:",
            font=("Arial", 12),
        ).pack(side=tk.LEFT, padx=5)
        
        self.answer_entry = tk.Entry(answer_frame, font=("Arial", 12), width=10)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_entry.focus_set()
        
        # Submit button
        self.submit_btn = tk.Button(
            self.root,
            text="Submit",
            font=("Arial", 12),
            command=self.check_answer,
            width=10
        )
        self.submit_btn.pack(pady=10)
        
        # Bind Enter key to submit
        self.root.bind("<Return>", lambda event: self.check_answer())
        
        # Score label
        self.score_label = tk.Label(
            self.root,
            text="Score: 0",
            font=("Arial", 12),
        )
        self.score_label.pack(pady=10)
    
    def new_question(self):
        self.num1 = random.randint(0, 100)
        self.num2 = random.randint(0, 100)
        express = random.randint(1, 3)
        
        if express == 1:
            self.result = self.num1 + self.num2
            operation = "+"
        elif express == 2:
            self.result = self.num1 - self.num2
            operation = "-"
        elif express == 3:
            self.result = self.num1 * self.num2
            operation = "*"
        
        self.question_label.config(text=f"{self.num1} {operation} {self.num2} = ?")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus_set()
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            self.total_questions += 1
            
            if user_answer == self.result:
                self.score += 1

                messagebox.showinfo("Correct!", "Your answer is correct!")
            else:
                # messagebox.showerror("Incorrect!", f"Wrong answer! The correct answer is {self.result}. Shutting down your pc in 10 seconds cus you failed math. :hehe:")
                if self.nuke:
                    playsound(soundpath)
                    os.system("sudo shutdown -h now")
                else:
                    messagebox.showwarning("Incorrect!","Giving you a second chance before nuking your PC.")
                    self.nuke = True
            
            # Update score
            self.score_label.config(text=f"Score: {self.score}")
            
            # Next question
            self.new_question()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()