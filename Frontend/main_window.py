import tkinter as tk

#PESTANA BASE

#-----Aqui creamos la ventana principal
VentanaPrincipal = tk.Tk()

#Titulo que aparece arriba de la ventana principal 
VentanaPrincipal.title("ClariSint MalwareText")

#Tamano base en el cual iniciara el programa
VentanaPrincipal.geometry("1600x900")

VentanaPrincipal.resizable(width=False, height=False)

#-----Fin PESTANA BASE

#-----Comando de Botones

def BNTFunc_Texto_Original():
    print("PRESIONAR")
def BTNFunc_Texto_Plano():
    x = 5

#-----Fin Comando de Botones

#-----Botones

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

#-----Fin Botones

#-----MARCOS

MARCOBLANCO = tk.Frame(VentanaPrincipal, bg='white', width=50, height=50)
MARCOBLANCO.place(x=1200, y= 20)

#-----FIN MARCOS

#-----TextBoxs

#Este es el textbox principal donde se ingresara el texto
TextBoxPRINCIPAL = tk.Text(VentanaPrincipal, padx=5, height= 39, width=123,  font=('Times New Roman', 14))
TextBoxPRINCIPAL.place(x=12 , y=51)

#-----Fin TextBoxs

#-----LABELS

LBL_LISTA = tk.Label(text="P R O Y E C T O S", font=('Times New Roman', 18, 'bold', 'underline'))
LBL_LISTA.place(x=1200, y= 10)
#-----FIN LABELS

#-----Aqui se inicializa la ventan principal
VentanaPrincipal.mainloop()