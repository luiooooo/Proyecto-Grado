import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        print("Feedback enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar feedback: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    feedback = "Este es un mensaje de prueba de feedback."
    send_feedback(feedback)
