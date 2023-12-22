from entities.technology import Technology
import mysql.connector


class DbTechnology:
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._table_name = 'technology'
        self._index_name = 'technology_index'

    def create_table(self):
        try:
            request = f'CREATE TABLE {self._table_name}(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Table already exists !')

    def drop_table(self):
        try:
            request = f'DROP TABLE IF EXISTS {self._table_name} '
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Table does not exist !')

    def create_index(self):
        try:
            request = f'CREATE INDEX {self._index_name} ON {self._table_name} (id)'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Index already exists !')

    def drop_index(self):
        try:
            request = f'DROP INDEX IF EXISTS {self._index_name} ON {self._table_name} '
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('Index does not exist !')

    def insert_technology(self, technology):
        try:
            request = f'INSERT INTO {self._table_name} (name) VALUES (%s)'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (technology.name,))
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('An error hos occurred !')

    def select_technology(self):
        try:
            request = f'SELECT id,name FROM {self._table_name} ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            rows = cursor.fetchall()
            technologies = []
            # Displaying fetched rows
            for row in rows:
                technologies.append(Technology(row[0], row[1]))
            self._db_connection.close_connection()
            return technologies
        except mysql.connector.Error:
            print('Could not fetch technologies !')

    def select_one_technology_by_id(self, technology_id):
        try:
            request = f'SELECT * FROM {self._table_name} WHERE id = %s ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (technology_id,))
            row = cursor.fetchone()
            technology = Technology(row[0], row[1])
            self._db_connection.close_connection()
            return technology
        except mysql.connector.Error:
            print(f'Could not fetch technology {technology_id} !')

    def select_one_technology_by_name(self, technology_name):
        try:
            request = f'SELECT * FROM {self._table_name} WHERE name = %s ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (technology_name,))
            row = cursor.fetchone()
            technology = Technology(row[0], row[1])
            self._db_connection.close_connection()
            return technology
        except mysql.connector.Error:
            print(f'Could not fetch technology {technology_name} !')
