import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = float(entry.get())
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        result.set(f"{math.sqrt(num):.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid non-negative number.")
        entry.delete(0, tk.END)


root = tk.Tk()
root.title("Square Root Calculator")
tk.Label(root, text="Enter number:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Button(root, text="Compute √", command=compute_sqrt).grid(row=1, column=0, columnspan=2)

result = tk.StringVar()
tk.Label(root, text="Square Root:").grid(row=2, column=0)
tk.Entry(root, textvariable=result, state="readonly").grid(row=2, column=1)
root.mainloop()
