from . import window_initializing
from model.shops import Shops
from tkinter import *
from tkinter import ttk
from functools import partial

window = window_initializing.window

font=('Times', 14)

class Shop_interface():

    def __init__(self):

        self.model_shops = Shops()

        self.shop_to_search = StringVar()
        self.shop_to_del = StringVar()
        self.shop_to_update = StringVar()
        self.shop_to_insert = StringVar()
        self.address = StringVar()
        self.rating = StringVar()
        self.pasport = StringVar()
        self.re_rating = StringVar()
        self.re_pasport = StringVar()


        self.button_full_shops = ttk.Button(window, text="Показать все магазины")
        self.label_search = ttk.Label(window, text="Поиск конкретного магазина:", font=font)
        self.button_search = ttk.Button(window, text="Найти")
        self.entry_search = ttk.Entry(window, textvariable=self.shop_to_search, font=font)
        self.label_insert = ttk.Label(window, text="Добавить магазин:", font=font)
        self.entry_insert = ttk.Entry(window, textvariable=self.shop_to_insert, font=font)
        self.label_rating = ttk.Label(window, text="Рейтинг:", font=font)
        self.entry_rating = ttk.Entry(window, textvariable=self.rating, font=font)
        self.label_pasport = ttk.Label(window, text="Требуют ли паспорт:", font=font)
        self.entry_pasport = ttk.Entry(window, textvariable=self.pasport, font=font)
        self.label_address = ttk.Label(window, text="Адрес:", font=font)
        self.entry_address = ttk.Entry(window, textvariable=self.address, font=font)
        self.label_del = ttk.Label(window, text="Удалить магазин:", font=font)
        self.entry_del = ttk.Entry(window, textvariable=self.shop_to_del, font=font)
        self.label_update = ttk.Label(window, text="Обновить данные о магазине:", font=font)
        self.entry_update = ttk.Entry(window, textvariable=self.shop_to_update, font=font)
        self.label_re_rating = ttk.Label(window, text="Новый рейтинг", font=font)
        self.entry_re_rating = ttk.Entry(window, textvariable=self.re_rating, font=font)
        self.label_re_pasport = ttk.Label(window, text="Требуют ли паспорт сейчас", font=font)
        self.entry_re_pasport = ttk.Entry(window, textvariable=self.re_pasport, font=font)
        self.button_del = ttk.Button(window, text="Удалить")
        self.button_update = ttk.Button(window, text="Обновить")
        self.button_insert = ttk.Button(window, text="Добавить")
        self.button_back = ttk.Button(window, text="Назад")

        self.shop_dict = {
            'button_full_shops': self.button_full_shops,
            'label_search': self.label_search,
            'entry_search': self.entry_search,
            'button_search': self.button_search,
            'label_insert': self.label_insert,
            'entry_insert': self.entry_insert,
            'label_rating': self.label_rating,
            'entry_rating': self.entry_rating,
            'label_pasport': self.label_pasport,
            'entry_pasport': self.entry_pasport,
            'label_address': self.label_address,
            'entry_address': self.entry_address,
            'label_del': self.label_del,
            'entry_del': self.entry_del,
            'label_update': self.label_update,
            'entry_update': self.entry_update,
            'label_re_rating': self.label_re_rating,
            'entry_re_rating': self.entry_re_rating,
            'label_re_pasport': self.label_re_pasport,
            'entry_re_pasport': self.entry_re_pasport,
            'button_del': self.button_del,
            'button_update': self.button_update,
            'button_back': self.button_back,
            'button_insert': self.button_insert
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event = None):
        self.hide()
        main_inter.build()

    def __search_event(self, event = None):
        row = self.model_shops.select_shop(self.shop_to_search.get())
        self.shop_to_search.set("")

    def __select_all_event(self, event = None):
        table_window = Tk()
        table_window.geometry("1200x600")
        table = self.model_shops.select_all()
        for i in range(len(table)):
            ttk.Label(table_window, text=str(table[i]), font=font).grid(row = i, column = 0)

    def __update_event(self, event = None):
        self.model_shops.update(self.shop_to_update.get(), self.re_rating.get(), self.re_pasport.get())
        self.shop_to_update.set("")
        self.re_rating.set("")
        self.re_pasport.set("")

    def __insert_event(self, event = None):
        self.model_shops.insert(self.shop_to_insert.get(), self.address.get(), self.rating.get(), self.pasport.get())
        self.shop_to_insert.set("")
        self.address.set("")
        self.rating.set("")
        self.pasport.set("")

    def __del_event(self, event = None):
        self.model_shops.delete_shop(self.shop_to_del.get())
        self.shop_to_del.set("")

    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter ))
        self.button_insert.bind("<Button-1>", partial(self.__insert_event))
        self.button_del.bind("<Button-1>", partial(self.__del_event))
        self.button_search.bind("<Button-1>", partial(self.__search_event))
        self.button_update.bind("<Button-1>", partial(self.__update_event))
        self.button_full_shops.bind("<Button-1>", partial(self.__select_all_event))

    def build(self):
        self.shop_dict['button_full_shops'].place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.03)
        self.shop_dict['label_search'].place(relx=0.4, rely=0.15, relheight=0.03)
        self.shop_dict['entry_search'].place(relx=0.4, rely=0.19, relwidth=0.2, relheight=0.03)
        self.shop_dict['button_search'].place(relx=0.4, rely=0.24, relwidth=0.2, relheight=0.03)
        self.shop_dict['label_insert'].place(relx=0.4, rely=0.29, relheight=0.03)
        self.shop_dict['entry_insert'].place(relx=0.4, rely=0.33, relwidth=0.2, relheight=0.03)
        self.shop_dict['label_address'].place(relx=0.4, rely=0.38, relheight=0.03)
        self.shop_dict['entry_address'].place(relx=0.3, rely=0.42, relwidth=0.4, relheight=0.03)
        self.shop_dict['label_rating'].place(relx=0.35, rely=0.46, relheight=0.03)
        self.shop_dict['entry_rating'].place(relx=0.35, rely=0.50, relwidth=0.1, relheight=0.03)
        self.shop_dict['label_pasport'].place(relx=0.55, rely=0.46, relheight=0.03)
        self.shop_dict['entry_pasport'].place(relx=0.55, rely=0.50, relwidth=0.1, relheight=0.03)
        self.shop_dict['label_del'].place(relx=0.4, rely=0.60, relheight=0.03)
        self.shop_dict['entry_del'].place(relx=0.4, rely=0.64, relwidth=0.2, relheight=0.03)
        self.shop_dict['label_update'].place(relx=0.4, rely=0.75, relheight=0.03)
        self.shop_dict['entry_update'].place(relx=0.4, rely=0.79, relwidth=0.2, relheight=0.03)
        self.shop_dict['label_re_rating'].place(relx=0.35, rely=0.82, relheight=0.03)
        self.shop_dict['entry_re_rating'].place(relx=0.35, rely=0.86, relwidth=0.1, relheight=0.03)
        self.shop_dict['label_re_pasport'].place(relx=0.55, rely=0.82, relheight=0.03)
        self.shop_dict['entry_re_pasport'].place(relx=0.55, rely=0.86, relwidth=0.1, relheight=0.03)
        self.shop_dict['button_del'].place(relx=0.4, rely=0.70, relwidth=0.2, relheight=0.03)
        self.shop_dict['button_update'].place(relx=0.4, rely=0.90, relwidth=0.2, relheight=0.03)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.95, relwidth=0.2, relheight=0.03)
        self.shop_dict['button_insert'].place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.03)
