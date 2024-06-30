import math
import os
import tkinter.simpledialog as sd
 
import customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from tkinter import messagebox

import utils as ut
import db_connection as db
import backend
import sys

DEFAULT_PROJECT = "Untitled"
DEFAULT_TAB = "Input"

# Variables globales
procesando_texto = False
proyectos_abiertos = []
current_proj_path = DEFAULT_PROJECT
tabs = ["Input", "Texto", "Librerias", "Redes", "Codigo", "Todo", "Reporte"] 
current_option = DEFAULT_TAB  # Opción predeterminada
window_title = f"{DEFAULT_PROJECT} - Clarisint"

contenido_guardado = {
    "Input": "",
    "Texto": [],
    "Librerias": [],
    "Redes": [],
    "Codigo": [],
    "Todo": [],
    "Reporte": []
}


# ---FUNCIONES---
# Cambiar de pestaña al hacer clic en boton
def get_txt_color(riskId):
    match(riskId):
        case 1:
            return "malicioso"
        case 2:
            return "explotable"
        case 3:
            return "vulnerable"
        case _:
            return "default"


def insert_text(content, risk_id=None):
    color_tag = get_txt_color(risk_id) if risk_id else "default"
    main_txt_box.insert("end", content + "\n", color_tag)


def actualizar_tbox(nuevo_contenido=None):
    global current_option  # Ensure we can modify the global variable if needed
    main_txt_box.delete("1.0", "end")
    if nuevo_contenido is None:
        nuevo_contenido = contenido_guardado.get(current_option, [])
    if current_option == "Input":
        insert_text(contenido_guardado["Input"])
    elif nuevo_contenido:
        for line in nuevo_contenido:
            if isinstance(line, tuple):
                content, riskId = line
                insert_text(content, riskId)
            else:
                insert_text(line)
    else:
        insert_text("No se encontró contenido en esta categoría.")
        
    
def cambiar_tab(tab):
    global current_option
    # Cambiar tab actual
    buttons.set(tab)
    current_option = tab

    main_txt_box.configure(state="normal") # Habilitar el textbox para insertar texto    
    actualizar_tbox(contenido_guardado[tab])
    if tab != "Input":
        main_txt_box.configure(state="disabled")


def tbox_on_changed(event):
    if current_option == "Input" and not procesando_texto: 
        process_txt_btn.configure(state="normal") # Habilitar boton de procesar
        contenido_guardado[current_option] = main_txt_box.get("1.0", "end")


def set_processed_text(content):
    global contenido_guardado

    for key, value in content.items(): 
        contenido_guardado[key] = value
        risks_found = [content for content in value if content[-1] > 0] #Filtrar solo los que tienen riesgo
        if len(risks_found) > 0:
            section_title = f"{key}: {len(risks_found)}"
            contenido_guardado["Reporte"].append((section_title, "title")) # Agregar titulo por categoría encontrada
            contenido_guardado["Reporte"].extend(risks_found)
            contenido_guardado["Reporte"].append("\n")
        contenido_guardado["Todo"].extend(value)


def on_procesar_click():
    if (current_option == "Input" and contenido_guardado[current_option] != ""):
        process_txt_btn.configure(state="disabled",text="Procesando...") # Deshabilitar boton de procesar
        ut.limpiar_textos(contenido_guardado) # Limpiar textos

        # Procesar texto
        resultado = backend.procesar_texto(contenido_guardado["Input"]) 
        set_processed_text(resultado)

        # Fin del procesamiento
        buttons.configure(state="normal") # Habilitar botones secundarios
        process_txt_btn.configure(text="Procesar")

        # Actualizar contenido en la pestaña de reporte
        buttons.set("Reporte")
        cambiar_tab("Reporte")


def on_exportar_click():
    carpeta_seleccionada = ctk.filedialog.askdirectory()
    if carpeta_seleccionada:
        nombre_proyecto = sd.askstring("Nombre de proyecto", "Ingrese el nombre del proyecto")
        ut.exportar_textos(carpeta_seleccionada, nombre_proyecto, contenido_guardado)

# PROJECT METHODS
def is_current_project(route):
    global current_proj_path
    return current_proj_path == route

def update_window_title(proj=None):
    new_proj_name = proj if proj else DEFAULT_PROJECT
    root.title(f"{new_proj_name} - Clarisint") 

def handle_project_saving(project_path=DEFAULT_PROJECT):
    global current_proj_path, contenido_guardado, proyectos_abiertos
    if ut.is_content_empty(contenido_guardado):
        return  # Exit if there's no content to save

    if current_proj_path in (DEFAULT_PROJECT, None):
        on_guardar_click()  # Trigger save dialog if no project path is set
    else:
        ut.guardar_json(current_proj_path, contenido_guardado)  # Save to the existing path

def on_click_project(ruta):
    global current_proj_path, contenido_guardado, current_option  # Declare to modify global variables
    current_proj_path = ruta
    update_window_title(ruta)
    contenido_guardado = ut.cargar_json(ruta)
    cambiar_tab(DEFAULT_TAB)
    actualizar_tbox(contenido_guardado[current_option])

def add_project_button(project_path):
    new_btn = ctk.CTkButton(project_list, text=os.path.basename(project_path), command=lambda project_path=project_path: on_click_project(project_path) if is_current_project(project_path) else "normal")
    new_btn.pack(expand=True, fill="x", pady=10)

def on_guardar_click():
    global current_proj_path
    ruta_archivo = ctk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if ruta_archivo == "":
        return False
    
    current_proj_path = ruta_archivo
    proyectos_abiertos.append(ruta_archivo)
    ut.guardar_json(current_proj_path, contenido_guardado)  # Save to the existing path
    update_window_title(ruta_archivo)
    add_project_button(ruta_archivo)
    return True

def on_cargar_click():
    global current_proj_path, contenido_guardado  # Declare to modify global variables

    ruta_archivo = ctk.filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if ruta_archivo and ruta_archivo not in proyectos_abiertos:
        # Agregar el archivo a la lista de proyectos abiertos
        update_window_title(ruta_archivo)
        current_proj_path = ruta_archivo
        proyectos_abiertos.append(ruta_archivo)
        contenido_proyecto = ut.cargar_json(ruta_archivo)

        if contenido_proyecto is None:
            # Display an error message if the JSON file could not be loaded
            messagebox.showerror("Error", "No se pudo cargar el archivo JSON.")
        else:
            contenido_guardado = contenido_proyecto
            # Safely delete "Input" key from contenido_guardado
            contenido_guardado.pop("Input", None)  # Use pop with None as default value to avoid KeyError
            if not ut.is_content_empty(contenido_guardado):
                buttons.configure(state="normal")  # Enable the segmented buttons
                cambiar_tab(DEFAULT_TAB)
            elif "Input" not in contenido_guardado or contenido_guardado.get("Input", "") != "":
                cambiar_tab("Input")
                process_txt_btn.configure(state="normal")  # Enable the process button

            actualizar_tbox(contenido_guardado[current_option])
            # Agregar un botón para el proyecto en la lista de proyectos
            add_project_button(ruta_archivo)

def on_nuevo_click():
    global contenido_guardado
    result = messagebox.askyesnocancel("Guardar", "¿Desea guardar el proyecto actual?")
    if result is not None:
        if result is True: 
            save_successful = on_guardar_click()  # Save the project if the user agrees
            if not save_successful:
                return  # Do not proceed if the user cancelled the save dialog

        main_txt_box.delete("1.0", "end")
        cambiar_tab(DEFAULT_TAB)  # Switch to the input tab
        current_proj_path = None  # Reset the current project path
        ut.limpiar_textos(contenido_guardado, True)
        actualizar_tbox(contenido_guardado)  # Needs modification to split information appropriately
        update_window_title(DEFAULT_PROJECT)  # Reset the window title


# ---DISEÑO---
# Crear ventana principal
root = ctk.CTk()
root.title(window_title)
root.minsize(1280,720) 
root.resizable(True, True)
root.state("zoomed") # Iniciar maximizado

# Definir estilo de la app
font_size = math.floor(18)
app_font = ctk.CTkFont(family="Helvetica", size=font_size, weight="bold")
dark_gray = "#242424"

# ---MENU BAR-- 201F1F  1E1D1D-
menu = CTkMenuBar(master=root,bg_color="#201F1F")
m1 = menu.add_cascade("Archivo")
m2 = menu.add_cascade("Feedback")

dropdown1 = CustomDropdownMenu(widget=m1)
dropdown1.add_option(option="Nuevo proyecto", command=lambda: on_nuevo_click())
dropdown1.add_option(option="Abrir proyecto", command=lambda: on_cargar_click())
dropdown1.add_option(option="Guardar proyecto", command=lambda: handle_project_saving())

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
process_txt_btn = ctk.CTkButton(button_row, text="Procesar", state= "disabled", font=app_font, hover_color="#E74C3C", command=on_procesar_click)
export_txt_btn = ctk.CTkButton(button_row, text="Exportar", font=app_font, hover_color="#E74C3C", command=on_exportar_click)
#opt_txt_select = ctk.CTkOptionMenu()

# Posicionar elementos dentro del contenedor
buttons.grid(row=0, column=0, sticky="nsew")
process_txt_btn.grid(row=0,column=1, sticky="nsew", padx=12)
export_txt_btn.grid(row=0,column=2, sticky="nsew") 


button_row.grid_columnconfigure(0, weight=10)
button_row.grid_columnconfigure(1, weight=8)
button_row.grid_columnconfigure(2, weight=8)


# ---CONTENT ROW---

# Textbox
main_txt_box = ctk.CTkTextbox(content_row, font=("Helvetica", font_size), activate_scrollbars=True, border_width=3)
main_txt_box.tag_config("explotable", foreground="yellow")
main_txt_box.tag_config("vulnerable", foreground="orange")
main_txt_box.tag_config("malicioso", foreground="red")
main_txt_box.tag_config("title", foreground="medium purple")
main_txt_box.tag_config("default", foreground="white")
main_txt_box.bind("<KeyRelease>", tbox_on_changed)


# Posicionar elementos dentro del contenedor
main_txt_box.grid(row=0, column=0, sticky="nsew")


# Configurar tamaño de elementos
content_row.grid_rowconfigure(0, weight=1) # Expandir elementos en el eje vertical
content_row.grid_columnconfigure(0, weight=1)


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
   