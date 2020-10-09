# imports
from tkinter import *


class App:
    def __init__(self, win):
        # Screen
        self.win = win
        # some variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        self.widgets()

    def create_account_widgets(self):
        self.n_username.set("")
        self.n_password.set("")
        self.login_frame.pack_forget()
        self.head["text"] = "Create Account"
        self.create_acc_frame.pack()

    def widgets(self):
        self.head = Label(self.win, text="LOGIN", font=("", 35), pady=10)
        self.head.pack()

        self.login_frame = Frame(self.win, padx=10, pady=10)
        Label(self.login_frame, text="Username: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Label(self.login_frame, text="Password: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.username, bd=5, font=("", 15)).grid(row=0, column=1)
        Entry(self.login_frame, textvariable=self.password, bd=5, font=("", 15)).grid(row=1, column=1)
        Button(self.login_frame, text=" Login ", bd=3, font=("", 15), padx=5, pady=5).grid(row=2, column=0)
        Button(self.login_frame, text=" Create Account ", bd=3, font=("", 15), padx=5, pady=5, command=self.create_account_widgets).grid(row=2, column=1)
        self.login_frame.pack()

        self.create_acc_frame = Frame(self.win, padx=10, pady=10)
        Label(self.create_acc_frame, text="Username: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Label(self.create_acc_frame, text="Password: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.create_acc_frame, textvariable=self.n_username, bd=5, font=("", 15)).grid(row=0, column=1)
        Entry(self.create_acc_frame, textvariable=self.n_password, bd=5, font=("", 15)).grid(row=1, column=1)
        Button(self.create_acc_frame, text=" Create Account ", bd=3, font=("", 15), padx=5, pady=5).grid(row=2, column=0)
        Button(self.create_acc_frame, text=" Go to login ", bd=3, font=("", 15), padx=5, pady=5).grid(row=2, column=1)



if __name__ == '__main__':
    screen = Tk()
    screen.title("Login form")

    App(screen)
    screen.mainloop()
