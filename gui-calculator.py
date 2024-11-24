import tkinter as tk
import math

# ---- Function Definitions ----

# Function to update the expression in the entry widget
def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)  # Clear current entry
    entry.insert(tk.END, current_expression + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to delete the last character
def delete_last():
    current_expression = entry.get()
    entry.delete(len(current_expression)-1, tk.END)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function for square root
def square_root():
    try:
        current_value = float(entry.get())
        result = math.sqrt(current_value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for factorial
def factorial():
    try:
        current_value = int(entry.get())
        result = math.factorial(current_value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for power (x^y)
def power_of():
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + '**')

# Function for exponential (e^x)
def exponential():
    current_value = entry.get()
    try:
        result = math.exp(float(current_value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for log (base 10)
def log():
    current_value = entry.get()
    try:
        result = math.log10(float(current_value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for natural log (ln)
def ln():
    current_value = entry.get()
    try:
        result = math.log(float(current_value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for pi
def insert_pi():
    entry.insert(tk.END, str(math.pi))

# ---- GUI Setup ----

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display the input/output
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=5)

# ---- Button Layout ----

# List of button definitions (text, row, column, and command function)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('exp', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('pi', 4, 4),
    ('C', 5, 0), ('del', 5, 1), ('log', 5, 2), ('ln', 5, 3), ('!', 5, 4)
]

# Creating and adding buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear_entry)
    elif text == 'del':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=delete_last)
    elif text == 'sqrt':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=square_root)
    elif text == '^':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=power_of)
    elif text == 'exp':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=exponential)
    elif text == 'log':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=log)
    elif text == 'ln':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=ln)
    elif text == 'pi':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=insert_pi)
    elif text == '!':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=factorial)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# ---- Start the GUI Event Loop ----
root.mainloop()
