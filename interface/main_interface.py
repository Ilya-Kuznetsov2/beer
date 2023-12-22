import psycopg2
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import types
from functools import partial
from . import window_initializing
from model.beer import Beer

window = window_initializing.window

class Main_interface:
    def __init__(self):

        self.beer_model = Beer()

        self.button_offer = ttk.Button(window, text="Посмотреть меню магазина")
        self.button_full_shops = ttk.Button(window, text="Магазины пива")
        self.button_full_beer = ttk.Button(window, text="Всё пиво")
        self.button_search_bear = ttk.Button(window, text="Поиск конкретного пива")
        self.add_beer = ttk.Button(window, text="Добавить пиво")
        self.update_beer = ttk.Button(window, text="Добавить пиво в магазин или изменить стоимость или рейтинг пива")
        self.button_del_bear = ttk.Button(window, text="Удалить пиво")
        self.button_logout = ttk.Button(window, text="Выйти из аккаунта")

        self.main_dict = {
            'button_offer': self.button_offer,
            'button_full_shops': self.button_full_shops,
            'button_full_beer': self.button_full_beer,
            'button_search_bear': self.button_search_bear,
            'add_beer': self.add_beer,
            'update_beer': self.update_beer,
            'button_del_bear': self.button_del_bear,
            'button_logout': self.button_logout
        }

    def build(self):
        self.main_dict['button_offer'].place(relx=0.4, rely=0.27, relwidth=0.2, relheight=0.04)
        self.main_dict['button_full_shops'].place(relx=0.4, rely=0.33, relwidth=0.2, relheight=0.04)
        self.main_dict['button_full_beer'].place(relx=0.4, rely=0.39, relwidth=0.2, relheight=0.04)
        self.main_dict['button_search_bear'].place(relx=0.4, rely=0.45,relwidth=0.2, relheight=0.04)
        self.main_dict['add_beer'].place(relx=0.4, rely=0.51, relwidth=0.2, relheight=0.04)
        self.main_dict['update_beer'].place(relx=0.35, rely=0.57,relwidth=0.3, relheight=0.04)
        self.main_dict['button_del_bear'].place(relx=0.4, rely=0.63, relwidth=0.2, relheight=0.04)
        self.main_dict['button_logout'].place(relx=0.4, rely=0.80, relwidth=0.2, relheight=0.04)

    def hide(self):
        for widget in self.main_dict.values():
            widget.place_forget()

    def __logout_event(self, aut_inter, event = None):
        self.hide()
        aut_inter.build()

    def __shop_event(self, shop_inter, event = None):
        self.hide()
        shop_inter.build()

    def __offer_event(self, offer_inter, event = None):
        self.hide()
        offer_inter.build()

    def __insert_beer_event(self, beer_insert_inter, event = None):
        self.hide()
        beer_insert_inter.build()

    def __del_beer_event(self, beer_del_inter, event = None):
        self.hide()
        beer_del_inter.build()

    def __update_beer_event(self, beer_update_inter, event = None):
        self.hide()
        beer_update_inter.build()

    def __search_beer_event(self, beer_search_inter, event = None):
        self.hide()
        beer_search_inter.build()

    def __search_all_beer_event(self, event = None):
        table_window = Tk()
        table_window.geometry("1200x600")
        table = self.beer_model.select_all()
        for i in range(len(table)):
            ttk.Button(table_window, text=str(table[i])).grid(row = i, column = 0)

    def bind_commands(self, aut, shop, beer_insert, offer_inter, beer_search_inter, beer_update_inter, beer_del_inter):
        self.button_logout.bind("<Button-1>", partial(self.__logout_event, aut ))
        self.button_full_shops.bind("<Button-1>", partial(self.__shop_event, shop ))
        self.add_beer.bind("<Button-1>", partial(self.__shop_event, beer_insert ))
        self.button_full_beer.bind("<Button-1>", partial(self.__search_all_beer_event))
        self.button_offer.bind("<Button-1>", partial(self.__offer_event, offer_inter ))
        self.button_search_bear.bind("<Button-1>", partial(self.__search_beer_event, beer_search_inter ))
        self.update_beer.bind("<Button-1>", partial(self.__update_beer_event, beer_update_inter ))
        self.button_del_bear.bind("<Button-1>", partial(self.__del_beer_event, beer_del_inter ))
