import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.config(bg='#F3FEFF')
        # Set window size

        self.display = tk.Entry(master, width=24, justify='right', font=('Helvetica', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky='ew')

        # Define button colors and font
        button_bg = '#8CF7C3'
        button_fg = '#002113'
        button_font = ('Helvetica', 14)

        style = ttk.Style()
        style.configure('Rounded.TButton', font=button_font, borderwidth=0,
                        padding=10, focusthickness=0)

        # Define buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'DEL'
        ]

        # Create and layout buttons with padding and rounded corners
        for i, button in enumerate(self.buttons):
            row = i // 4 + 1
            col = i % 4
            btn = ttk.Button(master, text=button, style='Rounded.TButton', command=lambda x=button: self.click(x))
            btn.grid(row=row, column=col, padx=8, pady=8)

        # Initialize calculator state
        self.clear()

    def click(self, key):
        if key == '=':
            # Calculate the result
            try:
                result = str(eval(self.expression))
            except:
                result = 'ERROR'
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = ''
        elif key == 'C':
            # Clear the display
            self.clear()
        elif key == 'DEL':
            # Delete the last character from the display
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        else:
            # Append the key to the expression
            self.expression += str(key)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ''
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, '0')


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
