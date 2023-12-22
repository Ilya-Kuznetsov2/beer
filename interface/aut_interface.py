import psycopg2
from model.users import Users
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import types
from functools import partial
from . import window_initializing

window = window_initializing.window
login_and_pass_dict = window_initializing.login_and_pass_dict

font=('Times', 14)

class Aut_interface:

    global login_and_pass_dict

    def __init__(self):

        self.users = Users()

        self.login = StringVar()
        self.password = StringVar()

        self.label_login = ttk.Label(window, text="Логин:", font=font)
        self.entry_login = ttk.Entry(window, textvariable=self.login, font=font)
        self.label_password = ttk.Label(window, text="Пароль:", font=font)
        self.entry_password = ttk.Entry(window, show='*', textvariable=self.password, font=font)
        self.button_entire = ttk.Button(text="Войти")
        self.button_reg = ttk.Button(text="Регистрация")

        self.aut_dict = {
            'label_login': self.label_login,
            'entry_login': self.entry_login,
            'label_password': self.label_password,
            'entry_password': self.entry_password,
            'button_entire': self.button_entire,
            'button_reg': self.button_reg
        }

    def __reg_event(self, reg_interface, event = None):
        self.hide()
        reg_interface.build()

    def __entire_event(self, main_interface, event = None):
        if self.users.get_pass(self.login.get())  and self.users.get_pass(self.login.get())[0][0] == self.password.get():
            self.hide()
            main_interface.build()
        else:
            messagebox.showerror("Ошибка входа", "Введен неверный логин или пароль")

    def bind_commands(self, reg, main_interface):
        self.button_reg.bind("<Button-1>", partial(self.__reg_event, reg ))
        self.button_entire.bind("<Button-1>", partial(self.__entire_event, main_interface ))

    def build(self):
        self.aut_dict['label_login'].place(relx=0.36, rely=0.3, relheight=0.03)
        self.aut_dict['entry_login'].place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.03)
        self.aut_dict['label_password'].place(relx=0.36, rely=0.38, relheight=0.03)
        self.aut_dict['entry_password'].place(relx=0.4, rely=0.38, relwidth=0.2, relheight=0.03)
        self.aut_dict['button_entire'].place(relx=0.38, rely=0.45, relwidth=0.1, relheight=0.03)
        self.aut_dict['button_reg'].place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.03)

    def hide(self):
        for widget in self.aut_dict.values():
            widget.place_forget()
