import tkinter

import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('300x300+900+200')
        self.title('Password')
        self.resizable(False, False)
        self.iconbitmap(default="Resources/Images/sneakerNew.ico")

        self.logo = CTk.CTkLabel(master=self, text='Добро пожаловать')
        self.logo.grid(row=0, column=1)

        self.listBox = tkinter.Listbox(listvariable=['xuy','xaxa'])
        self.listBox.grid(row=1, column=0)

if __name__ == '__main__':
    app = App()
    app.mainloop()
