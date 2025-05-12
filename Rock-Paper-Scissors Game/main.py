import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    computer_label.config(text=f"Computer: {computer_choice}")

    if choice == computer_choice:
        result.set("It's a draw!")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result.set("You win!")
    else:
        result.set("You lose!")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")

result = tk.StringVar()
result.set("Choose Rock, Paper or Scissors")

computer_label = tk.Label(root, text="Computer?", font=("Arial", 14))
computer_label.pack()

result_label = tk.Label(root, textvariable=result, font=("Arial", 14))
result_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(buttons_frame, text=choice, command=lambda c=choice: play(c),
              width=10, height=2).pack(side=tk.LEFT, padx=5)

root.mainloop()
