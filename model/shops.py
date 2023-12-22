import psycopg2
from tkinter import *
from tkinter import ttk
import types
from functools import partial
font=('Times', 14)
style_button = ttk.Style()
style_button.configure('TButton', font = font)

class Shops:

    def __init__(self):
        self.connection = psycopg2.connect(
            database = 'beer',
            user = 'pivozavr',
            password = 'beeeer',
            host = '127.0.0.1',
            port='5432'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS shops (" +
                            "shop varchar(30) PRIMARY KEY," +
                            "address varchar(80) NOT NULL," +
                            "rating real NOT NULL," +
                            "pasport boolean NOT NULL," +
                            "CHECK(rating <=5 AND rating >= 0));"
                            )
        self.connection.commit()


    def __del__(self):
        self.connection.close()

    def select_all(self):
        self.cursor.execute("SELECT * FROM shops")
        table = self.cursor.fetchall()
        return table

    def select_shop(self, shop):
        self.cursor.execute("SELECT * FROM shops WHERE shop=%s", (shop,))
        row = self.cursor.fetchall()
        return row

    def delete_shop(self, shop):
        self.cursor.execute("CALL delete_shop(%s)", (shop,))
        self.connection.commit()

    def insert(self, shop, address, rating, pasport):
        self.cursor.execute("CALL insert_shop(%s, %s, %s, %s)", (shop, address, rating, pasport))
        self.connection.commit()

    def update(self, shop, rating, pasport):
        self.cursor.execute("CALL update_shop(%s, %s, %s)", (shop, rating, pasport))
        self.connection.commit()

