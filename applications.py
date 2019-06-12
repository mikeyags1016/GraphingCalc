from tkinter import *
from tkinter import messagebox
from calculations import *

# Things to do:
#
# Continue Documentation
# Continue adding functions to calculator
# Add horizontal slide bar to display

class Application(Frame):
    # Initial setup for the master frame that places all of the widgets
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0)
        self.createWidgets()

        self.defaultMode = True # For inverse function
        self.storedAnswers = []

    def clearEntry(self):
        # Wipes stored answers if any
        if self.display.get() == "0":
            self.storedAnswers = []

        self.display.delete(0, END)
        self.display.insert(0, "0")

    def replaceEntry(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def deleteEnd(self):
        self.entry = self.display.get()
        self.entrySize = len(self.entry)

        if self.entrySize <= 1:
            self.clearEntry()
        else:
            self.entry = self.entry[0:-1] # Remove just the last character of the text
            self.replaceEntry(self.entry)

    def enterInEntry(self, value):
        self.entry = self.display.get()
        self.entrySize = len(self.entry)

        # Replaces the text with input if entry is already 0, adds on to previous input otherwise
        if self.entry == "0":
            self.replaceEntry(value)
        else:
            self.display.insert(self.entrySize, value)

    def calculate(self):
        self.expression = self.display.get()
        self.parser = Calculate(self.expression)

        # Try to calculate the current expression and display it
        # Display error message if input is invalid
        try:
            # Parse the expression through the "calculate" method in the Calculate class
            self.result = self.parser.parse()
            self.storedAnswers.append(self.result) # Store answer
            self.clearEntry()
            self.replaceEntry(self.result)
        except:
            messagebox.showinfo("Error", "Invalid Input")

    # Places all widgets and buttons
    def createWidgets(self):
        self.displayScroll = Scrollbar(self.master)
        self.displayScroll.grid(row=0, column=5, rowspan=2)

        self.display = Entry(self.master, xscrollcommand=self.displayScroll.set)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4)

        self.displayScroll.config(command=self.display.xview)

        # First Row
        self.second = Button(self.master, text="2nd", height=3, width=6, borderwidth=0,
                            highlightbackground="yellow", font=('Helvetica', '11', "bold"),
                            command=lambda: self.secondButton())
        self.second.grid(row=1, column=0, sticky="nesw")
        self.mode = Button(text="MODE", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", font=('Helvetica', '11', "bold"))
        self.mode.grid(row=1, column=1, sticky="nesw")
        self.delete = Button(text="DEL", height=3, width=6,  borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"),
                            command=lambda: self.deleteEnd())
        self.delete.grid(row=1, column=2, sticky="nesw")

        # Second Row
        self.alpha = Button(text="ALPHA", height=3, width=6, borderwidth=0,
                            highlightbackground="green", font=('Helvetica', '11', "bold"))
        self.alpha.grid(row=2, column=0, sticky="nesw")
        self.variables = Button(text="X,T,0,n", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", font=('Helvetica', '11', "bold"))
        self.variables.grid(row=2, column=1, sticky="nesw")
        self.stat = Button(text="STAT", height=3, width=6, borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"))
        self.stat.grid(row=2, column=2, sticky="nesw")

        # Third Row
        self.math = Button(text="MATH", height=3, width=6, borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"))
        self.math.grid(row=3, column=0, sticky="nesw")
        self.apps = Button(text="APPS", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", font=('Helvetica', '11', "bold"))
        self.apps.grid(row=3, column=1, sticky="nesw")
        self.prgm = Button(text="PGRM", height=3, width=6, borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"))
        self.prgm.grid(row=3, column=2, sticky="nesw")
        self.vars = Button(text="VARS", height=3, width=6, borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"))
        self.vars.grid(row=3, column=3, sticky="nesw")

        self.clear = Button(text="CLEAR", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.clearEntry(),
                            font=('Helvetica', '11', "bold"))
        self.clear.grid(row=3, column=4, sticky="nesw")

        # Fourth Row
        self.inverse = Button(text="X^-1", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("^(-1)"),
                              font=('Helvetica', '11', "bold"))
        self.inverse.grid(row=4, column=0, sticky="nesw")
        self.sine = Button(text="SIN", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("sin("),
                            font=('Helvetica', '11', "bold"))
        self.sine.grid(row=4, column=1, sticky="nesw")
        self.cosine = Button(text="COS", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("cos("),
                            font=('Helvetica', '11', "bold"))
        self.cosine.grid(row=4, column=2, sticky="nesw")
        self.tangent = Button(text="TAN", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("tan("),
                            font=('Helvetica', '11', "bold"))
        self.tangent.grid(row=4, column=3, sticky="nesw")

        self.exponent = Button(text="^", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("^"),
                            font=('Helvetica', '11', "bold"))
        self.exponent.grid(row=4, column=4, sticky="nesw")

        # Fifth Row
        self.squared = Button(text="X^2", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("^2"),
                            font=('Helvetica', '11', "bold"))
        self.squared.grid(row=5, column=0, sticky="nesw")
        self.comma = Button(text=",", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry(","),
                            font=('Helvetica', '11', "bold"))
        self.comma.grid(row=5, column=1, sticky="nesw")
        self.openParen = Button(text="(", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("("),
                            font=('Helvetica', '11', "bold"))
        self.openParen.grid(row=5, column=2, sticky="nesw")
        self.closedParen = Button(text=")", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry(")"),
                            font=('Helvetica', '11', "bold"))
        self.closedParen.grid(row=5, column=3, sticky="nesw")

        self.divide = Button(text="%", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", command=lambda: self.enterInEntry("/"),
                            font=('Helvetica', '11', "bold"))
        self.divide.grid(row=5, column=4, sticky="nesw")

        # Sixth Row
        self.commonLog = Button(text="LOG", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("log("),
                            font=('Helvetica', '11', "bold"))
        self.commonLog.grid(row=6, column=0, sticky="nesw")
        self.seven = Button(text="7", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("7"),
                            font=('Helvetica', '11', "bold"))
        self.seven.grid(row=6, column=1, sticky="nesw")
        self.eight = Button(text="8", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("8"),
                            font=('Helvetica', '11', "bold"))
        self.eight.grid(row=6, column=2, sticky="nesw")
        self.nine = Button(text="9", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("9"),
                            font=('Helvetica', '11', "bold"))
        self.nine.grid(row=6, column=3, sticky="nesw")

        self.multiply = Button(text="X", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", command=lambda: self.enterInEntry("*"),
                            font=('Helvetica', '11', "bold"))
        self.multiply.grid(row=6, column=4, sticky="nesw")

        # Seventh Row
        self.naturalLog = Button(text="LN", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.enterInEntry("ln("),
                            font=('Helvetica', '11', "bold"))
        self.naturalLog.grid(row=7, column=0, sticky="nesw")
        self.four = Button(text="4", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("4"),
                            font=('Helvetica', '11', "bold"))
        self.four.grid(row=7, column=1, sticky="nesw")
        self.five = Button(text="5", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("5"),
                            font=('Helvetica', '11', "bold"))
        self.five.grid(row=7, column=2, sticky="nesw")
        self.six = Button(text="6", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("6"),
                            font=('Helvetica', '11', "bold"))
        self.six.grid(row=7, column=3, sticky="nesw")

        self.subtract = Button(text="-", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", command=lambda: self.enterInEntry("-"),
                            font=('Helvetica', '11', "bold"))
        self.subtract.grid(row=7, column=4, sticky="nesw")

        # Eighth Row
        self.sto = Button(text="STO->", height=3, width=6, borderwidth=0,
                            highlightbackground="black", font=('Helvetica', '11', "bold"))
        self.sto.grid(row=8, column=0, sticky="nesw")
        self.one = Button(text="1", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("1"),
                            font=('Helvetica', '11', "bold"))
        self.one.grid(row=8, column=1, sticky="nesw")
        self.two = Button(text="2", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("2"),
                            font=('Helvetica', '11', "bold"))
        self.two.grid(row=8, column=2, sticky="nesw")
        self.three = Button(text="3", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("3"),
                            font=('Helvetica', '11', "bold"))
        self.three.grid(row=8, column=3, sticky="nesw")

        self.add = Button(text="+", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", command=lambda: self.enterInEntry("+"),
                            font=('Helvetica', '11', "bold"))
        self.add.grid(row=8, column=4, sticky="nesw")

        # Ninth Row
        self.exit = Button(text="ON", height=3, width=6, borderwidth=0,
                            highlightbackground="black", command=lambda: self.master.destroy(),
                            font=('Helvetica', '11', "bold"))
        self.exit.grid(row=9, column=0, sticky="nesw")
        self.zero = Button(text="0", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("0"),
                           font=('Helvetica', '11', "bold"))
        self.zero.grid(row=9, column=1, sticky="nesw")
        self.decimal = Button(text=".", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("."),
                            font=('Helvetica', '11', "bold"))
        self.decimal.grid(row=9, column=2, sticky="nesw")
        self.negative = Button(text="(-)", height=3, width=6, borderwidth=0, command=lambda: self.enterInEntry("(-"),
                            font=('Helvetica', '11', "bold"))
        self.negative.grid(row=9, column=3, sticky="nesw")
        self.equals = Button(text="ENTER", height=3, width=6, borderwidth=0,
                            highlightbackground="blue", command=lambda: self.calculate(),
                            font=('Helvetica', '11', "bold"))
        self.equals.grid(row=9, column=4, sticky="nesw")

    def secondButton(self):
        # If clicked, replace the text and functions of all buttons with their alternatives
        if self.defaultMode:
            self.defaultMode = False

            # First Row
            self.mode["text"] = "QUIT"

            # Second Row
            self.alpha["text"] = "A-LOCK"
            self.variables["text"] = "LINK"
            self.stat["text"] = "LIST"

            # Third Row
            self.math["text"] = "TEST"
            self.apps["text"] = "ANGLE"
            self.prgm["text"] = "DRAW"
            self.vars["text"] = "DISTR"

            # Fourth Row
            self.inverse["text"] = "MATRX"
            self.inverse["command"] = lambda: self.replaceEntry("0")
            self.sine["text"] = "SIN^-1"
            self.sine["command"] = lambda: self.replaceEntry("0")
            self.cosine["text"] = "COS^-1"
            self.cosine["command"] = lambda: self.replaceEntry("0")
            self.tangent["text"] = "TAN^-1"
            self.tangent["command"] = lambda: self.replaceEntry("0")

            self.exponent["text"] = "π"
            self.exponent["command"] = lambda: self.enterInEntry("π")

            # Fifth Row
            self.squared["text"] = "√"
            self.squared["command"] = lambda: self.enterInEntry("√(")
            self.comma["text"] = "EE"
            self.comma["command"] = lambda: self.replaceEntry("0")
            self.openParen["text"] = "{"
            self.openParen["command"] = lambda: self.replaceEntry("0")
            self.closedParen["text"] = "}"
            self.closedParen["command"] = lambda: self.replaceEntry("0")

            self.divide["text"] = "e"
            self.divide["command"] = lambda: self.enterInEntry("e")

            # Sixth Row
            self.commonLog["text"] = "10^x"
            self.commonLog["command"] = lambda: self.enterInEntry("10^(")
            self.seven["text"] = "u"
            self.seven["command"] = lambda: self.replaceEntry("0")
            self.eight["text"] = "v"
            self.eight["command"] = lambda: self.replaceEntry("0")
            self.nine["text"] = "w"
            self.nine["command"] = lambda: self.replaceEntry("0")

            self.multiply["text"] = "["
            self.multiply["command"] = lambda: self.replaceEntry("0")

            # Seventh Row
            self.naturalLog["text"] = "e"
            self.naturalLog["command"] = lambda: self.enterInEntry("e")
            self.four["text"] = "L4"
            self.four["command"] = lambda: self.replaceEntry("0")
            self.five["text"] = "L5"
            self.five["command"] = lambda: self.replaceEntry("0")
            self.six["text"] = "L6"
            self.six["command"] = lambda: self.replaceEntry("0")

            self.subtract["text"] = "]"
            self.subtract["command"] = lambda: self.replaceEntry("0")

            # Eighth Row
            self.sto["text"] = "RCL"
            self.one["text"] = "L1"
            self.one["command"] = lambda: self.replaceEntry("0")
            self.two["text"] = "L2"
            self.two["command"] = lambda: self.replaceEntry("0")
            self.three["text"] = "L3"
            self.three["command"] = lambda: self.replaceEntry("0")

            self.add["text"] = "MEM"
            self.add["command"] = lambda: self.replaceEntry("0")

            # Ninth Row
            self.zero["text"] = "CATALOG"
            self.zero["command"] = lambda: self.replaceEntry("0")
            self.zero["font"] = ('Helvetica', '8', "bold")
            self.decimal["text"] = "i"
            self.decimal["command"] = lambda: self.replaceEntry("0")
            self.negative["text"] = "ANS"
            self.negative["command"] = lambda: self.enterInEntry(self.storedAnswers[-1]) # CHANGE
            self.equals["text"] = "ENTRY"
            self.equals["command"] = lambda: self.replaceEntry("0")
        else:
            self.defaultMode = True

            # First Row
            self.mode["text"] = "MODE"

            # Second Row
            self.alpha["text"] = "ALPHA"
            self.variables["text"] = "X,T,0,n"
            self.stat["text"] = "STAT"

            # Third Row
            self.math["text"] = "MATH"
            self.apps["text"] = "APPS"
            self.prgm["text"] = "PGRM"
            self.vars["text"] = "VARS"

            # Fourth Row
            self.inverse["text"] = "x^-1"
            self.inverse["command"] = lambda: self.enterInEntry("x^(-1)")
            self.sine["text"] = "SIN"
            self.sine["command"] = lambda: self.enterInEntry("sin(")
            self.cosine["text"] = "COS"
            self.cosine["command"] = lambda: self.enterInEntry("cos(")
            self.tangent["text"] = "TAN"
            self.tangent["command"] = lambda: self.enterInEntry("tan(")

            self.exponent["text"] = "^"
            self.exponent["command"] = lambda: self.enterInEntry("^")

            # Fifth Row
            self.squared["text"] = "x^2"
            self.squared["command"] = lambda: self.enterInEntry("^2")
            self.comma["text"] = ","
            self.comma["command"] = lambda: self.enterInEntry(",")
            self.openParen["text"] = "("
            self.openParen["command"] = lambda: self.enterInEntry("(")
            self.closedParen["text"] = ")"
            self.closedParen["command"] = lambda: self.enterInEntry(")")

            self.divide["text"] = "%"
            self.divide["command"] = lambda: self.enterInEntry("/")

            # Sixth Row
            self.commonLog["text"] = "LOG"
            self.commonLog["command"] = lambda: self.enterInEntry("log(")
            self.seven["text"] = "7"
            self.seven["command"] = lambda: self.enterInEntry("7")
            self.eight["text"] = "8"
            self.eight["command"] = lambda: self.enterInEntry("8")
            self.nine["text"] = "9"
            self.nine["command"] = lambda: self.enterInEntry("9")

            self.multiply["text"] = "X"
            self.multiply["command"] = lambda: self.enterInEntry("*")

            # Seventh Row
            self.naturalLog["text"] = "LN"
            self.naturalLog["command"] = lambda: self.enterInEntry("ln(")
            self.four["text"] = "4"
            self.four["command"] = lambda: self.enterInEntry("4")
            self.five["text"] = "5"
            self.five["command"] = lambda: self.enterInEntry("5")
            self.six["text"] = "6"
            self.six["command"] = lambda: self.enterInEntry("6")

            self.subtract["text"] = "-"
            self.subtract["command"] = lambda: self.enterInEntry("-")

            # Eighth Row
            self.sto["text"] = "STO->"
            self.one["text"] = "1"
            self.one["command"] = lambda: self.enterInEntry("1")
            self.two["text"] = "2"
            self.two["command"] = lambda: self.enterInEntry("2")
            self.three["text"] = "3"
            self.three["command"] = lambda: self.enterInEntry("3")

            self.add["text"] = "+"
            self.add["command"] = lambda: self.enterInEntry("+")

            # Ninth Row
            self.zero["text"] = "0"
            self.zero["command"] = lambda: self.enterInEntry("0")
            self.zero["font"] = ('Helvetica', '11', "bold")
            self.decimal["text"] = "."
            self.decimal["command"] = lambda: self.enterInEntry(".")
            self.negative["text"] = "(-)"
            self.negative["command"] = lambda: self.enterInEntry("(-")
            self.equals["text"] = "ENTER"
            self.equals["command"] = lambda: self.calculate()
