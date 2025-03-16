
import tkinter as tk

# Function to update the entry field
def on_button_click(value):
    entry_field.insert(tk.END, value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create entry field
entry_field = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, relief="ridge")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), bg="green", fg="white",
                        command=calculate)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                        command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=43, height=2, font=("Arial", 14), bg="red", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the main loop
root.mainloop()
