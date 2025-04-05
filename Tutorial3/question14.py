import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = float(entry.get())
        if num < 0:
            raise ValueError("Negative number")
        result.set(f"√{num} = {math.sqrt(num):.2f}")
    except:
        messagebox.showerror("Error", "Enter a valid non-negative number.")

root = tk.Tk()
root.title("Square Root Calculator")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Compute √", command=compute_sqrt).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
