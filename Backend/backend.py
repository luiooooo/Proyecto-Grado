import sqlite3
import os

def buscar_contenido(nombre, tipo_riesgo, sql_connection):
    # Crear cursor para Transaccion SQL
    cursor = sql_connection.cursor()

    # Definir query
    query = f"SELECT Contenido.nombre, Tipo_Riesgo_Contenido.nombre_tipo, Versiones_Contenido.version, Versiones_Contenido.created_at FROM Versiones_Contenido JOIN Contenido ON Versiones_Contenido.id_contenido = Contenido.id JOIN Tipo_Riesgo_Contenido ON Versiones_Contenido.id_tipo_riesgo = Tipo_Riesgo_Contenido.id WHERE Contenido.nombre = '{nombre}' AND Tipo_Riesgo_Contenido.nombre_tipo = '{tipo_riesgo}'"


    # Ejecutar query y retornar resultados  
    try:
        result = cursor.execute(query)
        if result.fetchall():
            return result.fetchall()
    except Exception as e:
        print(f"Error ejecutando query: {e}")
    finally:
        cursor.close()
        return []


def get_db_connection(db_path):
    try:
        con = sqlite3.connect(db_path) # Conectar a base de datos
        return con
    except Exception as e:
        print("Error conectando a base de datos")
        return None

if __name__ == '__main__':
    # Obtener path a base de datos
    current_dir = os.path.dirname(os.path.abspath(__file__)) # Directorio actual del archivo .py
    db_path = os.path.join(current_dir, 'clarisint.db')      # Path a base de datos
    db_connection = get_db_connection(db_path)               # Conectar a base de datos
    if db_connection is not None: 
       result = buscar_contenido("symsrv.dll", "MALICIOSO", db_connection)
       pass