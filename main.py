from applications import *

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    app.master.title("Calculator TI-84")
    app.master.resizable(0, 0)
    app.master.configure(bg="grey")

    message = "For more information on how to use this application, " \
                          "go to the README file of this project"

    messagebox.showinfo("Welcome!", message)

    app.mainloop() # Starts the application