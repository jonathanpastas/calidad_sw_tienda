from flask import Flask, render_template ,request, session, redirect, url_for,flash
import hashlib

from bdatos import *

app = Flask(__name__)
app.secret_key='jsp1234'

@app.route('/')
def index() -> 'html':
    result = hashlib.md5(b'1234')
    print('equivale', result.digest())
    return render_template('index.html', titulo='HomeSmart')


@app.route('/login')
def login() -> 'html':
    return render_template('login.html', titulo='Iniciar Sesión')

#Metodo para Ingresar a la Sesion,Valida el Cliente

@app.route('/ingresar' ,methods=['POST'])
def ingreso() -> 'html':
  user=request.form['correo']
  clave = request.form['clave']
  validar=queryDatos(user,clave)

  if validar == True:
      perfilu = perfiluser(user)
      nombre = nombreuser(user)
      cedula = ciuser(user)
      session['username']=user
      session['pass']=clave
      session['perfiluser']=perfilu
      session['nombre']=nombre
      session['ci']=cedula
      return redirect(url_for('paginicio'))
  else :
       flash("Correo Electronico o Contraseña no son correctos.")
       return  redirect(url_for('login'))

#Metodo que redirige a la pagina de inicio del cliente
@app.route('/inicio')
def paginicio() -> 'html':

    if 'username' in session:
        print("true")
        #menu=menuopciones(str(session['perfiluser']))
        usuario=session['username']
        nom = str(session['nombre'])
        lista=listaproductosg()
        return render_template('cliente.html',titulo="HomeSmart | Bienvenido",lstp=lista)


    else :
        return redirect(url_for('index'))

#Metodo para Cerrar la Sesion
@app.route('/cerrarsesion')
def salir() ->'html':
    session.clear()
    return redirect(url_for('index'))



app.run(debug=True)
