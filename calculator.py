import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        textDisplayed = "Hello"
        self.display = tk.Label(text = textDisplayed, background = '#D3D3D3', font=("Verdana", 22), foreground = 'black')

        self.number0 = tk.Button(self, text="0")
        self.number1 = tk.Button(self, text="1")
        self.number2 = tk.Button(self, text="2")
        self.number3 = tk.Button(self, text="3")
        self.number4 = tk.Button(self, text="4")
        self.number5 = tk.Button(self, text="5")
        self.number6 = tk.Button(self, text="6")
        self.number7 = tk.Button(self, text="7")
        self.number8 = tk.Button(self, text="8")
        self.number9 = tk.Button(self, text="9")

        self.dot = tk.Button(self, text=",")
        self.equal = tk.Button(self, text="=")
        self.slash = tk.Button(self, text="/")
        self.multiple = tk.Button(self, text="X")
        self.substract = tk.Button(self, text="-")
        self.plus = tk.Button(self, text="+")

        self.display.grid(ipadx = 20, ipady = 20, row = 1, column = 1, columnspan = 4, rowspan = 2, sticky="nesw")

        self.number0.grid(ipadx = 20, ipady = 20, row = 6, column = 2, sticky="nesw")
        self.number1.grid(ipadx = 20, ipady = 20, row = 5, column = 1, sticky="nesw")
        self.number2.grid(ipadx = 20, ipady = 20, row = 5, column = 2, sticky="nesw")
        self.number3.grid(ipadx = 20, ipady = 20, row = 5, column = 3, sticky="nesw")
        self.number4.grid(ipadx = 20, ipady = 20, row = 4, column = 1, sticky="nesw")
        self.number5.grid(ipadx = 20, ipady = 20, row = 4, column = 2, sticky="nesw")
        self.number6.grid(ipadx = 20, ipady = 20, row = 4, column = 3, sticky="nesw")
        self.number7.grid(ipadx = 20, ipady = 20, row = 3, column = 1, sticky="nesw")
        self.number8.grid(ipadx = 20, ipady = 20, row = 3, column = 2, sticky="nesw")
        self.number9.grid(ipadx = 20, ipady = 20, row = 3, column = 3, sticky="nesw")

        self.dot.grid(ipadx = 20, ipady = 20, row = 6, column = 1, sticky="nesw")
        self.equal.grid(ipadx = 20, ipady = 20, row = 6, column = 3, sticky="nesw")
        self.slash.grid(ipadx = 20, ipady = 20, row = 6, column = 4, sticky="nesw")
        self.multiple.grid(ipadx = 20, ipady = 20, row = 5, column = 4, sticky="nesw")
        self.substract.grid(ipadx = 20, ipady = 20, row = 4, column = 4, sticky="nesw")
        self.plus.grid(ipadx = 20, ipady = 20, row = 3, column = 4, sticky="nesw")




if __name__ == "__main__":
    app = Calculator()
    app.title("Calculator")
    app.mainloop()