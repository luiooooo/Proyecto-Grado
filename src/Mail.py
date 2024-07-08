from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
import smtplib
import customtkinter as ctk

# Configuración del correo electrónico
email_sender = 'ProyectoDeGradoClarisint@outlook.com'
email_password = 'ClarisintMalwareText*1'  # Asegúrate de manejar esto de manera segura
email_receiver = 'ProyectoDeGradoClarisint@outlook.com'

def send_feedback(feedback_text):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = 'Feedback de la aplicación'
    msg.attach(MIMEText(feedback_text, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)  # Cambia esto si es necesario
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        messagebox.showinfo("Éxito", "Hemos recibido su comentario, gracias")
        feedback.destroy()  # Cierra la ventana de feedback después de enviar
    except Exception as e:
        print(f"Error al enviar feedback: {e}")

def enviar_button_click():
    feedback_text = feedback_txt_box.get("1.0", "end-1c")  # Obtener el texto del Textbox
    send_feedback(feedback_text)

def open_feedback():
    global feedback
    feedback = ctk.CTk()
    feedback.title("Contactanos")
    feedback.minsize(1280, 720)
    feedback.resizable(True, True)
    feedback.state("zoomed")  # Iniciar maximizado

    # Configurar la disposición usando grid
    feedback.grid_rowconfigure(0, weight=9)  # 90% de la pantalla
    feedback.grid_rowconfigure(1, weight=1)  # 10% restante para los botones
    feedback.grid_columnconfigure(0, weight=1)

    # Creación del Textbox para el feedback
    global feedback_txt_box
    feedback_txt_box = ctk.CTkTextbox(feedback, font=("Helvetica", 18), activate_scrollbars=True, border_width=3)
    feedback_txt_box.grid(row=0, column=0, sticky="nsew")

    # CTkFrame para los botones
    button_CTkFrame = ctk.CTkFrame(feedback)
    button_CTkFrame.grid(row=1, column=0, sticky="ew")

    # Botón para enviar el feedback
    enviar_button = ctk.CTkButton(button_CTkFrame, text="Enviar", command=enviar_button_click)
    enviar_button.pack(side=ctk.LEFT, padx=10, pady=10)

    # Botón para cancelar
    cancelar_button = ctk.CTkButton(button_CTkFrame, text="Cancelar", command=feedback.destroy)
    cancelar_button.pack(side=ctk.RIGHT, padx=10, pady=10)

    feedback.mainloop()  # Esta función se llama explícitamente cuando se quiere abrir la ventana de feedback
