from applications import *

"""
Application setup and launch
"""

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    app.master.title("Calculator TI-84")
    app.master.resizable(0, 0)

    app.mainloop()