from flask import Flask, render_template ,request, session, redirect, url_for,flash
from bdatos import *

app = Flask(__name__)
app.secret_key='jsp1234'

@app.route('/')
def index() -> 'html':

    return render_template('index.html', titulo='HomeSmart')


@app.route('/login')
def login() -> 'html':
    return render_template('login.html', titulo='Iniciar Sesión')

@app.route('/registro')
def cuentanueva() -> 'html':
    return render_template('registrarse.html', titulo='Crear una Cuenta Nueva')

#################METODOS PRINCIPALES DE FUNCIONAMIENTO DEL SITIO ##################
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
        return render_template('cliente.html',titulo="HomeSmart",lstp=lista,nomb=nom)


    else :
        return redirect(url_for('index'))

#Metodo para Cerrar la Sesion
@app.route('/cerrarsesion')
def salir() ->'html':
    session.clear()
    return redirect(url_for('index'))


@app.route('/producto',methods=['GET'])
def mostrarprod()->'html':

    if 'username' in session:
        print("true")
        #menu=menuopciones(str(session['perfiluser']))
        usuario=session['username']
        nom = str(session['nombre'])
        prod = request.args.get('id')

        datpro,cat=mostrarproducto(prod)
        daca=mprodcat(cat,prod)
        print(datpro)

        return render_template('producto.html',titulo="HomeSmart",nomb=nom,pr=datpro,pc=daca)


    else :
        return redirect(url_for('index'))

@app.route('/ingresarclie',methods=['POST'])
def ingusuario()->'html':

        cedula = request.form['cedula']
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['domicilio']
        correo = request.form['correo']
        clave = request.form['contrasenia']

        ingresar=nuevocliente(cedula, nombre, apellido, telefono, direccion, correo, clave)

        if ingresar == True:
            flash("Su Proceso de ha completado con Exito,ahora ingrese con su correo y contraseña registrados")
            return redirect(url_for('login'))
        else:
            flash("Error al Ingresar el Usuario Verifique que la Información Ingresada sea Correcta")
            return redirect(url_for('cuentanueva'))


app.run(debug=True)
