import psycopg2


class Users:

    def __init__(self):
        self.connection = psycopg2.connect(
            database='beer',
            user='postgres',
            password='12345',
            host='127.0.0.1',
            port='5432'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (" +
                            "login varchar(40) PRIMARY KEY," +
                            "password varchar(40) NOT NULL)"
                            )
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def get_pass(self, login):
        self.cursor.execute("SELECT password FROM users WHERE login=%s", (login,))
        row = self.cursor.fetchall()
        return row

    def insert(self, login, password):
        self.cursor.execute("CALL insert_user(%s, %s)", (login, password))
        self.connection.commit()

