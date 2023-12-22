import mysql.connector
import xml.etree.ElementTree as ET
import os


class DbConnection:
    def __init__(self):
        tree = ET.parse('db_configuration.xml')
        root = tree.getroot()
        self._host = os.getenv('DB_HOST', f'{root.find('host').text}')
        self._database = os.getenv('DB_DATABASE', f'{root.find('database').text}')
        self._user = os.getenv('DB_USER', f'{root.find('user').text}')
        self._password = os.getenv('DB_PASSWORD', f'{root.find('password').text}')
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def get_connection(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                database=self._database,
                user=self._user,
                password=self._password
            )
        except mysql.connector.Error:
            print('Could connect to the database !')

    def is_connected(self):
        return self._connection.is_connected()

    def close_connection(self):
        self._connection.close()

    def create_cursor(self):
        return self._connection.cursor()
