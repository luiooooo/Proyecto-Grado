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
        return None

def exportar_textos(ruta_carpeta, nombre_proyecto, contenido_guardado):
    ruta_carpeta = os.path.join(ruta_carpeta, nombre_proyecto)
    os.makedirs(ruta_carpeta, exist_ok=True)

    for variable, contenido in contenido_guardado.items():
        nombre_archivo = f"{variable}.txt"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        with open(ruta_archivo, 'w') as archivo:
            if variable == "Input":
                archivo.write(contenido)
            else:
                content = [tpl[0] for tpl in contenido]
                archivo.write('\n'.join(content))

def limpiar_textos(dict, erase_input=False):
    for key, value in dict.items():
        if isinstance(value, list):
            dict[key].clear()
        elif key == "Input" and erase_input: 
            dict[key] = ""

def is_content_empty(dict):
    for key, value in dict.items():
        if isinstance(value, list) and len(value) > 0:
            return False
        elif key == "Input" and value != "":
            return False
    return True