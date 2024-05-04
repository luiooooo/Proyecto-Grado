import sqlite3
import os

DEFAULT_DB_PATH = 'clarisint.db' # Nombre de base de datos

# Conectar a base de datos SQLite
def connect_database(db_path):
    if os.path.isfile(db_path):
        con = sqlite3.connect(db_path)
        return con # Retornar conexion a base de datos
    return None

# Obtener path a base de datos
def get_db_connection():
    current_dir = os.path.dirname(os.path.abspath(__file__)) # Directorio actual del archivo .py
    db_path = os.path.join(current_dir, DEFAULT_DB_PATH)      # Path a base de datos
    db_con = connect_database(db_path)             
    return db_con
