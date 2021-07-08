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

@app.route('/ingresar' ,methods=['POST'])
def ingreso() -> 'html':
  user=request.form['correo']
  clave = request.form['clave']
  validar=queryDatos(user,clave)
  #print(validar)

  #print(nombre)

  #print(perfil)

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
       flash("Error al Inciar Sesion. Por Favor Verifique sus Credenciales de Acceso")
       return  redirect(url_for('login'))

@app.route('/inicio')
def paginicio() -> 'html':

    if 'username' in session :
        print("true")
        #menu=menuopciones(str(session['perfiluser']))
        usuario=session['username']
        nom = str(session['nombre'])
        return render_template('cliente.html')


    else :
        return redirect(url_for('index'))


app.run(debug=True)
