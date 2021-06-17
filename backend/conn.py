# Module Imports
import mariadb
import sys


class DBConnector():
    '''
        Classe para conexão com o banco de dados.
    '''

    def __init__(self):
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user="root",
                password="jdf_abc",
                host="127.0.0.1",
                port=3306,
                database="db_jogodaforca"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        self.cur = conn.cursor()

    def select(self, query):
        self.cur.execute(query)
        response = []
        for _, value in enumerate(self.cur):
            response.append(value)
        return response

    def insert(self, query):
        self.cur.execute(query)