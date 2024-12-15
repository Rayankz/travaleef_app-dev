import psycopg2
from psycopg2 import pool
import configparser
import os

from psycopg2.extras import RealDictCursor

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

db_name = config['database']['name']
db_user = config['database']['user']
db_password = config['database']['password']
db_host = config['database']['host']
db_port = int(config['database']['port'])

class PostgresSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PostgresSingleton, cls).__new__(cls)
            cls._instance._init_connection_pool(*args, **kwargs)
        return cls._instance

    def _init_connection_pool(self, dbname, user, password, host, port=5432, minconn=1, maxconn=5):
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn,
                maxconn,
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print("Connexion pool créée avec succès")
        except Exception as e:
            print(f"Erreur lors de la création de la pool de connexions: {e}")
            raise

    def get_connection(self):
        try:
            return self.connection_pool.getconn()
        except Exception as e:
            print(f"Erreur lors de l'obtention de la connexion: {e}")
            raise

    def release_connection(self, connection):
        try:
            self.connection_pool.putconn(connection)
        except Exception as e:
            print(f"Erreur lors de la libération de la connexion: {e}")
            raise

    def close_all_connections(self):
        try:
            self.connection_pool.closeall()
        except Exception as e:
            print(f"Erreur lors de la fermeture de toutes les connexions: {e}")
            raise

    def execute_query(self, query, params=None, fetch_all=False, fetch_one=False):
        connection = self.get_connection()
        try:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)

                if query.strip().lower().startswith("select"):
                    if fetch_all:
                        result = cursor.fetchall()
                        return result
                    if fetch_one:
                        result = cursor.fetchone()
                        return result

                rows_affected = cursor.rowcount
                connection.commit()
                return rows_affected

        except Exception as e:
            connection.rollback()
            print(f"Erreur lors de l'exécution de la requête : {e}")
            raise
        finally:
            self.release_connection(connection)

# Utilisation du Singleton pour la connexion à PostgreSQL

if __name__ == "__main__":
    # Crée une instance de PostgresSingleton
    db_singleton = PostgresSingleton(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    # Obtention d'une connexion
    connection = db_singleton.get_connection()

    try:
        # Utilisation de la connexion
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print(f"Version de la base de données : {db_version}")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la requête: {e}")
    finally:
        # Libération de la connexion
        db_singleton.release_connection(connection)

    # Fermeture de toutes les connexions lors de l'arrêt de l'application
    db_singleton.close_all_connections()

db_singleton = PostgresSingleton(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
