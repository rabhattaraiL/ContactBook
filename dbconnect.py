import pyodbc
from dotenv import dotenv_values

class DBConnectHelper:
    def __init__(self):
        env_vars = dotenv_values('config/.env')
        server = env_vars['SERVER']
        database = env_vars['DATABASE']
        username = env_vars['USERNAME']
        password = env_vars['PASSWORD']

        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # The stored procedures are already created in the database of use.
    # They create table structure
    def create_tables(self):
        database_tables = ['ContactTable', 'AddressBook', 'NoteTable']
        for table in database_tables:
            self.cursor.execute(f'EXEC spCreateTable{table}')
            self.conn.commit()