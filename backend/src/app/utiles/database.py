import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self, host, database, user, password, port=5432):
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        self.connection.autocommit = True

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            if fetch_one:
                return cursor.fetchone()
            if fetch_all:
                return cursor.fetchall()
            return None

    def close(self):
        self.connection.close()
