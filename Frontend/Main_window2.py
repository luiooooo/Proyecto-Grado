import customtkinter as ctk
import math

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

#---MarcarBoton

# Definir colores

def Marcar_boton(boton_presionado):
    for boton in lista_botones:
        boton.configure(fg_color=BTN_colorBase)
    
    boton_presionado.configure(fg_color=BTN_ColorPresion)

    global ultimo_boton_presionado
    ultimo_boton_presionado = boton_presionado


#--Tamaño botones
#Diferencia de 0.075
BTN_General_Y = math.floor(alto_pantalla * 0.024)
BTN_Original_X = math.floor(ancho_pantalla * 0.007)
BTN_Plano_X = math.floor(ancho_pantalla * 0.082)
BTN_DLLS_X = math.floor(ancho_pantalla * 0.157)
BTN_Librerias_X = math.floor(ancho_pantalla * 0.232)
BTN_Codigo_X = math.floor(ancho_pantalla * 0.307)
BTN_Completo_X = math.floor(ancho_pantalla * 0.382)
BTN_Reporte_X = math.floor(ancho_pantalla * 0.457)

Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.00049)
heigh_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.018)
width_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.096)

#---Botones
BTN_colorBase = "#3498DB"
BTN_ColorPresion = "#1F618D"

#--Botones de texto
BTN_Texto_Original = ctk.CTkButton(Ventana_Principal, text="ORIGINAL", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_Original))
BTN_Texto_Original.place(x=BTN_Original_X, y=BTN_General_Y)
BTN_Texto_Plano = ctk.CTkButton(Ventana_Principal, text="TEXTO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_Plano) )
BTN_Texto_Plano.place(x=BTN_Plano_X, y=BTN_General_Y)
BTN_Texto_Dlls = ctk.CTkButton(Ventana_Principal, text="DLLS", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_Dlls))
BTN_Texto_Dlls.place(x=BTN_DLLS_X, y=BTN_General_Y)
BTN_Texto_Librerias = ctk.CTkButton(Ventana_Principal, text="LIBRERIAS", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_Librerias))
BTN_Texto_Librerias.place(x=BTN_Librerias_X, y=BTN_General_Y)
BTN_Texto_Codigo = ctk.CTkButton(Ventana_Principal, text="CODIGO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_Codigo))
BTN_Texto_Codigo.place(x=BTN_Codigo_X, y=BTN_General_Y)
BTN_Texto_TODO = ctk.CTkButton(Ventana_Principal, text="TODO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_TODO))
BTN_Texto_TODO.place(x=BTN_Completo_X, y=BTN_General_Y)
BTN_Texto_REPORTE = ctk.CTkButton(Ventana_Principal, text="REPORTE", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"), fg_color=BTN_colorBase, hover_color= BTN_ColorPresion, command=lambda: Marcar_boton(BTN_Texto_REPORTE))
BTN_Texto_REPORTE.place(x=BTN_Reporte_X, y=BTN_General_Y)

#Lista de botones
lista_botones = [BTN_Texto_Original,BTN_Texto_Plano,BTN_Texto_Dlls, BTN_Texto_Librerias, BTN_Texto_Codigo,BTN_Texto_TODO, BTN_Texto_REPORTE]
#Ultimo boton presionado
ultimo_boton_presionado = None


#Posicion Botones Funcionamiento
btn_procesar_x = math.floor(alto_pantalla * 0.9)
btn_procesar_y = math.floor(ancho_pantalla * 0.9)

#Botones de funcionamiento
BTN_Procesar = ctk.CTkButton(Ventana_Principal, text="PROCESAR", height=heigh_valor, width=width_valor,font=("Times New Roman", Letra, "bold"))
#BTN_Procesar.place(x=btn_procesar_x, y=btn_procesar_y)

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

#Tamano scrollbar
ScrollBar_X = math.floor(ancho_pantalla * 0.535)
ScrollBar_Y = math.floor(alto_pantalla * 0.0536)

ScrollBar_medida_X = math.floor(ancho_pantalla * 0.035)
ScrollBar_medida_Y = math.floor(alto_pantalla * 0.769)

#---Scrollbar
TextBar_Principal = ctk.CTkScrollbar(Ventana_Principal, orientation="vertical", width= ScrollBar_medida_X, height=ScrollBar_medida_Y, command=Tbox_Principal.yview, corner_radius=10)
TextBar_Principal.place(x=ScrollBar_X, y=ScrollBar_Y)

Tbox_Principal.configure(yscrollcommand=TextBar_Principal.set)

#---Fin

#---MAIN LOOP

Ventana_Principal.mainloop()

#---FIN