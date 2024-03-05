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

#--Obtener resolucion

ancho_pantalla = Ventana_Principal.winfo_screenwidth()
alto_pantalla = Ventana_Principal.winfo_screenheight()
Ancho_inicio = math.floor(ancho_pantalla // 1.2)
Alto_inicio = math.floor(alto_pantalla // 1.2)

Ventana_Principal.geometry(f"{Ancho_inicio}x{Alto_inicio}+100+0")

#--Fin

#---Fin

#--Tamaño botones
#Diferencia de 0.078
BTN_General_Y = math.floor(alto_pantalla * 0.024)
BTN_Original_X = math.floor(ancho_pantalla * 0.007)
BTN_Plano_X = math.floor(ancho_pantalla * 0.085)
BTN_DLLS_X = math.floor(ancho_pantalla * 0.163)
BTN_Librerias_X = math.floor(ancho_pantalla * 0.241)
BTN_Codigo_X = math.floor(ancho_pantalla * 0.319)
BTN_Completo_X = math.floor(ancho_pantalla * 0.397)
BTN_Reporte_X = math.floor(ancho_pantalla * 0.475)

Letra = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.00049)
heigh_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.018)
width_valor = math.floor(((ancho_pantalla+alto_pantalla)/2)*0.1 )

#---Botones
BTN_Texto_Original = ctk.CTkButton(Ventana_Principal, text="ORIGINAL", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_Original.place(x=BTN_Original_X, y=BTN_General_Y)
BTN_Texto_Plano = ctk.CTkButton(Ventana_Principal, text="TEXTO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_Plano.place(x=BTN_Plano_X, y=BTN_General_Y)
BTN_Texto_Dlls = ctk.CTkButton(Ventana_Principal, text="DLLS", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_Dlls.place(x=BTN_DLLS_X, y=BTN_General_Y)
BTN_Texto_Librerias = ctk.CTkButton(Ventana_Principal, text="LIBRERIAS", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_Librerias.place(x=BTN_Librerias_X, y=BTN_General_Y)
BTN_Texto_Codigo = ctk.CTkButton(Ventana_Principal, text="CODIGO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_Codigo.place(x=BTN_Codigo_X, y=BTN_General_Y)
BTN_Texto_TODO = ctk.CTkButton(Ventana_Principal, text="TODO", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))
BTN_Texto_TODO.place(x=BTN_Completo_X, y=BTN_General_Y)
BTN_Texto_REPORTE = ctk.CTkButton(Ventana_Principal, text="REPORTE", height=heigh_valor, width=width_valor, font=("Times New Roman", Letra, "bold"))

#---Fin

#---TextBox Principal

#Tamano Textbox
Tbox_X = math.floor(ancho_pantalla * 0.007)
Tbox_Y = math.floor(alto_pantalla * 0.055)
Altura_Tbox = math.floor(alto_pantalla * 0.765)
Anchura_Tbox = math.floor(alto_pantalla * 0.90)

Tbox_Principal = ctk.CTkTextbox(Ventana_Principal,height=Altura_Tbox, width=Anchura_Tbox, font=("Times New Roman", Letra))
Tbox_Principal.place(x= Tbox_X, y= Tbox_Y)

#---Fin

#---MAIN LOOP

Ventana_Principal.mainloop()

#---FIN