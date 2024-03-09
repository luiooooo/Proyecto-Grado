import customtkinter as ctk
import math
from PIL import Image
import os


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
Marco_x = math.floor(ancho_pantalla * 0.575)
Marco_Y = math.floor(alto_pantalla * 0.24)
MarcoSeleccion = ctk.CTkFrame(Ventana_Principal, height= math.floor(Marco_Y*2.02), width=math.floor(Marco_x*0.315), border_width=math.floor(ancho_pantalla*0.001))   
MarcoSeleccion.place(x=Marco_x,y=Marco_Y) 

#---Fin
    
#--Tamaño botones
#Diferencia de 0.075
BTN_General_Y = math.floor(alto_pantalla * 0.015)
BTN_Original_X = math.floor(ancho_pantalla * 0.007)
BTN_Plano_X = math.floor(ancho_pantalla * 0.082)
BTN_DLLS_X = math.floor(ancho_pantalla * 0.157)
BTN_Librerias_X = math.floor(ancho_pantalla * 0.232)
BTN_Codigo_X = math.floor(ancho_pantalla * 0.307)
BTN_Completo_X = math.floor(ancho_pantalla * 0.382)
BTN_Reporte_X = math.floor(ancho_pantalla * 0.457)

Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0152)
heigh_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0255)
width_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.396)

#---Botones

Botones_Texto = ctk.CTkSegmentedButton(Ventana_Principal,values=["ORIGINAL", "TEXTO", "DLLS", "LIBRERIAS", "CODIGO", "TODO", "REPORTE"], font=("Times New Roman", Letra, "bold"), dynamic_resizing=True, width=130)
Botones_Texto.place(x=BTN_Original_X, y=BTN_General_Y)

Botones_Texto.set("ORIGINAL")

#Posicion Botones Funcionamiento
btn_procesar_x = math.floor(alto_pantalla * 0.54)
btn_procesar_y = math.floor(ancho_pantalla * 0.71)

#Botones de funcionamiento
Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0152)
procesarHeigh = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0265)
procesarWidh = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.22)

procesarX = math.floor(ancho_pantalla * 0.58)
procesarY = math.floor(alto_pantalla * 0.735)

BTN_Procesar = ctk.CTkButton(Ventana_Principal, text="PROCESAR", height=procesarHeigh, width=procesarWidh,font=("Times New Roman", Letra, "bold"), hover_color="#E74C3C")
BTN_Procesar.place(x=procesarX,y=procesarY)


#Posicion Botones abrir y guardar
btn_abrir_x = math.floor(ancho_pantalla * 0.575)
btn_abrir_y = math.floor(alto_pantalla * 0.78)
ancho_abrir = math.floor(ancho_pantalla * 0.09)
alto_abrir = math.floor(alto_pantalla * 0.035)

btn_guardar_x = math.floor(ancho_pantalla * 0.667)

Letra_BTN_Abrir = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.0125)

# Botones abrir archivo y guardar
BTN_Abrir_Archivo = ctk.CTkButton(Ventana_Principal, text="ABRIR", font=("Times New Roman", Letra_BTN_Abrir, "bold"), width=ancho_abrir, height=alto_abrir, hover_color="#1ABC9C")
BTN_Abrir_Archivo.place(x=btn_abrir_x, y=btn_abrir_y)

BTN_cargar_Archivo = ctk.CTkButton(Ventana_Principal, text="GUARDAR", font=("Times New Roman", Letra_BTN_Abrir, "bold"), width=ancho_abrir, height=alto_abrir, hover_color="#1ABC9C")
BTN_cargar_Archivo.place(x=btn_guardar_x, y=btn_abrir_y)
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

#---Fin

#--Funcion scrollbar con texto

def Obtener_texto():
    contenido = Tbox_Principal.get("1.0", "end-1c")
    variable_contenido.set(contenido)
    texto_en_pestaña.configure(state="normal")
    texto_en_pestaña.delete("1.0", "end")  # Limpiar el contenido anterior
    texto_en_pestaña.insert("1.0", contenido)  # Insertar el nuevo contenido
    texto_en_pestaña.configure(state="disabled")
    Ventana_Principal.after(100, Obtener_texto)
#---FIN

#---Views

variable_contenido = ctk.StringVar()

Vista_principal_ancho = math.floor(ancho_pantalla * 0.0315)
Vista_principal_alto = math.floor(alto_pantalla * 0.779)

Vista_principal_X = math.floor(ancho_pantalla * 0.535)
Vista_principal_Y = math.floor(alto_pantalla * 0.0435)


Vista_principal = ctk.CTkTabview(master=Ventana_Principal, width=Vista_principal_ancho, height= Vista_principal_alto)
Vista_principal.place(x=Vista_principal_X, y=Vista_principal_Y)

tab1 = Vista_principal.add("prueba 1")  

copia_textbox = Tbox_Principal

TXTSCROLLBAR = variable_contenido.get()

#texto = ctk.CTkLabel(tab1, text="HOLA, ESTOY EN LA VISTA PRINCIPAL :D")
#texto.pack()

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

#Obtener_texto()

Ventana_Principal.mainloop()
#---FIN