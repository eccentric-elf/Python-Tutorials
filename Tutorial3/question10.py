import tkinter as tk

def calculate_distance():
    try:
        h = float(entry_h.get())
        i = float(entry_i.get())
        b = int(entry_b.get())

        d = h + sum(2 * (h := h * i) for _ in range(b))
        result.set(f"Total Distance: {d:.2f}")
    except:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Bouncy Ball")

tk.Label(root, text="Height:").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Label(root, text="Bounciness:").pack()
entry_i = tk.Entry(root)
entry_i.pack()

tk.Label(root, text="Bounces:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Button(root, text="Calculate", command=calculate_distance).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
