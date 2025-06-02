import tkinter as tk


def click(event):
    current_text = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(event.widget["text"]))


def clear():
    entry.delete(0, tk.END)


def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['AC', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(row_frame, text=char, font="Arial 18", relief=tk.GROOVE, border=0)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        if char == "C":
            btn.config(command=clear)
        elif char == "=":
            btn.config(command=equal)
        else:
            btn.bind("<Button-1>", click)

root.mainloop()
