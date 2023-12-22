import psycopg2
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import types
from functools import partial

def change_screen(window, event=None):

    if window.attributes("-fullscreen"):
        window.attributes("-fullscreen", False)
    else:
        window.attributes("-fullscreen", True)

window = Tk()

window.title("Пиво")
window.geometry(str(1920)+"x"+str(1024))
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='resourses/beer.png'))
window.attributes("-fullscreen", True)

window.change_screen = types.MethodType(change_screen, window)

img = Image.open('./resourses/full_screen.png')
bg_img = Image.open('./resourses/bg.png')

img = ImageTk.PhotoImage(img)
bg_img = ImageTk.PhotoImage(bg_img)

bg=Label(window, image = bg_img)
bg.place(x = 0, y = 0)
button_screen=ttk.Label(text="Смена режима", image = img)
button_screen.bind('<Button-1>', window.change_screen)
button_screen.place(relx = 0.95, rely = 0, relwidth = 0.1, relheight=0.1)


button_exit=ttk.Button(text="Выход", command=window.quit)
button_exit.place(relx = 0.85, rely = 0.9, relwidth = 0.1, relheight=0.03)

login_and_pass_dict = {
    'Пригожин': 'вагнер'
}
