# imports
from tkinter import *
import sqlite3
from tkinter import messagebox as ms

db = sqlite3.connect("main.db")

c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL);")
db.commit()
db.close()


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

    def login(self):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()

        find_user = 'SELECT * FROM user WHERE username = ? and password = ?'
        cursor.execute(find_user, [(self.username.get()), (self.password.get())])

        result = cursor.fetchall()
        if result:
            self.login_frame.pack_forget()
            self.head['text'] = self.username.get() + '\n Logged in'
            self.head['padx'] = 50
            self.head['pady'] = 50
        else:
            ms.showerror("Oops", "Username not found.")

    def new_user(self):
        db = sqlite3.connect("main.db")
        cursor = db.cursor()

        find_user = 'SELECT username FROM user WHERE username = ?'
        cursor.execute(find_user, [(self.n_username.get())])
        if cursor.fetchall():
            ms.showerror("Error", "Username Taken Try a Different one.")
        else:
            ms.showinfo("Success", "Account is created.")
            self.login_widgets()

        insert = 'INSERT INTO user(username, password) VALUES(?,?)'
        cursor.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()



    def login_widgets(self):
        self.username.set("")
        self.password.set("")
        self.create_acc_frame.pack_forget()
        self.win.title("Login Form")
        self.head['text'] = "LOGIN"
        self.login_frame.pack()

    def create_account_widgets(self):
        self.n_username.set("")
        self.n_password.set("")
        self.login_frame.pack_forget()
        self.win.title("Create Account Form")
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
        Button(self.login_frame, text=" Login ", bd=3, font=("", 15), padx=5, pady=5, command=self.login).grid(row=2, column=0)
        Button(self.login_frame, text=" Create Account ", bd=3, font=("", 15), padx=5, pady=5, command=self.create_account_widgets).grid(row=2, column=1)
        self.login_frame.pack()

        self.create_acc_frame = Frame(self.win, padx=10, pady=10)
        Label(self.create_acc_frame, text="Username: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Label(self.create_acc_frame, text="Password: ", font=("", 20), padx=5, pady=5).grid(sticky=W)
        Entry(self.create_acc_frame, textvariable=self.n_username, bd=5, font=("", 15)).grid(row=0, column=1)
        Entry(self.create_acc_frame, textvariable=self.n_password, bd=5, font=("", 15)).grid(row=1, column=1)
        Button(self.create_acc_frame, text=" Create Account ", bd=3, font=("", 15), padx=5, pady=5, command=self.new_user).grid(row=2, column=0)
        Button(self.create_acc_frame, text=" Go to login ", bd=3, font=("", 15), padx=5, pady=5, command=self.login_widgets).grid(row=2, column=1)



if __name__ == '__main__':
    screen = Tk()
    screen.title("Login form")

    App(screen)
    screen.mainloop()
