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
##---MANEJO DE ARCHIVOS
def guardar_Textos():
    carpeta_seleccionada = ctk.filedialog.askdirectory()
    if carpeta_seleccionada:
        nombre_carpeta = sd.askstring("Nombre de la carpeta", "Ingrese el nombre de la carpeta:")
        ruta_carpeta = os.path.join(carpeta_seleccionada, nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

        for variable, contenido in contenido_guardado.items():
            nombre_archivo = f"{variable}.txt"
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            with open(ruta_archivo, 'w') as archivo:
                archivo.write(contenido)

        print("Archivos de Texto guardados en:", ruta_carpeta)
##Fin

##---GUARDAR VARIABLES EN .JSON    
def guardar_todas_variables():
    # Solicitar al usuario la ubicación y el nombre del archivo para guardar
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
def cargar_variables_desde_json(ruta_archivo):
    # Verificar si el archivo existe
    if not os.path.isfile(ruta_archivo):
        print("El archivo especificado no existe.")
        return None

    # Intentar cargar el contenido del archivo JSON
    try:
        with open(ruta_archivo, 'r') as archivo:
            variables_cargadas = json.load(archivo)
        print("Variables cargadas desde:", ruta_archivo)
        return variables_cargadas
    except json.JSONDecodeError as e:
        print("Error al decodificar el archivo JSON:", e)
        return None

def usar_variables_cargadas():
    ruta_archivo_json = ctk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if ruta_archivo_json:
        variables_cargadas = cargar_variables_desde_json(ruta_archivo_json)
        global contenido_guardado 
        contenido_guardado = variables_cargadas


#FIN
#---Ventana principal
Ventana_Principal = ctk.CTk()
Ventana_Principal.title("Clarisint MalwareText")
Ventana_Principal.resizable(width=False,height=False)

#Obtener resolucion
ancho_pantalla = Ventana_Principal.winfo_screenwidth()
alto_pantalla = Ventana_Principal.winfo_screenheight()
Ancho_inicio = math.floor(ancho_pantalla // 1.31)
Alto_inicio = math.floor(alto_pantalla // 1.2)

Ventana_Principal.geometry(f"{Ancho_inicio}x{Alto_inicio}+100+0")

#--Fin

#---Imagen Logo
logo_X = math.floor(ancho_pantalla * 0.61)
logo_Y = math.floor(alto_pantalla * 0.012)

tamano_logo = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.15)


Directorio_actual = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(Directorio_actual, "Fotos", "ClariSint MalwareText LOGO.jpeg")
imagen_logo = ctk.CTkImage(dark_image=Image.open(image_path), size=(tamano_logo,tamano_logo))
Label_logo = ctk.CTkLabel(Ventana_Principal, image= imagen_logo, text="")

Label_logo.place(x = logo_X, y =  logo_Y)

#LOGO = ctk.p

#---Fin

#---Marco
Marco_x = math.floor(ancho_pantalla * 0.576)
Marco_Y = math.floor(alto_pantalla * 0.24)
MarcoSeleccion = ctk.CTkFrame(Ventana_Principal, height= math.floor(Marco_Y*2.02), width=math.floor(Marco_x*0.315), border_width=math.floor(ancho_pantalla*0.001))   
MarcoSeleccion.place(x=Marco_x,y=Marco_Y) 

#---Fin
    
#--Tamaño botones
#Diferencia de 0.075
BTN_General_Y = math.floor(alto_pantalla * 0.015)
BTN_Original_X = math.floor(ancho_pantalla * 0.007)
BTN_Plano_X = math.floor(ancho_pantalla * 0.082)
BTN_Dlls_X = math.floor(ancho_pantalla * 0.157)
BTN_Librerias_X = math.floor(ancho_pantalla * 0.232)
BTN_Codigo_X = math.floor(ancho_pantalla * 0.307)
BTN_Completo_X = math.floor(ancho_pantalla * 0.382)
BTN_Reporte_X = math.floor(ancho_pantalla * 0.457)

Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0152)
heigh_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0255)
width_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.396)

#---Botones
#Funcion activar y desactivar botones
def desactivar_botones_secundarios(botones_secundarios):
    for boton in botones_secundarios:
        boton.configure(state="disabled")

def activar_botones_secundarios(botones_secundarios):
    for boton in botones_secundarios:
        boton.configure(state="normal")

def cambiar_variable(variable):
    variable_actual = variable
    contenido = contenido_guardado.get(variable_actual, "")
    Tbox_Principal.delete("1.0", "end")
    Tbox_Principal.insert("1.0", contenido)

def pestana_abierta(btn_presionado):
    global boton_actual_presionado, variable_actual
    boton_actual_presionado = btn_presionado
    variable_actual = btn_presionado
    cambiar_variable(variable_actual)

boton_actual_presionado = ""
Botones_Texto = ctk.CTkSegmentedButton(Ventana_Principal,values=["Original", "Texto", "Dlls", "Librerias", "Codigo", "Todo", "Reporte"], font=("Times New Roman", Letra, "bold"), dynamic_resizing=True, width=130, command=pestana_abierta)
Botones_Texto.place(x=BTN_Original_X, y=BTN_General_Y)

Botones_Texto.set("Original")
variable_actual = "Original"

botones_secundarios = [widget for widget in Botones_Texto.winfo_children() if isinstance(widget, ctk.CTkButton)]
desactivar_botones_secundarios(botones_secundarios)

#Posicion Botones Funcionamiento
btn_procesar_x = math.floor(alto_pantalla * 0.54)
btn_procesar_y = math.floor(ancho_pantalla * 0.71)

#Botones de funcionamiento
Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0152)
procesarHeigh = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0265)
procesarWidh = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.22)

procesarX = math.floor(ancho_pantalla * 0.58)
procesarY = math.floor(alto_pantalla * 0.735)

#--Funcion Procesar Texto
def BTN_Procesar_presionado():
    activar_botones_secundarios(botones_secundarios)

#Guardar info en Texto Original
def actualizar_variables(evento):
    global contenido_guardado
    contenido = Tbox_Principal.get("1.0","end-1c")  
    contenido_guardado[variable_actual] = contenido
    print("Contenido guardado para", variable_actual, ":", contenido)

contenido_guardado = {
    "Original": "",  
    "Texto": "",
    "Dlls": "",
    "Librerias": "",
    "Codigo": "",
    "Todo": "",
    "Reporte": ""
}

BTN_Procesar = ctk.CTkButton(Ventana_Principal, text="PROCESAR", height=procesarHeigh, width=procesarWidh,font=("Times New Roman", Letra, "bold"), hover_color="#E74C3C", command=BTN_Procesar_presionado)
BTN_Procesar.place(x=procesarX,y=procesarY)

ExportarY = math.floor(alto_pantalla * 0.7835)
#Boton EXPORTAR (.txt)
BTN_exportar_Archivo = ctk.CTkButton(Ventana_Principal, text="EXPORTAR", font=("Times New Roman", Letra, "bold"), width=procesarWidh, height=procesarHeigh, hover_color="#1ABC9C", command=guardar_Textos)
BTN_exportar_Archivo.place(x=procesarX,y=ExportarY)

#Posicion Botones abrir y guardar progreso
Abrir_X = math.floor(ancho_pantalla * 0.4)
Abrir_Y = math.floor(alto_pantalla * 0.023)
Guardar_X = math.floor(ancho_pantalla * 0.455)

BTN_Abrir = ctk.CTkButton(Ventana_Principal, text="Abrir", height=procesarHeigh*0.7, width=procesarWidh*0.3,font=("Times New Roman", Letra*0.65, "bold"), hover_color="#00796B", command=usar_variables_cargadas)
BTN_Abrir.place(x=Abrir_X,y=Abrir_Y)

BTN_Guardar = ctk.CTkButton(Ventana_Principal, text="Guardar", height=procesarHeigh*0.7, width=procesarWidh*0.3,font=("Times New Roman", Letra*0.65, "bold"), hover_color="#00796B", command=guardar_todas_variables)
BTN_Guardar.place(x=Guardar_X,y=Abrir_Y)

#---Fin

#---TextBox Principal

#Tamano Textbox         
Tbox_X = math.floor(ancho_pantalla * 0.007)
Tbox_Y = math.floor(alto_pantalla * 0.055)
Altura_Tbox = math.floor(alto_pantalla * 0.765)
Anchura_Tbox = math.floor(alto_pantalla * 0.94)

#TextBox Principal
Letra_TextBox = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.012)
Tbox_Principal = ctk.CTkTextbox(Ventana_Principal,height=Altura_Tbox, width=Anchura_Tbox, font=("Times New Roman", Letra_TextBox), activate_scrollbars=False, border_width=3)
Tbox_Principal.place(x= Tbox_X, y= Tbox_Y)
Tbox_Principal.pack_propagate(False)

Tbox_Principal.bind("<KeyRelease>", actualizar_variables)

#---Fin


#---Views INCOMPLETO

variable_contenido = ctk.StringVar()

Vista_principal_ancho = math.floor(ancho_pantalla * 0.0315)
Vista_principal_alto = math.floor(alto_pantalla * 0.779)

Vista_principal_X = math.floor(ancho_pantalla * 0.535)
Vista_principal_Y = math.floor(alto_pantalla * 0.0435)


Vista_principal = ctk.CTkTabview(master=Ventana_Principal, width=Vista_principal_ancho, height= Vista_principal_alto)
Vista_principal.place(x=Vista_principal_X, y=Vista_principal_Y)

#---Fin

#Tamano scrollbar
ScrollBar_X = math.floor(ancho_pantalla * 0.565)
ScrollBar_Y = math.floor(alto_pantalla * 0.0536)

ScrollBar_medida_X = math.floor(ancho_pantalla * 0.008)
ScrollBar_medida_Y = math.floor(alto_pantalla * 0.769)


#---Scrollbar

TextBar_Principal = ctk.CTkScrollbar(Ventana_Principal, orientation="vertical", width= ScrollBar_medida_X, height=ScrollBar_medida_Y, command=Tbox_Principal.yview, corner_radius=10)
TextBar_Principal.place(x=ScrollBar_X, y=ScrollBar_Y)

Tbox_Principal.configure(yscrollcommand=TextBar_Principal.set)

#---Fin

#---MAIN LOOP
ListaX = math.floor(ancho_pantalla * 0.61)
ListaY = math.floor(alto_pantalla * 0.21)
LISTA = ctk.CTkLabel(Ventana_Principal, text="LISTA PROYECTOS", font=("Times New Roman", Letra, "bold"),text_color="#1ABC9C")
LISTA.place(x=ListaX,y=ListaY)

#Obtener_Texto()

Ventana_Principal.mainloop()
#---FIN