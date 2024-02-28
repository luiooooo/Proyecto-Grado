import tkinter as tk

""" Significado de comentarios
# desarrollo
#---Titulo
#--Subtitulo
"""

#PESTANA BASE

#---Aqui creamos la ventana principal
VentanaPrincipal = tk.Tk()

#Titulo que aparece arriba de la ventana principal 
VentanaPrincipal.title("ClariSint MalwareText")

#Tamano base en el cual iniciara el programa
VentanaPrincipal.geometry("1600x900")

VentanaPrincipal.resizable(width=False, height=False)

#---Fin PESTANA BASE

#---Comando de Botones

def BNTFunc_Texto_Original():
    print("PRESIONAR")
def BTNFunc_Texto_Plano():
    x = 5

#---Fin Comando de Botones

#---Botones
    
#--Botones para ver texto
    
#159 Distancia de botones
BTN_Ver_Texto_Original = tk.Button(VentanaPrincipal, text="TEXTO ORIGINAL", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Texto_Original.place(x=12,y=15, relwidth=0.1)

BTN_Ver_Texto_Plano = tk.Button(VentanaPrincipal, text="TEXTO PLANO", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Texto_Plano.place(x=171,y=15, relwidth=0.1)

BTN_Ver_DLLS = tk.Button(VentanaPrincipal, text="DLLS", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_DLLS.place(x=330,y=15, relwidth=0.1)

BTN_Ver_Librerias = tk.Button(VentanaPrincipal, text="LIBRERIAS", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Librerias.place(x=489,y=15, relwidth=0.1)

BTN_Ver_Codigo = tk.Button(VentanaPrincipal, text="CODIGO", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Codigo.place(x=648,y=15, relwidth=0.1)

BTN_Ver_Completo = tk.Button(VentanaPrincipal, text="TODO", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Completo.place(x=807,y=15, relwidth=0.1)

BTN_Ver_Reporte = tk.Button(VentanaPrincipal, text="REPORTE", command=BNTFunc_Texto_Original, width=16, height=1, font=("Times New Roman",12, "bold"))
BTN_Ver_Reporte.place(x=966,y=15, relwidth=0.1)

#--Fin Botones para ver texto

#--BOTON PROCESAR TEXTO

BTN_PROCESAR_TEXTO = tk.Button(VentanaPrincipal, text="PROCESAR", width=18, height=2, font=("Times New Roman", 16, "bold"))
BTN_PROCESAR_TEXTO.place(x=1279, y=800)

#--FIN BOTON PROCESAR TEXTO

#---Fin Botones

#---MARCOS

MARCO_Lista = tk.Frame(VentanaPrincipal, bg='white', width=370, height=735, bd=2, relief=tk.SOLID)
MARCO_Lista.place(x=1200, y= 45)

#---FIN MARCOS

#---TextBoxs

#Este es el textbox principal donde se ingresara el texto
TextBoxPRINCIPAL = tk.Text(VentanaPrincipal, padx=7, pady = 7, height= 39, width=123,  font=('Times New Roman', 14), borderwidth=2, relief=tk.SOLID)
TextBoxPRINCIPAL.place(x=12 , y=51)

#---Fin TextBoxs

#---LABELS

LBL_LISTA = tk.Label(text="P R O Y E C T O S", font=('Times New Roman', 18, 'bold', 'underline'))
LBL_LISTA.place(x=1283, y= 10)

#---FIN LABELS

#---Aqui se inicializa la ventan principal
VentanaPrincipal.mainloop()