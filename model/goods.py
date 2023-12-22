import psycopg2


class Goods:

    def __init__(self):
        self.connection = psycopg2.connect(
            database='beer',
            user='pivozavr',
            password='beeeer',
            host='127.0.0.1',
            port='5432'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS goods (" +
                            "beer varchar(30) NOT NULL," +
                            "shop varchar(30) NOT NULL," +
                            "price real NOT NULL," +
                            "rating real NOT NULL,"+
                            "PRIMARY KEY (beer, shop),"+
                            "FOREIGN KEY (beer) REFERENCES beer (name) ON DELETE CASCADE,"+
                            "FOREIGN KEY (shop) REFERENCES shops (shop) ON DELETE CASCADE"+
                            ");"
                            )
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def select_all(self):
        self.cursor.execute("SELECT * FROM goods")
        table = self.cursor.fetchall()
        return table

    def select_shop(self, shop):
        self.cursor.execute("SELECT beer, price, rating FROM goods WHERE shop=%s", (shop,))
        row = self.cursor.fetchall()
        return row

    def select_good(self, beer, shop):
        self.cursor.execute("SELECT beer, shop, price, rating FROM goods WHERE shop=%s and beer=%s", (shop, beer))
        row = self.cursor.fetchall()
        return row


    def delete_good(self, beer, shop):
        self.cursor.execute("CALL delete_good(%s, %s)", (beer, shop))
        self.connection.commit()

    def insert(self, beer, shop, price, rating):
        self.cursor.execute("CALL insert_good(%s, %s, %s, %s)", (beer, shop, price, rating))
        self.connection.commit()

    def update(self, beer, shop, price, rating):
        self.cursor.execute("CALL update_good(%s, %s, %s, %s)", (beer, shop, price, rating))
        self.connection.commit()
