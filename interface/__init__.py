from tkinter import ttk
from . import window_initializing
from . import aut_interface
from . import reg_interface
from . import main_interface
from . import shop_interface
from . import beer_interfaces

aut = aut_interface.Aut_interface()
reg = reg_interface.Reg_interface()
main_inter = main_interface.Main_interface()
shop_inter = shop_interface.Shop_interface()
beer_insert_inter = beer_interfaces.Beer_insert_interface()
beer_del_inter = beer_interfaces.Beer_del_interface()
beer_update_inter = beer_interfaces.Beer_update_interface()
beer_search_inter = beer_interfaces.Beer_search_interface()
offer_inter = beer_interfaces.Offer_interface()




aut.build()

aut.bind_commands(reg, main_inter)
reg.bind_commands(aut)
main_inter.bind_commands(aut, shop_inter, beer_insert_inter, offer_inter, beer_search_inter, beer_update_inter, beer_del_inter)
shop_inter.bind_commands(main_inter)
beer_insert_inter.bind_commands(main_inter)
beer_del_inter.bind_commands(main_inter)
beer_update_inter.bind_commands(main_inter)
beer_search_inter.bind_commands(main_inter)
offer_inter.bind_commands(main_inter)


font=('Times', 14)

style_button = ttk.Style()
style_button.configure('TButton', font = font)