import smtplib

def enviarcorreo(mensaje):

    print(mensaje)
    # Reemplaza estos valores con tus credenciales de Google Mail

    try:
        from_addr = [email]
        to = [destinatario]
        message = mensaje
        username = [email_remitente]
        password = [contrasenia_email]
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, message)

        server.quit()

        return True
    except:
        return False


