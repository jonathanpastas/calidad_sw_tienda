# Importamos el ModuMódulo

import pywhatkit

# Usamos Un try-except
try:
    # Enviamos el mensaje
    pywhatkit.sendwhatmsg("+593979178408", "Hello, World", 11,42)

    print("Mensaje Enviado")



except:

    print("Ocurrio Un Error")
