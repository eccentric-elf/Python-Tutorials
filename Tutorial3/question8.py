import tkinter as tk
import random


target_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < target_number:
            result.set("Too small, try again!")
        elif guess > target_number:
            result.set("Too large, try again!")
        else:
            result.set(f"Congratulations! You guessed it in {attempts} attempts.")
            entry.config(state="disabled")  
    except ValueError:
        result.set("Invalid input! Enter a number.")

root = tk.Tk()
root.title("Guess the Number")

tk.Label(root, text="Guess a number (1-100):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit Guess", command=check_guess).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()


root.mainloop()
