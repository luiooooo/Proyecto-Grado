import sqlite3
import os

def buscar_contenido(nombre, tipo_riesgo, sql_connection):
    # Crear cursor para Transaccion SQL
    cursor = sql_connection.cursor()

    # Definir query
    query = f"SELECT Contenido.nombre, Tipo_Riesgo_Contenido.nombre_tipo, Versiones_Contenido.version, Versiones_Contenido.created_at FROM Versiones_Contenido JOIN Contenido ON Versiones_Contenido.id_contenido = Contenido.id JOIN Tipo_Riesgo_Contenido ON Versiones_Contenido.id_tipo_riesgo = Tipo_Riesgo_Contenido.id WHERE Contenido.nombre = '{nombre}'"

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
