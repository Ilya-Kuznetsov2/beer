import psycopg2


class Beer:

    def __init__(self):
        self.connection = psycopg2.connect(
            database='beer',
            user='pivozavr',
            password='beeeer',
            host='127.0.0.1',
            port='5432'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS beer (" +
                            "name varchar(30) PRIMARY KEY," +
                            "type varchar(30) NOT NULL," +
                            "rating real NOT NULL DEFAULT 0,"+
                            "shop_count integer NOT NULL DEFAULT 0);"
                            )
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def select_all(self):
        self.cursor.execute("SELECT * FROM beer")
        table = self.cursor.fetchall()
        return table

    def select_beer(self, name):
        self.cursor.execute("SELECT * FROM beer WHERE name=%s", (name,))
        row = self.cursor.fetchall()
        return row

    def select_light(self):
        self.cursor.execute("SELECT * FROM beer WHERE type='светлое'")
        table = self.cursor.fetchall()
        return table

    def select_black(self):
        self.cursor.execute("SELECT * FROM beer WHERE type='темное'")
        table = self.cursor.fetchall()
        return table

    def delete_beer(self, name):
        self.cursor.execute("CALL delete_beer(%s)", (name,))
        self.connection.commit()

    def insert(self, name, type, rating):
        self.cursor.execute("CALL insert_beer(%s, %s, %s, %s)", (name, type, rating, 0))
        self.connection.commit()

