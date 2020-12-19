import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.textDisplayed = tk.StringVar()
        self.textDisplayed.set("")
        self.reset = tk.BooleanVar()
        self.reset.set(False)
        self.display = tk.Label(textvariable = self.textDisplayed, background = '#D3D3D3', font=("Verdana", 22), foreground = 'black')

        self.number0 = tk.Button(self, text = "0", command = lambda : self.numberButtonClick(0))
        self.number1 = tk.Button(self, text = "1", command = lambda : self.numberButtonClick(1))
        self.number2 = tk.Button(self, text = "2", command = lambda : self.numberButtonClick(2))
        self.number3 = tk.Button(self, text = "3", command = lambda : self.numberButtonClick(3))
        self.number4 = tk.Button(self, text = "4", command = lambda : self.numberButtonClick(4))
        self.number5 = tk.Button(self, text = "5", command = lambda : self.numberButtonClick(5))
        self.number6 = tk.Button(self, text = "6", command = lambda : self.numberButtonClick(6))
        self.number7 = tk.Button(self, text = "7", command = lambda : self.numberButtonClick(7))
        self.number8 = tk.Button(self, text = "8", command = lambda : self.numberButtonClick(8))
        self.number9 = tk.Button(self, text = "9", command = lambda : self.numberButtonClick(9))

        self.dot = tk.Button(self, text=",", command = lambda : self.signButtonClick(","))
        self.equal = tk.Button(self, text="=", command = lambda : self.signButtonClick("="))
        self.slash = tk.Button(self, text="/", command = lambda : self.signButtonClick("/"))
        self.multiple = tk.Button(self, text="X", command = lambda : self.signButtonClick("*"))
        self.substract = tk.Button(self, text="-", command = lambda : self.signButtonClick("-"))
        self.plus = tk.Button(self, text="+", command = lambda : self.signButtonClick("+"))

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
    
    def numberButtonClick (self, number):
        str = ""
        if self.reset.get() == True:
            self.textDisplayed.set("")
            self.reset.set(False)
        
        if number == 0:
            str = self.textDisplayed.get() + "0"
        elif number == 1:
            str = self.textDisplayed.get() + "1"
        elif number == 2:
            str = self.textDisplayed.get() + "2"
        elif number == 3:
            str = self.textDisplayed.get() + "3"
        elif number == 4:
            str = self.textDisplayed.get() + "4"
        elif number == 5:
            str = self.textDisplayed.get() + "5"
        elif number == 6:
            str = self.textDisplayed.get() + "6"
        elif number == 7:
            str = self.textDisplayed.get() + "7"
        elif number == 8:
            str = self.textDisplayed.get() + "8"
        elif number == 9:
            str = self.textDisplayed.get() + "9"
        self.textDisplayed.set(str)

    def signButtonClick (self, sign):
        if sign == "=":
            try:
                self.textDisplayed.set(eval (self.textDisplayed.get()))
            except SyntaxError:
                    print("Syntax Error")
                    self.textDisplayed.set("")
            finally:
                self.reset.set(True)
        elif sign == ",":
            self.textDisplayed.set(self.textDisplayed.get() + ".")
        elif sign == "+":
            self.textDisplayed.set(self.textDisplayed.get() + "+")
        elif sign == "-":
            self.textDisplayed.set(self.textDisplayed.get() + "-")
        elif sign == "*":
            self.textDisplayed.set(self.textDisplayed.get() + "*")
        elif sign == "/":
            self.textDisplayed.set(self.textDisplayed.get() + "/")




if __name__ == "__main__":
    app = Calculator()
    app.title("Calculator")
    app.mainloop()