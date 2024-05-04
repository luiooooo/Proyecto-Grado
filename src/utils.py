import json


def guardar_json(ruta, contenido):
    try:
        with open(ruta, 'w') as archivo:
                json.dump(contenido, archivo)      
    except :
        print("Error al guardar el archivo JSON:")


def cargar_json(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except:
        print("Error al decodificar el archivo JSON:")