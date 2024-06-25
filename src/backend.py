import sqlite3
import os
import db_connection
import re

db = db_connection.get_db_connection()

#Variables globales
lineas_limpias = []

def buscar_contenido(nombre, sql_connection):
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

###MOVER ESTO A BACKEND
def clean_process(txt_to_process):
    patrones_basura = [
        re.compile(r'^[^\w\s]*$'),                # Líneas que no contienen caracteres alfanuméricos
        re.compile(r'\bHSU\w*\b'),                # Palabras que empiezan con HSU
        re.compile(r'\bHSW\w*\b'),                # Palabras que empiezan con HSW
        re.compile(r'\bSVW\w*\b'),                # Palabras que empiezan con SVW
        re.compile(r'\bUAV\w*\b'),                # Palabras que empiezan con UAV
        re.compile(r'\bUAWA\w*\b'),               # Palabras que empiezan con UAWA
        re.compile(r'\bAWAV\w*\b'),               # Palabras que empiezan con AWAV
        re.compile(r'\bUVW\w*\b'),                # Palabras que empiezan con UVW
        re.compile(r'[^\w\s.@*\-\']|(?<![\w.])[.@]'),            # Cualquier cosa que no sea alfanumérica, espacio, punto, arroba, asterisco, guion o comilla
        re.compile(r'^[^a-zA-Z0-9]*$'),           # Líneas que no contienen letras o números
        re.compile(r'^.{1,3}$'),                  # Líneas muy cortas
        re.compile(r'^\d+$'),                     # Líneas que contienen solo números
        re.compile(r'^.*?\$(?![\w.]|\S\S\S).*?$'),                # Líneas que contienen el símbolo $
        re.compile(r'\b(?:储墨墨悪|균기길김|储墨您梨)\b'),  # Caracteres aleatorios no identificables
        re.compile(r'[^\x00-\x7F]+'),             # Caracteres no ASCII, suponiendo que no sean relevantes
        re.compile(r'^[\s\W_]+$'),                # Líneas que contienen solo espacios, caracteres no alfanuméricos y guiones bajos
        re.compile(r'\b(?:b\\p|B\\p|\\l#mW|RHS8DAdNTsLCOIEV\.X\.PU|0pc3d5b7-9lBsDEF)\b'),  # Patrones de texto aleatorio o sin sentido
        re.compile(r'\b(?:P\s+"|储墨墨悪|균기길김|储墨您梨)\b'),  # Patrones específicos de caracteres extraños o sin sentido
        re.compile(r'^\d{1,2}:\d{2}:\d{2}\s+\d{4}-\d{2}-\d{2}$'),  # Formatos de fecha y hora sin contexto
        re.compile(r'\b(?:[a-fA-F0-9]{16,})\b'),  # Secuencias largas de caracteres hexadecimales
        re.compile(r'^\d+.*$'),                   # Líneas que comienzan con números
        re.compile(r'\b(?:AVVWSH|VWUSH|gffffffff|gfffffff)\b'),  # Palabras repetidas y sin contexto
        re.compile(r'\b(?:[a-zA-Z]\d+[a-zA-Z])\b'),  # Patrones de letras y números sin sentido (e.g., t-H9s, BQRAPAQH)
        re.compile(r'\b(?:H9Q\s+u1H|3L9f0t|7L9v8t|tyH9_)\b'),  # Combinaciones específicas de letras y números sin sentido
        re.compile(r'\b(?:[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_]{10,})\b'),  # Secuencias largas de caracteres alfanuméricos y guiones bajos
        re.compile(r'\b(?:Bla World Bla Bla)\b'),  # Frases sin sentido
        re.compile(r'^\d{4,}\b'),  # Líneas con muchos números
        #nuevos
        re.compile(r'(.)\1{3,}'), #Identifica lineas con 5 o mas caracteres seguidos
        re.compile(r'\b\.\w+|\@\.\w+'),      # .text, @.data, etc.
        re.compile(r'^\s*$'),    #Identifica lineas vacias
        re.compile(r'[\u0E0E-\u0E7F]'),  #Caracteres tailandeses 
        re.compile(r'\b\w{1}\d+[A-Z]\w*\b'),  # Patrones como t2H9_, taH9s, t6H9N
        re.compile(r'\b\w{1,2}[A-Z]{1}\d+\w*\b'),  # Patrones como tnH9q, tSL9Y, tLL9X, tXL9P
        re.compile(r'\bgf{4,}\w*\b'),  # Patrones como gfffffffH
        re.compile(r'\b[A-Z]{1}\w+\d+\w*\b'),  # Patrones como BQRAPAQH, y combinaciones similares
        re.compile(r'\b[A-Z]{2,}\w+\b'),  # Patrones como AVVWUSH, BQRAPAQH
        re.compile(r'\b[A-Z]{2}\w+\d+\b'),  # Patrones como tMI9H, tfL9Z, tXL9k
        re.compile(r'\b[a-z]\d+[A-Z][a-z]\d+\b'),  # Patrones como taH9s
        re.compile(r'\b\d+[a-zA-Z]{2,}\d+\b'),  # Patrones como H3KXH3CPH, Q8H9Q v
        re.compile(r'\b[a-zA-Z]{2,}\d+[a-zA-Z]\b'),  # Patrones como x0uNf.
        re.compile(r'@ \d+[a-zA-Z]\d+'),  # Patrones como @ 0t4H
        re.compile(r'\b[a-z]{2}[A-Z]\d\b'),  # Patrones como tEH9p
        re.compile(r'\b[a-z]{1}[A-Z]\d+[a-z]\b'),  # Patrones como tVL9f
        re.compile(r'\b[a-z]{1,2}[A-Z]\d{1,2}[a-z]*\b'),  # Patrones como txL9R, xcI9_, xfI9_
        re.compile(r'\b[a-z]{2,3}[A-Z]\w*\b'),  # Patrones como xbtlD, oTU0f
        re.compile(r'\b[a-zA-Z]{1}\d+[A-Z][a-zA-Z]\b'),  # Patrones como t3Hc@
        re.compile(r'\b[A-Z]{2,}[A-Z][a-zA-Z]\b'),  # Patrones como AVVWUSH
        re.compile(r'\b[a-zA-Z]{2,}[a-zA-Z]\b'),  # Patrones como filor, adgjmpsvy
        re.compile(r'\b\d+\w*\b')  # Números seguidos de cualquier cosa, como '*-036
    ]
    
    lineas = txt_to_process.split('\n')
    for linea in lineas:
        es_basura = False
        for patron in patrones_basura:
            if patron.search(linea):
                es_basura = True
                break
        if not es_basura:
            lineas_limpias.append(linea)
    return lineas



def procesar_texto(txt_to_process):
    base_text = txt_to_process.split('\n')
    cleaned_text = clean_process('\n'.join(base_text))
    return cleaned_text
