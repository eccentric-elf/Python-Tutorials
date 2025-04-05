import tkinter as tk
import math

def compute_sqrt():
    try:
        num = float(entry.get())
        result.set(f"√{num} = {math.sqrt(num):.2f}")
    except:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Square Root Calculator")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Compute √", command=compute_sqrt).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
