import tkinter as tk

def to_uppercase():
    result.set(entry.get().upper())

root = tk.Tk()
root.title("Uppercase Converter")

tk.Label(root, text="Enter text:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=to_uppercase).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
