import tkinter as tk

def convert_to_upper():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, input_entry.get().upper())


root = tk.Tk()
root.title("Uppercase Converter")


tk.Label(root, text="Enter text:").grid(row=0, column=0)
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

tk.Button(root, text="Convert", command=convert_to_upper).grid(row=1, column=0, columnspan=2)

tk.Label(root, text="Uppercase:").grid(row=2, column=0)
output_entry = tk.Entry(root)
output_entry.grid(row=2, column=1)
root.mainloop()
