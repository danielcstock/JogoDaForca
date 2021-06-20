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
            self.conn = mariadb.connect(
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
        self.cur = self.conn.cursor()

    def executeQuery(self, qry):
        self.cur.execute(qry)
        response = []
        for _, value in enumerate(self.cur):
            response.append(value)
        return response

    def select(self, table, column, value):
        qry = "SELECT * FROM " + table + " WHERE " + column + " = " + value
        self.cur.execute(qry)
        response = []
        for _, value in enumerate(self.cur):
            response.append(value)
        return response

    def selectValue(self, table, columnResult, column, value):
        qry = "SELECT " + columnResult + " FROM " + table + " WHERE " + column + " = " + value
        self.cur.execute(qry)
        response = []
        for _, value in enumerate(self.cur):
            response.append(value)
        return response

    def count(self, table, column):
        qry = "SELECT COUNT("+ column +") FROM " + table
        self.cur.execute(qry)
        response = []
        for _, value in enumerate(self.cur):
            response.append(value)
        return response

    def insert(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def update(self, table, column, value, id):
        qry = "UPDATE " + table + " SET " + column + " = " + str(value) + " WHERE id = " + str(id)
        self.cur.execute(qry)
        self.conn.commit()