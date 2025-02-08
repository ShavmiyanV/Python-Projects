from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), 
              textvariable=self.equation, justify='right').place(x=0, y=0)

        self.create_buttons(master)

    def create_buttons(self, master):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        x = 0
        y = 70

        for button in buttons:
            Button(master, text=button, width=10, height=3, 
                   command=lambda value=button: self.on_button_click(value)).place(x=x, y=y)
            x += 89
            if x > 267:
                x = 0
                y += 70

    def on_button_click(self, value):
        if value == "C":
            self.clear()
        elif value == "=":
            self.solve()
        else:
            self.show(value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
