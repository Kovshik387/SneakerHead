import tkinter as Tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

import logic

import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.label_purchase = None
        self.size_box = None
        self.size_text = CTk.StringVar()
        self.brand_box = None
        self.model_text = CTk.StringVar()

        self.button = None
        self.tree_buy = None
        self.tree = None
        self.geometry('760x540+900+200')
        self.title('Password')
        self.resizable(False, False)
        self.iconbitmap(default="Resources/Images/sneakerNew.ico")

        self.logo = CTk.CTkLabel(master=self, text='Добро пожаловать')
        self.logo.grid(row=0, column=0, columnspan=2)

        self.create_three_view()
        self.show_buttons()
        self.create_buy_view()

    def create_three_view(self):
        columns = 'Артикул', 'Бренд', 'Модель', 'Расцветка', 'Размер', 'Количество на складе'
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.heading('Артикул', text='Артикул')
        self.tree.heading('Бренд', text='Бренд')
        self.tree.heading('Модель', text='Модель')
        self.tree.heading('Расцветка', text='Расцветка')
        self.tree.heading('Размер', text='Размер')
        self.tree.heading('Количество на складе', text='Количество на складе')

        self.tree.column('Артикул', width=60, anchor=Tk.W)
        self.tree.column('Бренд', width=50, anchor=Tk.W)
        self.tree.column('Модель', width=100, anchor=Tk.W)
        self.tree.column('Расцветка', width=70, anchor=Tk.W)
        self.tree.column('Размер', width=50, anchor=Tk.W)
        self.tree.column('Количество на складе', width=130)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=1, rowspan=3, column=0, columnspan=2, sticky=Tk.NSEW)

        scrollbar = ttk.Scrollbar(self, orient=Tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, rowspan=3, column=2, sticky='ns')

        for item in logic.sneakers:
            self.tree.insert('', Tk.END, values=item.display_info())

    def update_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in logic.sneakers:
            self.tree.insert('', Tk.END, values=item.display_info())

    def create_buy_view(self):
        columns = 'Артикул', 'Бренд', 'Модель', 'Расцветка', 'Размер', 'Количество на складе'
        self.tree_buy = ttk.Treeview(self, columns=columns, show='headings')

        self.tree_buy.heading('Артикул', text='Артикул')
        self.tree_buy.heading('Бренд', text='Бренд')
        self.tree_buy.heading('Модель', text='Модель')
        self.tree_buy.heading('Расцветка', text='Расцветка')
        self.tree_buy.heading('Размер', text='Размер')
        self.tree_buy.heading('Количество на складе', text='Куплено')

        self.tree_buy.column('Артикул', width=60, anchor=Tk.W)
        self.tree_buy.column('Бренд', width=50, anchor=Tk.W)
        self.tree_buy.column('Модель', width=100, anchor=Tk.W)
        self.tree_buy.column('Расцветка', width=70, anchor=Tk.W)
        self.tree_buy.column('Размер', width=50, anchor=Tk.W)
        self.tree_buy.column('Количество на складе', width=130)

        self.label_purchase = CTk.CTkLabel(text='Купленные товары', master=self)
        self.label_purchase.grid(row=4, column=0, columnspan=2)
        self.tree_buy.grid(row=5, column=0, columnspan=2, sticky=Tk.NSEW)

        scrollbar = ttk.Scrollbar(self, orient=Tk.VERTICAL, command=self.tree.yview)
        self.tree_buy.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=5, column=2, sticky='ns')

        for item in logic.buy_sneakers:
            self.tree_buy.insert('', Tk.END, values=item.display_info())

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)

            record = item['values']

            if record[5] == 0:
                showerror(title='Информация', message='Товара нет в наличии')
                return

            for sub_item in logic.sneakers:
                if sub_item.id_item == record[0]:
                    sub_item.count -= 1

            record[5] = 1
            self.tree_buy.insert('', Tk.END, values=record)
            self.update_view()
            showinfo(title='Информация', message='Товара успешно куплен')

    def show_buttons(self):
        self.button = CTk.CTkButton(self, text='Найти', command=self.search_button)
        self.button.grid(row=3, rowspan=2, column=3, padx=30)

        self.brand_box = CTk.CTkEntry(self, placeholder_text='Бренд', textvariable=self.model_text)
        self.brand_box.grid(row=2, rowspan=2, column=3)

        self.size_box = CTk.CTkEntry(self, placeholder_text='Размер', textvariable=self.size_text)
        self.size_box.grid(row=1, rowspan=2, column=3)

    def search_button(self):
        logic.sneakers = logic.search_in_sneakers(self.model_text, self.size_text)
        self.update_view()


if __name__ == '__main__':
    app = App()
    app.mainloop()
