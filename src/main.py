import math
import os
import tkinter.simpledialog as sd

import customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu

import utils as ut
import db_connection as db
import sys

# Variables globales
procesando_texto = False
proyectos_abiertos = []
tabs = ["Original", "Texto", "DLLs", "Librerias", "Codigo", "Todo", "Reporte"] 
current_option = tabs[0]  # Opción predeterminada
contenido_guardado = {
    "Original": "",  
    "Texto": "",
    "DLLs": "",
    "Librerias": "",
    "Codigo": "",
    "Todo": "",
    "Reporte": ""
}

# ---FUNCIONES---
# Cambiar de pestaña al hacer clic en boton

def actualizar_tbox(nuevo_contenido):
    main_txt_box.delete("1.0", "end")
    main_txt_box.insert("1.0", nuevo_contenido)  
    
    
def cambiar_tab(tab_seleccionado):
    opcion_actual = tab_seleccionado
    contenido_tab = contenido_guardado[opcion_actual]
    if contenido_tab: 
        actualizar_tbox(contenido_tab)
    


def tbox_on_changed(event):
    contenido_guardado[current_option] = main_txt_box.get("1.0", "end")
 
def on_procesar_click():
    if (current_option == "Original" and contenido_guardado[current_option] != ""):
        process_txt_btn.configure(state="disabled") # Deshabilitar boton de procesar 
        buttons.configure(state="normal") # Habilitar botones secundarios
        #Direccion al backend de procesar
        
def on_exportar_click():
    carpeta_seleccionada = ctk.filedialog.askdirectory()
    if carpeta_seleccionada:
        nombre_proyecto = sd.askstring("Nombre de proyecto", "Ingrese el nombre del proyecto")
        ut.exportar_textos(carpeta_seleccionada, nombre_proyecto)

def on_guardar_click():
    ruta_archivo = ctk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if ruta_archivo:
        ut.guardar_json(ruta_archivo, contenido_guardado)
    
def on_cargar_click():
    ruta_archivo = ctk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if ruta_archivo and ruta_archivo not in proyectos_abiertos:
        # Agregar el archivo a la lista de proyectos abiertos
        proyectos_abiertos.append(ruta_archivo)
        contenido_guardado = ut.cargar_json(ruta_archivo)
        actualizar_tbox(contenido_guardado[current_option])
        
        # Agregar un botón para el proyecto en la lista de proyectos
        new_btn = ctk.CTkButton(project_list, text=os.path.basename(ruta_archivo), command=lambda: on_click_project(ruta_archivo))
        new_btn.pack(expand=True, fill="x", pady=10)
        
def  on_click_project(ruta):
    contenido_guardado = ut.cargar_json(ruta)
    actualizar_tbox(contenido_guardado[current_option])

# ---DISEÑO---
# Crear ventana principal
root = ctk.CTk()
root.title("Test Window")
root.minsize(1280,720) 
root.resizable(True, True)
root.state("zoomed") # Iniciar maximizado

# Definir estilo de la app
font_size = math.floor(20)
app_font = ctk.CTkFont(family="Times New Roman", size=font_size, weight="bold")
dark_gray = "#242424"

# ---MENU BAR-- 201F1F  1E1D1D-
menu = CTkMenuBar(master=root,bg_color="#201F1F")
m1 = menu.add_cascade("Archivo")
m2 = menu.add_cascade("Feedback")

dropdown1 = CustomDropdownMenu(widget=m1)
dropdown1.add_option(option="Abrir", command=lambda: on_cargar_click())
dropdown1.add_option(option="Guardar", command=lambda: on_guardar_click())

# Definir contenedor principal de la app
main_container = ctk.CTkFrame(root, fg_color=dark_gray)

menu.place()
main_container.pack(after=menu, fill="both", expand=True, padx=10, pady=6)

# Partes principales de la app
columna_general = ctk.CTkFrame(main_container, fg_color=dark_gray)
columna_proyectos = ctk.CTkFrame(main_container, fg_color=dark_gray)

columna_general.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
columna_proyectos.grid(row=0, column=1, sticky="nsew")

# Set column weights to make them 50% each
main_container.grid_columnconfigure(0, weight=74)
main_container.grid_columnconfigure(1, weight=26)
main_container.grid_rowconfigure(0, weight=1)


# Partes de Column General
button_row = ctk.CTkFrame(columna_general, fg_color=dark_gray)
content_row = ctk.CTkFrame(columna_general)

# Posicionar partes de Column General
button_row.grid(row=0, column=0, sticky="nsew")
content_row.grid(row=1, column=0, sticky="nsew")

# Set tamaño de partes de Column General
columna_general.grid_rowconfigure(0, weight=4)
columna_general.grid_rowconfigure(1, weight=96)
columna_general.grid_columnconfigure(0, weight=1)


# ---BUTTON ROW---

# Definir botones
buttons = ctk.CTkSegmentedButton(button_row, values=tabs, font=app_font, height=40, corner_radius=24, dynamic_resizing=True, command=cambiar_tab, state="disabled")
buttons.set(current_option) 

# Botones de accion
process_txt_btn = ctk.CTkButton(button_row, text="Procesar", font=app_font, hover_color="#E74C3C", command=on_procesar_click)
export_txt_btn = ctk.CTkButton(button_row, text="Exportar", font=app_font, hover_color="#E74C3C", command=on_exportar_click)

# Posicionar elementos dentro del contenedor
buttons.grid(row=0, column=0, sticky="nsew")
process_txt_btn.grid(row=0,column=1, sticky="nsew", padx=12)
export_txt_btn.grid(row=0,column=2, sticky="nsew") 


button_row.grid_columnconfigure(0, weight=10)
button_row.grid_columnconfigure(1, weight=8)
button_row.grid_columnconfigure(2, weight=8)


# ---CONTENT ROW---

# Textbox
main_txt_box = ctk.CTkTextbox(content_row, font=("Times New Roman", font_size), activate_scrollbars=False, border_width=3)
main_txt_box.bind("<KeyRelease>", tbox_on_changed)


# Code View (Incomplete)
code_view = ctk.CTkFrame(content_row, height=75, width=75, fg_color="#2B2B2B")

# Scrollbar
txt_scroll = ctk.CTkScrollbar(content_row, orientation="vertical", command=main_txt_box.yview, corner_radius=10)
main_txt_box.configure(yscrollcommand=txt_scroll.set)

# Posicionar elementos dentro del contenedor
main_txt_box.grid(row=0, column=0, sticky="nsew")
code_view.grid(row=0, column=1, sticky="nsew")
txt_scroll.grid(row=0, column=2, sticky="nsew")

# Configurar tamaño de elementos
content_row.grid_rowconfigure(0, weight=1) # Expandir elementos en el eje vertical
content_row.grid_columnconfigure(0, weight=97)
content_row.grid_columnconfigure(1, weight=1)
content_row.grid_columnconfigure(2, weight=1)


# ---COLUMN PROYECTOS---

# Lista de proyectos
projects_lbl = ctk.CTkLabel(columna_proyectos, text="Proyectos abiertos", font=app_font, text_color="#1ABC9C")
project_list = ctk.CTkScrollableFrame(master=columna_proyectos, border_width=3)

# Posicionar elementos dentro del contenedor
projects_lbl.grid(row=0,column=0, sticky="nsew")
project_list.grid(row=1,column=0, sticky="nsew")

# Configurar tamaño de elementos
columna_proyectos.grid_columnconfigure(0, weight=1) # Expandir elementos en el eje horizontal
columna_proyectos.grid_rowconfigure(1, weight=90)  # Hacer que la lista de proyectos ocupe el 90% del espacio vertical

# Start app
if __name__ == "__main__":
    db_con = db.get_db_connection()
    if db_con is None:
        print("Error al conectar a la base de datos")
        sys.exit(1)
    root.mainloop()
   