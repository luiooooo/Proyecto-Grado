import tkinter as tk

#el .pack agrega lo que queramos a la interface

#PESTANA BASE

#Aqui creamos la ventana principal
VentanaPrincipal = tk.Tk()

#Titulo que aparece arriba de la ventana principal 
VentanaPrincipal.title("ClariSint MalwareText")

#Tamano base en el cual iniciara el programa
VentanaPrincipal.geometry("1500x800")

#Fin PESTANA BASE

#Botones

#Fin Botones

#TextBoxs

#Este es el textbox principal donde se ingresara el texto
TextBoxPRINCIPAL = tk.Text(VentanaPrincipal, padx=5, height= 40, width=200,  font=('Arial', 10))
TextBoxPRINCIPAL.pack(pady= 40)

#Fin TextBoxs

#LABELS

#Creo un texto, con label (Ventana a elegir, texto en si, fuente)
Texto1 = tk.Label(VentanaPrincipal, text="Prueba", font=('Arial', 20))
Texto1.pack()

#FIN LABELS

#Aqui se inicializa la ventan principal
VentanaPrincipal.mainloop()