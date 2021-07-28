import smtplib

def enviarcorreo(mensaje):

    print(mensaje)
    # Reemplaza estos valores con tus credenciales de Google Mail

    try:
        from_addr = 'cpruebas285@gmail.com'
        to = 'jonathanpastas@hotmail.com'
        message = mensaje
        username = 'cpruebas285@gmail.com'
        password = '@7080uiosT'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, message)

        server.quit()

        return True
    except:
        return False


