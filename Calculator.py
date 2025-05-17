import tkinter as tk
from tkinter import font

def digit_input(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def clear_display():
    display.delete(0, tk.END)

def delete_last():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def operation_add():
    first_number = display.get()
    global stored_value
    global operation
    operation = "summation"
    stored_value = float(first_number)
    display.delete(0, tk.END)

def operation_subtract():
    first_number = display.get()
    global stored_value
    global operation
    operation = "difference"
    stored_value = float(first_number)
    display.delete(0, tk.END)

def operation_multiply():
    first_number = display.get()
    global stored_value
    global operation
    operation = "product"
    stored_value = float(first_number)
    display.delete(0, tk.END)

def operation_divide():
    first_number = display.get()
    global stored_value
    global operation
    operation = "quotient"
    stored_value = float(first_number)
    display.delete(0, tk.END)

def calculate_result():
    second_number = display.get()
    display.delete(0, tk.END)
    
    try:
        if operation == "summation":
            display.insert(0, stored_value + float(second_number))
        elif operation == "difference":
            display.insert(0, stored_value - float(second_number))
        elif operation == "product":
            display.insert(0, stored_value * float(second_number))
        elif operation == "quotient":
            display.insert(0, stored_value / float(second_number))
    except ZeroDivisionError:
        display.insert(0, "Undefined")
    except:
        display.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Mathematical Calculator")
root.geometry("300x450")
root.resizable(False, False)

# Display widget
display = tk.Entry(root, width=14, borderwidth=5, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons with mathematical terms
button_font = font.Font(size=12, weight='bold')

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('Quotient', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('Product', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('Difference', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('⌫', 4, 2), ('Summation', 4, 3),
    ('Clear', 5, 0), ('Result', 5, 1, 1, 3)  # Result spans 3 columns
]

# Create and place buttons
for button in buttons:
    text, row, col = button[0], button[1], button[2]
    if text == 'Clear':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=clear_display)
    elif text == 'Result':
        colspan = button[3] if len(button) > 3 else 1
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=calculate_result)
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
        continue
    elif text == 'Summation':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=operation_add)
    elif text == 'Difference':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=operation_subtract)
    elif text == 'Product':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=operation_multiply)
    elif text == 'Quotient':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=operation_divide)
    elif text == '⌫':
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=delete_last)
    else:
        btn = tk.Button(root, text=text, padx=10, pady=20, font=button_font, command=lambda num=text: digit_input(num))
    
    btn.grid(row=row, column=col, sticky="nsew")

# Configure grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()