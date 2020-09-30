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
        Button(self.login_frame, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5).grid(row=2,column=1)
        self.login_frame.pack()


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Login Form')
    # root.geometry('400x350+300+300')
    Main(root)
    root.mainloop()
