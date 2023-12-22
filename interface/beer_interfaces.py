from . import window_initializing
from model.beer import Beer
from model.shops import Shops
from model.goods import Goods
from tkinter import *
from tkinter import ttk, messagebox
from functools import partial

window = window_initializing.window

font=('Times', 14)


class Beer_insert_interface():

    def __init__(self):

        self.model_goods = Goods()
        self.model_beer = Beer()

        self.beer_to_insert = StringVar()
        self.type = StringVar()


        self.label_insert = ttk.Label(window, text="Название пива:", font=font)
        self.entry_insert = ttk.Entry(window, textvariable=self.beer_to_insert, font=font)
        self.label_type = ttk.Label(window, text="Светлое или темное:", font=font)
        self.entry_type = ttk.Entry(window, textvariable=self.type, font=font)
        self.button_insert = ttk.Button(window, text="Добавить")
        self.button_back = ttk.Button(window, text="Назад")

        self.shop_dict = {
            'label_insert': self.label_insert,
            'entry_insert': self.entry_insert,
            'label_type': self.label_type,
            'entry_type': self.entry_type,
            'button_back': self.button_back,
            'button_insert': self.button_insert
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event = None):
        self.hide()
        main_inter.build()

    def __insert_event(self, event = None):

        if not(self.model_beer.select_beer(self.beer_to_insert.get())):
            self.model_beer.insert(self.beer_to_insert.get(), self.type.get(), 0)
            self.beer_to_insert.set("")
            self.type.set("")
        else:
            messagebox.showerror("Ошибка добавления", "Пиво с таким названием уже существует")


    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter ))
        self.button_insert.bind("<Button-1>", partial(self.__insert_event))

    def build(self):

        self.shop_dict['label_insert'].place(relx=0.4, rely=0.3, relheight=0.04)
        self.shop_dict['entry_insert'].place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.04)
        self.shop_dict['label_type'].place(relx=0.4, rely=0.43, relheight=0.04)
        self.shop_dict['entry_type'].place(relx=0.4, rely=0.48, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_insert'].place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.04)


class Beer_del_interface:

    def __init__(self):

        self.model_beer = Beer()

        self.beer = StringVar()

        self.label_beer = ttk.Label(window, text="Название пива:", font=font)
        self.entry_beer = ttk.Entry(window, textvariable=self.beer, font=font)
        self.button_del = ttk.Button(window, text="Удалить")
        self.button_back = ttk.Button(window, text="Назад")

        self.shop_dict = {
            'label_beer': self.label_beer,
            'entry_beer': self.entry_beer,
            'button_del': self.button_del,
            'button_back': self.button_back
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event = None):
        self.hide()
        main_inter.build()

    def __del_event(self, event = None):
        self.model_beer.delete_beer(self.beer.get())
        self.beer.set("")

    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter ))
        self.button_del.bind("<Button-1>", partial(self.__del_event))

    def build(self):

        self.shop_dict['label_beer'].place(relx=0.4, rely=0.4, relheight=0.04)
        self.shop_dict['entry_beer'].place(relx=0.4, rely=0.46, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_del'].place(relx=0.4, rely=0.56, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)


class Beer_update_interface:

    def __init__(self):

        self.model_beer=Beer()
        self.model_goods=Goods()
        self.model_shop = Shops()

        self.shop = StringVar()
        self.beer = StringVar()
        self.rating = StringVar()
        self.price = StringVar()

        self.label_shop = ttk.Label(window, text="Название магазина:", font=font)
        self.entry_shop = ttk.Entry(window, textvariable=self.shop, font=font)
        self.label_beer = ttk.Label(window, text="Название пива:", font=font)
        self.entry_beer = ttk.Entry(window, textvariable=self.beer, font=font)
        self.label_rate = ttk.Label(window, text="Рейтинг:", font=font)
        self.entry_rate = ttk.Entry(window, textvariable=self.rating, font=font)
        self.label_price = ttk.Label(window, text="Цена:", font=font)
        self.entry_price = ttk.Entry(window, textvariable=self.price, font=font)
        self.button_up = ttk.Button(window, text="Обновить")
        self.button_back = ttk.Button(window, text="Назад")

        self.shop_dict = {
            'label_shop': self.label_shop,
            'entry_shop': self.entry_shop,
            'label_beer': self.label_beer,
            'entry_beer': self.entry_beer,
            'label_rate': self.label_rate,
            'entry_rate': self.entry_rate,
            'label_price': self.label_price,
            'entry_price': self.entry_price,
            'button_up': self.button_up,
            'button_back': self.button_back
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event = None):
        self.hide()
        main_inter.build()

    def __update_event(self, event = None):

        if self.model_beer.select_beer(self.beer.get()) and self.model_shop.select_shop(self.shop.get()):
            if self.model_goods.select_good(self.beer.get(), self.shop.get()):
                self.model_goods.update(self.beer.get(), self.shop.get(), self.price.get(), self.rating.get())
            else:
                self.model_goods.insert(self.beer.get(), self.shop.get(), self.price.get(), self.rating.get())
        else:
                messagebox.showerror("Ошибка добавления", "Такого пива или магазина не существует")

    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter ))
        self.button_up.bind("<Button-1>", partial(self.__update_event))

    def build(self):

        self.shop_dict['label_shop'].place(relx=0.4, rely=0.3, relheight=0.04)
        self.shop_dict['entry_shop'].place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.04)
        self.shop_dict['label_beer'].place(relx=0.4, rely=0.42, relheight=0.04)
        self.shop_dict['entry_beer'].place(relx=0.4, rely=0.47, relwidth=0.2, relheight=0.04)
        self.shop_dict['label_rate'].place(relx=0.35, rely=0.53, relheight=0.04)
        self.shop_dict['entry_rate'].place(relx=0.35, rely=0.58, relwidth=0.1, relheight=0.04)
        self.shop_dict['label_price'].place(relx=0.55, rely=0.53, relheight=0.04)
        self.shop_dict['entry_price'].place(relx=0.55, rely=0.58, relwidth=0.1, relheight=0.04)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_up'].place(relx=0.4, rely=0.68, relwidth=0.2, relheight=0.04)


class Beer_search_interface:
    def __init__(self):

        self.model_beer = Beer()

        self.beer = StringVar()

        self.label_beer = ttk.Label(window, text="Название пива:", font=font)
        self.entry_beer = ttk.Entry(window, textvariable=self.beer, font=font)
        self.button_show = ttk.Button(window, text="Найти пиво")
        self.button_back = ttk.Button(window, text="Назад")
        self.button_light = ttk.Button(window, text="Показать светлое пиво")
        self.button_dark = ttk.Button(window, text="Показать темное пиво")

        self.shop_dict = {
            'label_beer': self.label_beer,
            'entry_beer': self.entry_beer,
            'button_show': self.button_show,
            'button_back': self.button_back,
            'button_light': self.button_light,
            'button_dark': self.button_dark,
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event=None):
        self.hide()
        main_inter.build()

    def __dark_event(self, event=None):
        table = self.model_beer.select_black()
        table_window = Tk()
        table_window.geometry("1200x600")

        for i in range(len(table)):
            ttk.Label(table_window, text=str(table[i]), font=font).grid(row=i, column=0)

    def __light_event(self, event=None):
        table = self.model_beer.select_light()
        table_window = Tk()
        table_window.geometry("1200x600")

        for i in range(len(table)):
            ttk.Label(table_window, text=str(table[i]), font=font).grid(row=i, column=0)

    def __show_event(self, event=None):
        row = self.model_beer.select_beer(self.beer.get())
        table_window = Tk()
        table_window.geometry("200x200")
        if row:
            ttk.Button(table_window, text='Пиво:'+str(row[0][0])).grid(row = 0, column = 0)
            ttk.Button(table_window, text='Тип:'+str(row[0][1])).grid(row = 1, column = 0)
            ttk.Button(table_window, text='Рейтинг:'+str(row[0][2])).grid(row = 2, column = 0)
            ttk.Button(table_window, text='Количество магазинов:'+str(row[0][3])).grid(row = 3, column = 0)

    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter))
        self.button_show.bind("<Button-1>", partial(self.__show_event))
        self.button_light.bind("<Button-1>", partial(self.__light_event))
        self.button_dark.bind("<Button-1>", partial(self.__dark_event))

    def build(self):
        self.shop_dict['label_beer'].place(relx=0.4, rely=0.4, relheight=0.04)
        self.shop_dict['entry_beer'].place(relx=0.4, rely=0.46, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_show'].place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_light'].place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_dark'].place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.04)


class Offer_interface:

    def __init__(self):

        self.model_goods = Goods()

        self.shop = StringVar()

        self.label_shop = ttk.Label(window, text="Название магазина:", font=font)
        self.entry_shop = ttk.Entry(window, textvariable=self.shop, font=font)
        self.button_show = ttk.Button(window, text="Показать меню")
        self.button_back = ttk.Button(window, text="Назад")

        self.shop_dict = {
            'label_shop': self.label_shop,
            'entry_shop': self.entry_shop,
            'button_show': self.button_show,
            'button_back': self.button_back
        }

    def hide(self):
        for widget in self.shop_dict.values():
            widget.place_forget()

    def __back_event(self, main_inter, event=None):
        self.hide()
        main_inter.build()

    def __show_event(self, event=None):
        table = self.model_goods.select_shop(self.shop.get())
        table_window = Tk()
        table_window.geometry("1200x600")

        for i in range(len(table)):
            ttk.Label(table_window, text=str(table[i]), font=font).grid(row=i, column=0)

    def bind_commands(self, main_inter):
        self.button_back.bind("<Button-1>", partial(self.__back_event, main_inter))
        self.button_show.bind("<Button-1>", partial(self.__show_event))

    def build(self):
        self.shop_dict['label_shop'].place(relx=0.4, rely=0.4, relheight=0.04)
        self.shop_dict['entry_shop'].place(relx=0.4, rely=0.46, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_show'].place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.04)
        self.shop_dict['button_back'].place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.04)

