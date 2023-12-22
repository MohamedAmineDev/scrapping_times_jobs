from entities.job import Job
from entities.technology import Technology
import mysql.connector


class DbJob:
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._table_name = 'job'
        self._index_name = 'job_index'

    def create_table(self):
        try:
            request = (f'CREATE TABLE {self._table_name}(id INT AUTO_INCREMENT PRIMARY KEY,unique_id VARCHAR(255) '
                       f'UNIQUE,experience VARCHAR(255),skills VARCHAR(2000),languages VARCHAR(2000),entreprise_name '
                       f'VARCHAR(255),date VARCHAR(255),address VARCHAR(255),contract_type VARCHAR(255), '
                       f'qualification VARCHAR(255), technology_id INT,'
                       f'title VARCHAR(255),'
                       f'FOREIGN KEY (technology_id) REFERENCES '
                       f'technology(id))')
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

    def insert_offer(self, job):
        try:
            request = (f'INSERT INTO {self._table_name} (unique_id,experience,skills,languages,entreprise_name,date,'
                       f'address,contract_type,qualification,technology_id,title) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'
                       f'%s,%s)')
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (job.unique_id,
                                     job.experience, job.skills, job.languages, job.enterprise_name, job.date,
                                     job.address,
                                     job.contract_type,
                                     job.qualification, job.technology.id, job.title))
            self._db_connection.connection.commit()
            self._db_connection.close_connection()
        except mysql.connector.Error:
            print('An error has occurred !')

    def select_job(self):
        try:
            request = f'SELECT * FROM {self._table_name} ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request)
            rows = cursor.fetchall()
            jobs = []
            for row in rows:
                jobs.append(
                    Job(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                        Technology(row[10], ''), row[11]))
            self._db_connection.close_connection()
            return jobs
        except mysql.connector.Error:
            print('Could not fetch jobs !')
            return []

    def select_one_job_by_id(self, job_id):
        try:
            request = f'SELECT * FROM {self._table_name} WHERE id = %s ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (job_id,))
            row = cursor.fetchone()
            job = Job(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                      Technology(row[10], ''), row[11])
            self._db_connection.close_connection()
            return job
        except mysql.connector.Error:
            # print(f'Could not fetch job {job_id} !')
            return None

    def select_one_job_by_unique_id(self, job_unique_id):
        try:
            request = f'SELECT * FROM {self._table_name} WHERE unique_id = %s ORDER BY id'
            self._db_connection.get_connection()
            cursor = self._db_connection.create_cursor()
            cursor.execute(request, (job_unique_id,))
            row = cursor.fetchone()
            if not row:
                raise EmptyResultSetError("No rows found for the given condition.")
            job = Job(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                      Technology(row[10], ''), row[11])
            self._db_connection.close_connection()
            return job
        except mysql.connector.Error:
            print(f'Could not fetch job {job_unique_id} !')
            return None
        except EmptyResultSetError:
            print(f'Could not fetch job {job_unique_id} !')
            return None


class EmptyResultSetError(Exception):
    """Custom exception for empty result sets."""
    pass
