"""
Storage for data values and operators
"""

class Stack:
    def __init__(self):
        self.stack = []

    def peekTop(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        return None

    def isEmpty(self):
        if self.size() <= 0:
            return True
        return False

    def peek(self):
        return self.stack[-1]