import customtkinter as ctk
import math
from PIL import Image
import os
import tkinter.simpledialog as sd
import tkinter.filedialog as df
import json

""" Significado de comentarios
# desarrollo
#---Titulo
#--Subtitulo
"""

#---Ventana principal
Ventana_Principal = ctk.CTk()
Ventana_Principal.title("Clarisint MalwareText")
Ventana_Principal.resizable(width=False,height=False)

#Obtener resolucion
ancho_x = Ventana_Principal.winfo_screenwidth()
alto_y = Ventana_Principal.winfo_screenheight()
Ancho_inicio = math.floor(Ventana_Principal.winfo_screenwidth() // 1.31)
Alto_inicio = math.floor(Ventana_Principal.winfo_screenheight() // 1.2)

Ventana_Principal.geometry(f"{Ancho_inicio}x{Alto_inicio}+100+0")

##---MANEJO DE ARCHIVOS
def guardar_Textos():
    carpeta_seleccionada = ctk.filedialog.askdirectory()
    if carpeta_seleccionada:
        nombre_carpeta = sd.askstring("Nombre de la carpeta", "Ingrese el nombre de la carpeta:")
        ruta_carpeta = os.path.join(carpeta_seleccionada, nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

        for variable, contenido in contenido_guardado.items():
            nombre_archivo = f"{variable}."
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            with open(ruta_archivo, 'w') as archivo:
                archivo.write(contenido)

        print("Archivos de Texto guardados en:", ruta_carpeta)
##Fin

##---GUARDAR VARIABLES EN .JSON    
def guardar_todas_variables():
    # Solicitar al usuario la ubicación y el nombre del archivo para guardar
    #if (ruta == null)
    ruta_archivo = ctk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not ruta_archivo:
        return  # El usuario canceló la operación
    
    # Crear un diccionario para almacenar todas las variables
    todas_variables = {}
    for variable, contenido in contenido_guardado.items():
        todas_variables[variable] = contenido

    # Guardar el diccionario en formato JSON en el archivo
    with open(ruta_archivo, 'w') as archivo:
        json.dump(todas_variables, archivo)
    
    print("Variables guardadas en:", ruta_archivo)
#FIN
    

##---CARGAR VARIABLES DEL .JSON
    
#Lista con botones para abrir proyectos
botones = []
botones_proyectos_y = math.floor(alto_y * 0.25)
proyectos_guardados = [""]
def agregar_boton(nombre_archivo):
    global botones_proyectos_y
    botones_proyectos_x = math.floor(ancho_x * 0.584)    
    boton = ctk.CTkButton(Ventana_Principal, text=nombre_archivo, height=procesarHeigh*0.7, width=procesarWidh*0.99,font=("Times New Roman", Letra*0.65, "bold"), hover_color="#00796B", corner_radius=heigh_valor*0.365, command=lambda: cargar_variables_desde_json(nombre_archivo))
    boton.place(x=botones_proyectos_x, y=botones_proyectos_y)
    a = math.floor(alto_y * 0.25)
    b = math.floor(alto_y * 0.25)*1.12
    c = b-a
    botones_proyectos_y += c
    botones.append(boton)

def cargar_proyecto():
    global proyectos_guardados, botones
    ruta_archivo_json = ctk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if ruta_archivo_json:
        nombre_archivo = os.path.basename(ruta_archivo_json)
        proyectos_guardados.append(ruta_archivo_json)
        if not any(boton._text == nombre_archivo for boton in botones):
            agregar_boton(nombre_archivo)


def cargar_variables_desde_json(nombre_archivo):
    # Verificar si el archivo existe
    for ruta_archivo_json in proyectos_guardados:
        if nombre_archivo in ruta_archivo_json:
            ruta_archivo = ruta_archivo_json
            break
    else:
        return    
    if not os.path.isfile(ruta_archivo):
        print("El archivo especificado no existe.")
        return None
    # Intentar cargar el contenido del archivo JSON
    try:
        with open(ruta_archivo, 'r') as archivo:
            variables_cargadas = json.load(archivo)
        print("Variables cargadas desde:", ruta_archivo)
        actualizar_contenido_guardado(variables_cargadas)
    except json.JSONDecodeError as e:
        print("Error al decodificar el archivo JSON:", e)
        return None

def actualizar_contenido_guardado(variables_cargadas):
    global contenido_guardado
    contenido_guardado = variables_cargadas



#Guardar info en Texto Original
def actualizar_variables(evento):
    global contenido_guardado
    contenido = Tbox_Principal.get("1.0","end-1c")  
    contenido_guardado[Boton_Texto_Presionado] = contenido
    print("Contenido guardado para", Boton_Texto_Presionado, ":", contenido)

contenido_guardado = {
    "Original": "",  
    "Texto": "",
    "Dlls": "",
    "Librerias": "",
    "Codigo": "",
    "Todo": "",
    "Reporte": ""
}
#FIN


#---Botones
#Funcion activar y desactivar botones
def desactivar_botones_secundarios(botones_secundarios):
    for boton in botones_secundarios:
        boton.configure(state="disabled")

def activar_botones_secundarios(botones_secundarios):
    for boton in botones_secundarios:
        boton.configure(state="normal")

def cambiar_variable(variable):
    contenido = contenido_guardado.get(variable, "")
    Tbox_Principal.delete("1.0", "end")
    Tbox_Principal.insert("1.0", contenido)

def pestana_abierta(btn_presionado):
    global  Boton_Texto_Presionado
    Boton_Texto_Presionado = btn_presionado
    cambiar_variable(Boton_Texto_Presionado)
    

x = heigh_valor*0.365
Botones_Texto = ctk.CTkSegmentedButton(Ventana_Principal,values=["Original", "Texto", "Dlls", "Librerias", "Codigo", "Todo", "Reporte"], font=("Times New Roman", Letra, "bold"), dynamic_resizing=True, width=130, command=pestana_abierta, corner_radius=heigh_valor*0.365)
Botones_Texto.place(x=BTN_Original_X, y=BTN_General_Y)

Botones_Texto.set("Original")
Boton_Texto_Presionado = "Original"

botones_secundarios = [widget for widget in Botones_Texto.winfo_children() if isinstance(widget, ctk.CTkButton)]
desactivar_botones_secundarios(botones_secundarios)

#Posicion Botones Funcionamiento
btn_procesar_x = math.floor(alto_y * 0.54)
btn_procesar_y = math.floor(ancho_x * 0.71)

#Botones de funcionamiento
Letra = math.floor(((ancho_x+alto_y)/2)*0.0152)
procesarHeigh = math.floor(((ancho_x+alto_y)/2)*0.0265)
procesarWidh = math.floor(((ancho_x+alto_y)/2)*0.22)

procesarX = math.floor(ancho_x * 0.58)
procesarY = math.floor(alto_y * 0.735)

#--Funcion Procesar Texto
def BTN_Procesar_presionado():
    activar_botones_secundarios(botones_secundarios)

BTN_Procesar = ctk.CTkButton(Ventana_Principal, text="PROCESAR", height=procesarHeigh, width=procesarWidh,font=("Times New Roman", Letra, "bold"), hover_color="#E74C3C", command=BTN_Procesar_presionado, corner_radius=heigh_valor*0.365)
BTN_Procesar.place(x=procesarX,y=procesarY)

ExportarY = math.floor(alto_y * 0.7835)

#Boton EXPORTAR (.txt)
BTN_exportar_Archivo = ctk.CTkButton(Ventana_Principal, text="EXPORTAR", font=("Times New Roman", Letra, "bold"), width=procesarWidh, height=procesarHeigh, hover_color="#1ABC9C", command=guardar_Textos, corner_radius=heigh_valor*0.365)
BTN_exportar_Archivo.place(x=procesarX,y=ExportarY)

#Posicion Botones abrir y guardar progreso
Abrir_X = math.floor(ancho_x * 0.4)
Abrir_Y = math.floor(alto_y * 0.023)
Guardar_X = math.floor(ancho_x * 0.455)

BTN_Abrir = ctk.CTkButton(Ventana_Principal, text="Abrir", height=procesarHeigh*0.7, width=procesarWidh*0.3,font=("Times New Roman", Letra*0.65, "bold"), hover_color="#00796B", command=cargar_proyecto, corner_radius=heigh_valor*0.365)
BTN_Abrir.place(x=Abrir_X,y=Abrir_Y)

BTN_Guardar = ctk.CTkButton(Ventana_Principal, text="Guardar", height=procesarHeigh*0.7, width=procesarWidh*0.3,font=("Times New Roman", Letra*0.65, "bold"), hover_color="#00796B", command=guardar_todas_variables, corner_radius=heigh_valor*0.365)
BTN_Guardar.place(x=Guardar_X,y=Abrir_Y)

#---Fin

#---TextBox Principal

#Tamano Textbox         
Tbox_X = math.floor(ancho_x * 0.007)
Tbox_Y = math.floor(alto_y * 0.055)
Altura_Tbox = math.floor(alto_y * 0.765)
Anchura_Tbox = math.floor(alto_y * 0.94)

#TextBox Principal
Letra_TextBox = math.floor(((ancho_x+alto_y)/2)*0.012)
Tbox_Principal = ctk.CTkTextbox(Ventana_Principal,height=Altura_Tbox, width=Anchura_Tbox, font=("Times New Roman", Letra_TextBox), activate_scrollbars=False, border_width=3)
Tbox_Principal.place(x= Tbox_X, y= Tbox_Y)
Tbox_Principal.pack_propagate(False)

Tbox_Principal.bind("<KeyRelease>", actualizar_variables)

#---Fin

#---Views INCOMPLETO

variable_contenido = ctk.StringVar()

Vista_principal_ancho = math.floor(ancho_x * 0.0315)
Vista_principal_alto = math.floor(alto_y * 0.779)

Vista_principal_X = math.floor(ancho_x * 0.535)
Vista_principal_Y = math.floor(alto_y * 0.0435)


Vista_principal = ctk.CTkTabview(master=Ventana_Principal, width=Vista_principal_ancho, height= Vista_principal_alto)
Vista_principal.place(x=Vista_principal_X, y=Vista_principal_Y)

#---Fin

#Tamano scrollbar
ScrollBar_X = math.floor(ancho_x * 0.565)
ScrollBar_Y = math.floor(alto_y * 0.0536)

ScrollBar_medida_X = math.floor(ancho_x * 0.008)
ScrollBar_medida_Y = math.floor(alto_y * 0.769)

#---Scrollbar

TextBar_Principal = ctk.CTkScrollbar(Ventana_Principal, orientation="vertical", width= ScrollBar_medida_X, height=ScrollBar_medida_Y, command=Tbox_Principal.yview, corner_radius=10)
TextBar_Principal.place(x=ScrollBar_X, y=ScrollBar_Y)

Tbox_Principal.configure(yscrollcommand=TextBar_Principal.set)

#---Fin

#---MAIN LOOP
ListaX = math.floor(ancho_x * 0.61)
ListaY = math.floor(alto_y * 0.21)
LISTA = ctk.CTkLabel(Ventana_Principal, text="LISTA PROYECTOS", font=("Times New Roman", Letra, "bold"),text_color="#1ABC9C")
LISTA.place(x=ListaX,y=ListaY)

#Obtener_Texto()
if __name__ == "__main__":
    Ventana_Principal.mainloop()
#---FIN