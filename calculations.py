import math
from decimal import Decimal
from containers import *

class Calculate:
    def __init__(self, expression):
        self.expression = expression

        self.vals = Stack()
        self.ops = Stack()
        self.funcs = Stack()

        # Identify all valid characters
        self.operators = "+-/*^"
        self.nums = ".0123456789"
        self.vars = {
            'e': 2.718281828459045,
            'π': 3.141592653589793}

    # Basic operations
    def operations(self, op, var1, var2):
        self.operators = {
            "+": var2 + var1,
            "-": var2 - var1,
            "*": var2 * var1,
            "/": var2 / var1,
            "^": var2 ** var1
        }

        return self.operators[str(op)]

    # Basic functions
    def functions(self, function, var1):
        self.functionsList = {
            "sin": math.sin(math.radians(var1)),
            "cos": math.cos(math.radians(var1)),
            "tan": math.tan(math.radians(var1)) if var1 != 90 else None,
            "log": math.log10(var1),
            "ln": math.log(var1),
            "√": math.sqrt(var1)
        }

        return self.functionsList[function]

    # Checks if the current operation is higher in PEMDAS than the previous one
    def currentOpHasPrec(self, op1, op2):
        if op2 == "(" or op2 == ")":
            return False
        elif (op1 == '*' or op1 == '/' or op1 == "^" or op1 == "(") \
                and (op2 == "+" or op2 == "-"):
            return False
        else:
            return True

    def pushCurrentNum(self):
        if self.currentNum != "":
            self.vals.push(Decimal(self.currentNum))
            self.currentNum = ""

    def pushValue(self, function):
        self.value = function
        self.vals.push(self.value)

    def evaluateExpr(self):
        # Checks if expression in parenthesis is a negative number
        if self.currentChar == "-" and self.expression[self.index - 1] == "(":
            self.ops.push("(-")
        else:
            # Start evaluating all numbers and operations based on PEMDAS
            while not self.ops.isEmpty() and self.ops.peek() != "(" and \
                    self.currentOpHasPrec(self.currentChar, self.ops.peek()):
                self.pushValue(self.operations(self.ops.pop(), self.vals.pop(), self.vals.pop()))

            self.ops.push(self.currentChar)

    def evaluateParen(self):
        # If negative sign is found, evaluate it and remove the negative sign
        if "(-" in self.ops.stack:
            self.pushValue(-1 * self.vals.pop())
            self.ops.pop()

        while self.ops.peek() != "(":
            self.pushValue(self.operations(self.ops.pop(), self.vals.pop(), self.vals.pop()))

        if not self.funcs.isEmpty():
            self.pushValue(self.functions(self.funcs.pop(), self.vals.pop()))

        self.ops.pop()

        # Replace parenthesis with a multiplication sign if there is a number next to it
        if self.expression.find("(") - 1 >= 0 and \
                self.expression[self.expression.find("(") - 1] in self.nums:
            self.ops.push("*")

    def parse(self):
        # Place holders to store any given current number or function
        self.currentNum = ""
        self.currentFuncName = ""

        self.parenCounter = 0
        self.index = 0

        while self.index < len(self.expression):
            self.currentChar = self.expression[self.index]

            if self.currentChar in self.nums:
                self.currentNum += self.currentChar

            elif self.currentChar in self.vars:
                self.pushCurrentNum()
                self.vals.push(self.vars[self.currentChar])

            # Checks for functions like sin or sqrt
            elif self.currentChar.isalpha() or self.currentChar == "√":
                self.currentFuncName += self.currentChar

            elif self.currentChar == "(":
                self.ops.push(self.currentChar)
                self.pushCurrentNum()

                # If these parenthesis are apart of a function, store it
                if self.currentFuncName != "":
                    self.funcs.push(self.currentFuncName)
                    self.currentFuncName = ""

                self.parenCounter += 1

            elif self.currentChar == ")":
                self.pushCurrentNum()
                self.evaluateParen()

                self.parenCounter -= 1

            # If an operator is found, store it in memory and evaluate the values with it
            elif self.currentChar in self.operators:
                self.pushCurrentNum()
                self.evaluateExpr()

            self.index += 1

        # Evaluates any remaining parenthesis in the expression
        self.pushCurrentNum()

        while self.parenCounter > 0:
            self.evaluateParen()
            self.parenCounter -= 1

        while not self.ops.isEmpty():
            self.pushValue(self.operations(self.ops.pop(), self.vals.pop(), self.vals.pop()))

        return self.vals.peek()

# Problems:
# Can't place functions at the user's cursor
# Can't calculate expression when enter key is pressed