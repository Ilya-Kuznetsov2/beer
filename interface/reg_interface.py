import psycopg2
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import types
from functools import partial
from . import window_initializing
from model.users import Users

window = window_initializing.window

font=('Times', 14)

class Reg_interface:

    global login_and_pass_dict

    def __init__(self):

        self.users = Users()

        self.login = StringVar()
        self.password = StringVar()
        self.re_password = StringVar()

        self.label_login = ttk.Label(window, text="Логин:", font=font)
        self.entry_login = ttk.Entry(window, textvariable=self.login, font=font)
        self.label_password = ttk.Label(window, text="Пароль:", font=font)
        self.entry_password = ttk.Entry(window, show='*', textvariable=self.password, font=font)
        self.button_reg = ttk.Button(text="Зарегистрироваться")
        self.label_re_password = ttk.Label(window, text="Повторите пароль:", font=font)
        self.entry_re_password = ttk.Entry(window, show='*', textvariable=self.re_password, font=font)
        self.button_aut_back = ttk.Button(text="Уже есть аккаунт")

        self.reg_dict = {
            'label_login': self.label_login,
            'entry_reg_login': self.entry_login,
            'label_password': self.label_password,
            'entry_reg_password': self.entry_password,
            'button_reg': self.button_reg,
            'label_re_password': self.label_re_password,
            'entry_re_password': self.entry_re_password,
            'button_aut_back': self.button_aut_back
        }


    def __aut_event(self, aut, event = None):
        self.hide()
        aut.build()

    def __create_acc_event(self, aut, event = None):

        if self.users.get_pass(self.login.get()):
            messagebox.showerror("Ошибка регистрации", "Пользователь с таким именем уже существует")
        elif self.password.get()!=self.re_password.get():
            messagebox.showerror("Ошибка регистрации", "Пароли не совпадают")
        else:
            self.users.insert(self.login.get(), self.password.get())
            self.hide()
            aut.build()

    def bind_commands(self, aut):
        self.button_aut_back.bind("<Button-1>", partial(self.__aut_event, aut ))
        self.button_reg.bind("<Button-1>", partial(self.__create_acc_event, aut ))

    def build(self):
        self.reg_dict['label_login'].place(relx=0.36, rely=0.25, relheight=0.03)
        self.reg_dict['entry_reg_login'].place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.03)
        self.reg_dict['label_password'].place(relx=0.36, rely=0.33, relheight=0.03)
        self.reg_dict['entry_reg_password'].place(relx=0.4, rely=0.33, relwidth=0.2, relheight=0.03)
        self.reg_dict['label_re_password'].place(relx=0.3, rely=0.41, relheight=0.03)
        self.reg_dict['entry_re_password'].place(relx=0.4, rely=0.41, relwidth=0.2, relheight=0.03)
        self.reg_dict['button_reg'].place(relx=0.38, rely=0.48, relwidth=0.1, relheight=0.03)
        self.reg_dict['button_aut_back'].place(relx=0.5, rely=0.48, relwidth=0.2, relheight=0.03)

    def hide(self):
        for widget in self.reg_dict.values():
            widget.place_forget()
