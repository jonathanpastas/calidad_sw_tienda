from flask import Flask, render_template ,request, session, redirect, url_for,flash
from bdatos import *

app = Flask(__name__)
app.secret_key='jsp1234'

################# METODOS DONDE SE RENDERIZAN PAGINAS WEB ##################
@app.route('/')
def index() -> 'html':

    return render_template('index.html', titulo='HomeSmart')


@app.route('/login')
def login() -> 'html':
    return render_template('login.html', titulo='Iniciar Sesión')

@app.route('/registro')
def cuentanueva() -> 'html':
    return render_template('registrarse.html', titulo='Crear una Cuenta Nueva')


@app.route('/verproductos')
def listaproductos() -> 'html':
    lista = listaproductosg()
    numero=numerogeneralpro()
    nug=numerogeneralprog()
    nua = numerogeneralproa()
    nux = numerogeneralprox()
    prog,proa,progx=prodgoogle();
    return render_template('productosbase.html', titulo='Lista de Productos',lstp=lista,np=numero,ng=nug,na=nua,nx=nux,go=prog,am=proa,xi=progx)

@app.route('/productod',methods=['GET'])
def productogeneral()->'html':

        prod = request.args.get('id')

        datpro,cat=mostrarproducto(prod)
        daca=mprodcat(cat,prod)
        print(datpro)

        return render_template('detallep.html',titulo="HomeSmart",pr=datpro,pc=daca)



#################METODOS PRINCIPALES DE FUNCIONAMIENTO DEL SITIO ##################
#Metodo para Ingresar a la Sesion,Valida el Cliente

@app.route('/ingresar' ,methods=['POST'])
def ingreso() -> 'html':
  user=request.form['correo']
  clave1 = request.form['contrasenia']
  validar=queryDatos(user, clave1)

  if validar == True:
      perfilu = perfiluser(user)
      nombre = nombreuser(user)
      cedula = ciuser(user)
      session['username']=user
      session['pass']=clave1
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
        return redirect(url_for('login'))

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

@app.route('/comparar')
def vcomparar() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        listap = listaproductosg()

        return render_template('comparacion.html', titulo='Comparación de Productos',nomb=nom,prod=listap)

    else :
        return redirect(url_for('index'))


@app.route('/pcomparar',methods=['POST'])
def comparaciones()->'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        p1 = request.form['prod1']
        p2 = request.form['prod2']
        proa = verprocompara(p1)
        prob = verprocompara(p2)

        return render_template('vercomparaciones.html', titulo='Comparación de Productos', nomb=nom, pa=proa,pb=prob)

    else:
        return redirect(url_for('index'))


@app.route('/ayuda')
def ayudasclie()->'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])

        return render_template('ayudaclie.html', titulo='Comparación de Productos', nomb=nom)

    else:
        return redirect(url_for('index'))


@app.route('/agcarrito',methods=['POST'])
def carritoag()->'html':
    if 'username' in session:
        cedula=session['ci']
        usuario = session['username']
        nom = str(session['nombre'])
        npro = request.form['numc']
        idpro = request.form['prodId']
        ingresar= agcarrito(cedula,npro,idpro);

        if ingresar == True:
            flash("Se ha añadido al carrito correctamente")
            return redirect(url_for('paginicio'))
        else:
            flash("Error al añadir el producto verifique si existe stock")
            return redirect(url_for('paginicio'))

@app.route('/vercarrito')
def vcarritocompra()->'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        cedula = session['ci']
        valores=visualcarrito(cedula)
        return render_template('vercarrito.html', titulo='Carrito de Compras', nomb=nom,carpro=valores)

    else:
        return redirect(url_for('index'))



###########FIN DEL PROGRAMA #################
app.run(debug=True)
