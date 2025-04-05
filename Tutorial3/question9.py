import tkinter as tk
import random

low, high = 1, 100
computer_guess = random.randint(low, high)
attempts = 0

def too_small():
    global low, computer_guess, attempts
    low = computer_guess + 1
    computer_guess = random.randint(low, high)
    update_label()

def too_large():
    global high, computer_guess, attempts
    high = computer_guess - 1
    computer_guess = random.randint(low, high)
    update_label()

def correct_guess():
    result.set(f"Computer guessed it in {attempts} attempts!")
    disable_buttons()

def update_label():
    global attempts
    attempts += 1
    result.set(f"Is it {computer_guess}?")

def disable_buttons():
    btn_small.config(state="disabled")
    btn_large.config(state="disabled")
    btn_correct.config(state="disabled")

root = tk.Tk()
root.title("Computer Guesses the Number")
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()
btn_small = tk.Button(root, text="Too Small", command=too_small)
btn_small.pack()
btn_large = tk.Button(root, text="Too Large", command=too_large)
btn_large.pack()
btn_correct = tk.Button(root, text="Correct!", command=correct_guess)
btn_correct.pack()

update_label()
root.mainloop()
