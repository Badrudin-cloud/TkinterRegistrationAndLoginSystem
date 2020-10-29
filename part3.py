# imports
from tkinter import *


class Main:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Useful variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        # Create Widgets
        self.widgets()

    # part3
    def login_widgets(self):
        self.username.set('')
        self.password.set('')
        self.create_acc_frame.pack_forget()
        self.master.title("Login Form")
        self.head['text'] = 'LOGIN'
        self.login_frame.pack()

    def create_acc_widgets(self):
        self.n_username.set('')
        self.n_password.set('')
        self.login_frame.pack_forget()
        self.master.title("Create Account form")
        self.head['text'] = 'Create Account'
        self.create_acc_frame.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.login_frame = Frame(self.master, padx=10, pady=10)
        Label(self.login_frame, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.login_frame, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.login_frame, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.login_frame, text=' Login ', bd=3, font=('', 15), padx=5, pady=5).grid()
        Button(self.login_frame, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.create_acc_widgets).grid(row=2, column=1)
        self.login_frame.pack()

        # part 2
        self.create_acc_frame = Frame(self.master, padx=10, pady=10)
        Label(self.create_acc_frame, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_acc_frame, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.create_acc_frame, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.create_acc_frame, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.create_acc_frame, text='Create Account', bd=3, font=('', 15), padx=5, pady=5).grid()
        Button(self.create_acc_frame, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.login_widgets).grid(row=2,column=1)


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Login Form')
    root.geometry('400x300+300+300')
    Main(root)
    root.mainloop()
