import sqlite3
from sqlite3 import Error

class SpotifyActivityDB:
    def __init__(self, db_file='Spotify.db'):
        self.db_file = db_file
        self.conn = None
        self.setup()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return True
        except Error as e:
            print(f"Error connecting to database: {e}")
        return False

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Activity (
                    userURI TEXT,
                    trackURI TEXT,
                    contextURI TEXT,
                    timestamp INTEGER,
                    PRIMARY KEY (timestamp, userURI)
                )
            ''')
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_datapoint(self, datapoint):
        sql = '''
        INSERT OR IGNORE INTO Activity(userURI, trackURI, contextURI, timestamp)
        VALUES(?,?,?,?)
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, datapoint)
            return cursor.rowcount
        except Error as e:
            print(f"Error inserting datapoint: {e}")
        return 0

    def commit(self):
        self.conn.commit()
        
    def setup(self):
        if self.create_connection():
            self.create_table()
        else:
            print("Error! Cannot create the database connection.")