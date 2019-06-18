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

        # Calculator settings
        self.calcMode = IntVar()
        self.angleMode = IntVar()

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
        self.parser = Calculate(self.expression,
                                int(self.angleMode.get()),
                                int(self.calcMode.get()))

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

    def secondButton(self):
        # If clicked, replace the text and functions of all buttons with their alternatives
        if self.defaultMode:
            self.defaultMode = False
            self.secondBtnFunctions()
        else:
            self.defaultMode = True
            self.defaultBtnFunctions()

    def createWidgets(self):
        self.displayScroll = Scrollbar(self.master)
        self.displayScroll.grid(row=0, column=5, rowspan=8, sticky='ns')

        self.display = Entry(self.master, xscrollcommand=self.displayScroll.set, width=24)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        self.displayScroll.config(command=self.display.xview)

        # First Row
        self.second = Button(self.master, text="2nd", height=3, width=6, borderwidth=1,
                            highlightbackground="yellow", font=('Helvetica', '11', "bold"),
                            command=lambda: self.secondButton(), relief=RAISED, justify=RIGHT)
        self.second.grid(row=1, column=0, sticky="nesw")
        self.modeButton = Button(self.master, text="MODE", height=3, width=6, borderwidth=1,
                            highlightbackground="black", font=('Helvetica', '11', "bold"),
                            command=lambda: self.modeMenu(), relief=RAISED, justify=RIGHT)
        self.modeButton.grid(row=1, column=1, sticky="nesw")
        self.math = Button(self.master, text="MATH", height=3, width=6, borderwidth=1,
                           highlightbackground="black", font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.math.grid(row=1, column=2, sticky="nesw")
        self.delete = Button(self.master, text="DEL", height=3, width=6,  borderwidth=1,
                            highlightbackground="black", font=('Helvetica', '11', "bold"),
                            command=lambda: self.deleteEnd(), relief=RAISED, justify=RIGHT)
        self.delete.grid(row=1, column=3, sticky="nesw")
        self.clear = Button(self.master, text="CLEAR", height=3, width=6, borderwidth=1,
                            highlightbackground="black", command=lambda: self.clearEntry(),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.clear.grid(row=1, column=4, sticky="nesw")

        # Second Row
        self.inverse = Button(self.master, text="X^-1", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("^(-1)"),
                              font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.inverse.grid(row=2, column=0, sticky="nesw")
        self.sine = Button(self.master, text="SIN", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("sin("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.sine.grid(row=2, column=1, sticky="nesw")
        self.cosine = Button(self.master, text="COS", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("cos("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.cosine.grid(row=2, column=2, sticky="nesw")
        self.tangent = Button(self.master, text="TAN", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("tan("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.tangent.grid(row=2, column=3, sticky="nesw")

        self.exponent = Button(self.master, text="^", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("^"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.exponent.grid(row=2, column=4, sticky="nesw")

        # Fifth Row
        self.squared = Button(self.master, text="X^2", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("^2"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.squared.grid(row=3, column=0, sticky="nesw")
        self.comma = Button(self.master, text=",", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry(","),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.comma.grid(row=3, column=1, sticky="nesw")
        self.openParen = Button(self.master, text="(", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.openParen.grid(row=3, column=2, sticky="nesw")
        self.closedParen = Button(self.master, text=")", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry(")"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.closedParen.grid(row=3, column=3, sticky="nesw")

        self.divide = Button(self.master, text="%", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("/"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.divide.grid(row=3, column=4, sticky="nesw")

        # Third Row
        self.commonLog = Button(self.master, text="LOG", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("log("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.commonLog.grid(row=4, column=0, sticky="nesw")
        self.seven = Button(self.master, text="7", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("7"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.seven.grid(row=4, column=1, sticky="nesw")
        self.eight = Button(self.master, text="8", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("8"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.eight.grid(row=4, column=2, sticky="nesw")
        self.nine = Button(self.master, text="9", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("9"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.nine.grid(row=4, column=3, sticky="nesw")

        self.multiply = Button(self.master, text="X", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("*"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.multiply.grid(row=4, column=4, sticky="nesw")

        # Fourth Row
        self.naturalLog = Button(self.master, text="LN", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("ln("),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.naturalLog.grid(row=5, column=0, sticky="nesw")
        self.four = Button(self.master, text="4", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("4"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.four.grid(row=5, column=1, sticky="nesw")
        self.five = Button(self.master, text="5", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("5"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.five.grid(row=5, column=2, sticky="nesw")
        self.six = Button(self.master, text="6", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("6"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.six.grid(row=5, column=3, sticky="nesw")

        self.subtract = Button(self.master, text="-", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("-"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.subtract.grid(row=5, column=4, sticky="nesw")

        # Fifth Row
        self.sto = Button(self.master, text="STO->", height=3, width=6, borderwidth=1,
                            highlightbackground="black", font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.sto.grid(row=6, column=0, sticky="nesw")
        self.one = Button(self.master, text="1", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("1"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.one.grid(row=6, column=1, sticky="nesw")
        self.two = Button(self.master, text="2", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("2"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.two.grid(row=6, column=2, sticky="nesw")
        self.three = Button(self.master, text="3", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("3"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.three.grid(row=6, column=3, sticky="nesw")

        self.add = Button(self.master, text="+", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.enterInEntry("+"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.add.grid(row=6, column=4, sticky="nesw")

        # Sixth Row
        self.exit = Button(self.master, text="ON", height=3, width=6, borderwidth=1,
                            highlightbackground="black", command=lambda: self.master.destroy(),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.exit.grid(row=7, column=0, sticky="nesw")
        self.zero = Button(self.master, text="0", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("0"),
                           font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.zero.grid(row=7, column=1, sticky="nesw")
        self.decimal = Button(self.master, text=".", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("."),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.decimal.grid(row=7, column=2, sticky="nesw")
        self.negative = Button(self.master, text="(-)", height=3, width=6, borderwidth=1, command=lambda: self.enterInEntry("(-"),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.negative.grid(row=7, column=3, sticky="nesw")
        self.equals = Button(self.master, text="ENTER", height=3, width=6, borderwidth=1,
                            highlightbackground="blue", command=lambda: self.calculate(),
                            font=('Helvetica', '11', "bold"), relief=RAISED, justify=RIGHT)
        self.equals.grid(row=7, column=4, sticky="nesw")

    # Layout and button changes for when the "second button" is pressed
    def secondBtnFunctions(self):
        # First Row
        self.modeButton["text"] = "QUIT"
        self.modeButton["command"] = lambda: self.destroyMenus()

        # Second Row
        self.inverse["text"] = "MATRX"
        self.inverse["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.sine["text"] = "SIN^-1"
        self.sine["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.cosine["text"] = "COS^-1"
        self.cosine["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.tangent["text"] = "TAN^-1"
        self.tangent["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        self.exponent["text"] = "π"
        self.exponent["command"] = lambda: [self.enterInEntry("π"), self.secondButton()]

        # Third Row
        self.squared["text"] = "√"
        self.squared["command"] = lambda: [self.enterInEntry("√("), self.secondButton()]
        self.comma["text"] = "EE"
        self.comma["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.openParen["text"] = "{"
        self.openParen["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.closedParen["text"] = "}"
        self.closedParen["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        self.divide["text"] = "e"
        self.divide["command"] = lambda: [self.enterInEntry("e"), self.secondButton()]

        # Fourth Row
        self.commonLog["text"] = "10^x"
        self.commonLog["command"] = lambda: [self.enterInEntry("10^("), self.secondButton()]
        self.seven["text"] = "u"
        self.seven["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.eight["text"] = "v"
        self.eight["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.nine["text"] = "w"
        self.nine["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        self.multiply["text"] = "["
        self.multiply["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        # Fifth Row
        self.naturalLog["text"] = "e"
        self.naturalLog["command"] = lambda: [self.enterInEntry("e"), self.secondButton()]
        self.four["text"] = "L4"
        self.four["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.five["text"] = "L5"
        self.five["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.six["text"] = "L6"
        self.six["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        self.subtract["text"] = "]"
        self.subtract["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        # Sixth Row
        self.sto["text"] = "RCL"
        self.one["text"] = "L1"
        self.one["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.two["text"] = "L2"
        self.two["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.three["text"] = "L3"
        self.three["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        self.add["text"] = "MEM"
        self.add["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

        # Seventh Row
        self.zero["text"] = "CATALOG"
        self.zero["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.zero["font"] = ('Helvetica', '8', "bold")
        self.decimal["text"] = "i"
        self.decimal["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]
        self.negative["text"] = "ANS"
        self.negative["command"] = lambda: [self.enterInEntry(self.storedAnswers[-1]), self.secondButton()]
        self.equals["text"] = "ENTRY"
        self.equals["command"] = lambda: [self.replaceEntry("0"), self.secondButton()]

    # Layout and button changes to revert back to original layout
    def defaultBtnFunctions(self):
        # First Row
        self.modeButton["text"] = "MODE"
        self.modeButton["command"] = lambda: self.modeMenu()

        # Second Row
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

        # Third Row
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

        # Fourth Row
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

        # Fifth Row
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

        # Sixth Row
        self.sto["text"] = "STO->"
        self.one["text"] = "1"
        self.one["command"] = lambda: self.enterInEntry("1")
        self.two["text"] = "2"
        self.two["command"] = lambda: self.enterInEntry("2")
        self.three["text"] = "3"
        self.three["command"] = lambda: self.enterInEntry("3")

        self.add["text"] = "+"
        self.add["command"] = lambda: self.enterInEntry("+")

        # Seventh Row
        self.zero["text"] = "0"
        self.zero["command"] = lambda: self.enterInEntry("0")
        self.zero["font"] = ('Helvetica', '11', "bold")
        self.decimal["text"] = "."
        self.decimal["command"] = lambda: self.enterInEntry(".")
        self.negative["text"] = "(-)"
        self.negative["command"] = lambda: self.enterInEntry("(-")
        self.equals["text"] = "ENTER"
        self.equals["command"] = lambda: self.calculate()

    # Menu options for mode options
    def modeMenu(self):
        self.mode = Toplevel(self.master)
        self.x = self.master.winfo_x()
        self.y = self.master.winfo_y()
        self.mode.geometry("+%d+%d" % (self.x, self.y))
        self.mode.resizable(0, 0)

        # Calculator Modes
        self.normal = Radiobutton(self.mode, text="NORMAL", font=('Helvetica', '8'),
                                        variable=self.calcMode, value=0)
        self.normal.grid(row=0, column=0)
        self.scientific = Radiobutton(self.mode, text="SCI", font=('Helvetica', '8'),
                                        variable=self.calcMode, value=1)
        self.scientific.grid(row=0, column=1)
        self.english = Radiobutton(self.mode, text="ENG", font=('Helvetica', '8'),
                                        variable=self.calcMode, value=2)
        self.english.grid(row=0, column=2)

        # Angle Mode
        self.radian = Radiobutton(self.mode, text="RADIAN", font=('Helvetica', '8'),
                                        variable=self.angleMode, value=1)
        self.radian.grid(row=1, column=0)
        self.degree = Radiobutton(self.mode, text="DEGREE", font=('Helvetica', '8'),
                                        variable=self.angleMode, value=0)
        self.degree.grid(row=1, column=1)

    def destroyMenus(self):
        try:
            self.mode.destroy()
        except:
            pass