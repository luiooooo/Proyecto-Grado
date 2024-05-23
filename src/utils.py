import json
import os

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

def exportar_textos(ruta_carpeta, nombre_proyecto, contenido_guardado):
    ruta_carpeta = os.path.join(ruta_carpeta, nombre_proyecto)
    os.makedirs(ruta_carpeta, exist_ok=True)

    for variable, contenido in contenido_guardado.items():
        nombre_archivo = f"{variable}.txt"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(contenido)

def limpiar_textos(contenido_guardado):
    for key in contenido_guardado:
        contenido_guardado[key] = ""
