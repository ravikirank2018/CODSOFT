import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def on_calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return

    operation = operation_var.get()

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result_label.config(text="Invalid operation. Please select a valid operation.")
        return

    result_label.config(text=f"Result: {result}")


root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=15)
entry_num2.grid(row=0, column=1, padx=10, pady=10)


operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")  # default operation

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=0, column=2, padx=10, pady=10)


calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
